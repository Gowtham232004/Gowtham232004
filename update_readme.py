import json, re, urllib.request

REPO = "Gowtham232004/Skill_Proof"
URL = f"https://api.github.com/repos/{REPO}/commits?per_page=5"

req = urllib.request.Request(URL, headers={"Accept": "application/vnd.github+json", "User-Agent": "readme-updater"})
commits = json.load(urllib.request.urlopen(req))

rows = []
for c in commits:
    msg = c["commit"]["message"].split("\n")[0].replace("|", "/")[:80]
    date = c["commit"]["author"]["date"][:10]
    sha = c["sha"][:7]
    rows.append(f"| `{date}` | [`{sha}`]({c['html_url']}) | {msg} |")

block = "| Date | Commit | What changed |\n|---|---|---|\n" + "\n".join(rows)

text = open("README.md", encoding="utf-8").read()
new = re.sub(r"<!--START_COMMITS-->.*?<!--END_COMMITS-->",
             f"<!--START_COMMITS-->\n{block}\n<!--END_COMMITS-->", text, flags=re.S)
if new != text:
    open("README.md", "w", encoding="utf-8").write(new)
