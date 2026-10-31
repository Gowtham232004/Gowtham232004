"""Rebuilds the auto-generated sections of README.md from the GitHub API.
Standard library only. Sections it owns (between marker comments):
  STATS     - one-line summary numbers
  PROJECTS  - every public repo I built (forks, archived, duplicates, upstream copies excluded)
  DNA       - language mix across those repos
  COMMITS   - my latest commits across my most recently active repos
Tables never contain blank cells: curated text > GitHub description > generated fallback.
"""
import json, os, re, sys, urllib.request
from collections import Counter
from datetime import datetime, timezone

USER = "Gowtham232004"
# Not shown in the generated tables: the profile repo, a duplicate of github-auditor,
# and an upstream open-source project I only keep a copy of.
SKIP = {USER, "github_auditor", "story-spark-ai"}
API = "https://api.github.com"

# Curated one-liners (verified against the code). Anything missing falls back to the
# repo's GitHub description, then to a generated line, so no cell is ever empty.
DESCRIPTIONS = {
    "Skill_Proof": "Developer credibility platform: repo-grounded assessment, Docker-sandboxed challenges, HMAC-signed badges. Team of 3.",
    "github-auditor": "FastAPI service that scores how authentic a GitHub profile looks from its commit history, with 7 red-flag detectors and AI insights.",
    "github-auditor-frontend": "Next.js 16 dashboard for GitHub Auditor: results, profile compare, history and shareable badge pages.",
    "Dish_Management_System": "Starter layout for a dish and menu platform: Spring Boot 3.2 backend (Security, JPA, JWT dependencies) and a React 19 client. Business logic not built yet.",
    "Salesforce_Internship_Tracker": "Salesforce internship tracker: 4 custom objects, 3 Apex triggers, 5 Apex classes and 3 validation rules.",
}


def get(path):
    headers = {"Accept": "application/vnd.github+json", "User-Agent": "readme-updater"}
    token = os.environ.get("GITHUB_TOKEN")
    if token:
        headers["Authorization"] = f"Bearer {token}"
    with urllib.request.urlopen(urllib.request.Request(API + path, headers=headers), timeout=20) as r:
        return json.load(r)


def clean(s, n):
    return (s or "").replace("|", "/").replace("\n", " ").strip()[:n]


def describe(r):
    text = DESCRIPTIONS.get(r["name"]) or clean(r["description"], 140)
    return text or f"{r['language'] or 'Code'} project, last updated {r['pushed_at'][:10]}."


def projects_block(repos):
    rows = ["| Project | What it is | Stack | Last push |", "|---|---|---|---|"]
    for r in repos:
        rows.append(f"| [**{r['name']}**]({r['html_url']}) | {describe(r)} | {r['language'] or 'Mixed'} | `{r['pushed_at'][:10]}` |")
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
    for r in repos[:5]:
        try:
            for c in get(f"/repos/{USER}/{r['name']}/commits?author={USER}&per_page=4"):
                msg = c["commit"]["message"].split("\n")[0]
                if msg.startswith("Merge"):
                    continue
                items.append((c["commit"]["author"]["date"], r["name"], c, msg))
        except Exception:
            pass
    if not items:
        return None
    items.sort(key=lambda x: x[0], reverse=True)
    rows = ["| Date | Repo | Commit | What changed |", "|---|---|---|---|"]
    for date, name, c, msg in items[:6]:
        rows.append(f"| `{date[:10]}` | {name} | [`{c['sha'][:7]}`]({c['html_url']}) | {clean(msg, 72)} |")
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
