"""Rebuilds the auto-generated sections of README.md from the GitHub API.
Standard library only. Sections it owns (between marker comments):
  STATS     - one-line summary numbers
  PROJECTS  - every public repo I built (forks and archived repos excluded)
  DNA       - language mix across those repos
  COMMITS   - latest commits across my most recently active repos
"""
import json, os, re, sys, urllib.request
from collections import Counter
from datetime import datetime, timezone

USER = "Gowtham232004"
SKIP = {USER}  # the profile repo itself
API = "https://api.github.com"


def get(path):
    headers = {"Accept": "application/vnd.github+json", "User-Agent": "readme-updater"}
    token = os.environ.get("GITHUB_TOKEN")
    if token:
        headers["Authorization"] = f"Bearer {token}"
    with urllib.request.urlopen(urllib.request.Request(API + path, headers=headers), timeout=20) as r:
        return json.load(r)


def clean(s, n):
    return (s or "").replace("|", "/").replace("\n", " ").strip()[:n]


def projects_block(repos):
    rows = ["| Project | What it is | Stack | Last push |", "|---|---|---|---|"]
    for r in repos:
        desc = clean(r["description"], 110) or "—"
        rows.append(f"| [**{r['name']}**]({r['html_url']}) | {desc} | {r['language'] or '—'} | `{r['pushed_at'][:10]}` |")
    return "\n".join(rows)


def language_totals(repos):
    total = Counter()
    for r in repos:
        try:
            total.update(get(f"/repos/{USER}/{r['name']}/languages"))
        except Exception:
            pass
    return total


def dna_block(total):
    s = sum(total.values())
    if not s:
        return None
    lines = []
    for lang, b in total.most_common(6):
        pct = b / s * 100
        filled = round(pct / 5)
        lines.append(f"{lang:<12} {'█' * filled}{'░' * (20 - filled)} {pct:4.1f}%")
    return "```text\n" + "\n".join(lines) + "\n```"


def stats_block(repos, total):
    kb = sum(total.values()) / 1024
    today = datetime.now(timezone.utc).strftime("%d %b %Y")
    return (f"**{len(repos)}** original repositories · **{len(total)}** languages · "
            f"**{kb:,.0f} KB** of code · refreshed `{today}` (UTC)")


def commits_block(repos):
    items = []
    for r in repos[:4]:
        try:
            for c in get(f"/repos/{USER}/{r['name']}/commits?per_page=3"):
                items.append((c["commit"]["author"]["date"], r["name"], c))
        except Exception:
            pass
    if not items:
        return None
    items.sort(key=lambda x: x[0], reverse=True)
    rows = ["| Date | Repo | Commit | What changed |", "|---|---|---|---|"]
    for date, name, c in items[:6]:
        rows.append(f"| `{date[:10]}` | {name} | [`{c['sha'][:7]}`]({c['html_url']}) | {clean(c['commit']['message'].split(chr(10))[0], 70)} |")
    return "\n".join(rows)


def replace(text, tag, body):
    if body is None:
        return text  # keep old content if an API call failed
    pat = rf"<!--START_{tag}-->.*?<!--END_{tag}-->"
    return re.sub(pat, lambda m: f"<!--START_{tag}-->\n{body}\n<!--END_{tag}-->", text, flags=re.S)


def main():
    all_repos = get(f"/users/{USER}/repos?per_page=100&type=owner&sort=pushed")
    mine = [r for r in all_repos if not r["fork"] and not r["archived"] and r["name"] not in SKIP]
    mine.sort(key=lambda r: r["pushed_at"], reverse=True)
    if not mine:
        sys.exit("no repos found")

    totals = language_totals(mine)
    text = open("README.md", encoding="utf-8").read()
    new = replace(text, "STATS", stats_block(mine, totals) if totals else None)
    new = replace(new, "PROJECTS", projects_block(mine))
    new = replace(new, "DNA", dna_block(totals))
    new = replace(new, "COMMITS", commits_block(mine))
    if new != text:
        open("README.md", "w", encoding="utf-8").write(new)
        print("README updated")
    else:
        print("no changes")


if __name__ == "__main__":
    main()
