"""Refreshes the 'Recent Activity' table in README.md from the owner's public repos (stdlib only)."""
import json
import os
import re
import urllib.request
from datetime import datetime

USER = "mugil0095"
README = "README.md"
START, END = "<!--RECENT_ACTIVITY:START-->", "<!--RECENT_ACTIVITY:END-->"


def api(url):
    headers = {"Accept": "application/vnd.github+json"}
    if os.environ.get("GITHUB_TOKEN"):
        headers["Authorization"] = "Bearer " + os.environ["GITHUB_TOKEN"]
    with urllib.request.urlopen(urllib.request.Request(url, headers=headers), timeout=30) as r:
        return json.load(r)


def clip(text, n=95):
    text = " ".join((text or "").split()).replace("|", "/")
    text = re.split(r"\. |: | — ", text)[0].rstrip(".")  # first clause reads cleaner than a mid-sentence cut
    return text if len(text) <= n else text[: n - 1].rstrip() + "…"


repos = api(f"https://api.github.com/users/{USER}/repos?sort=pushed&direction=desc&per_page=30&type=owner")
# repos without a description are skipped so the table stays presentable
rows = [
    r for r in repos
    if not r["fork"] and not r["archived"] and not r["private"] and r["description"] and r["name"].lower() != USER.lower()
][:5]

lines = ["| Project | What it is | Updated |", "|---|---|---|"]
for r in rows:
    what = clip(r["description"])
    updated = datetime.strptime(r["pushed_at"], "%Y-%m-%dT%H:%M:%SZ").strftime("%b %d").replace(" 0", " ")
    lines.append(f"| [**{r['name']}**]({r['html_url']}) | {what} | {updated} |")
block = f"{START}\n" + "\n".join(lines) + f"\n{END}"

text = open(README, encoding="utf-8").read()
pattern = re.compile(re.escape(START) + r".*?" + re.escape(END), re.S)
assert pattern.search(text), "markers missing in README.md"
new = pattern.sub(lambda _: block, text)
if new != text:
    open(README, "w", encoding="utf-8", newline="").write(new)
    print("README updated")
else:
    print("no change")
