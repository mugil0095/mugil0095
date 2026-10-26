"""Refreshes the 'Recent Activity' table in README.md and .github/stats.svg from the owner's public repos (stdlib only)."""
import json
import os
import re
import urllib.request
from collections import Counter
from datetime import datetime, timezone

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


def write_stats(user, repos):
    """Self-hosted stats card (no third-party service): four tiles plus a language bar on a dark panel."""
    own = [r for r in repos if not r["fork"] and not r["private"] and r["name"].lower() != USER.lower()]
    year = datetime.now(timezone.utc).year
    langs = Counter(r["language"] for r in own if r["language"])
    total = sum(langs.values()) or 1
    top, top_n = langs.most_common(1)[0] if langs else ("-", 0)
    tiles = [
        (str(user["public_repos"]), "Public repos"),
        (str(sum(1 for r in own if r["created_at"][:4] == str(year))), f"Built in {year}"),
        (user["created_at"][:4], "On GitHub since"),
        (top, f"Top language · {round(100 * top_n / total)}% of repos"),
    ]
    palette = ["#7fe0c8", "#ffb86b", "#6fb8ff", "#ff7eb6", "#ffd866"]
    out = [
        '<svg width="900" height="226" viewBox="0 0 900 226" xmlns="http://www.w3.org/2000/svg" '
        "font-family=\"'Segoe UI', -apple-system, 'Helvetica Neue', Arial, sans-serif\">",
        '<defs><linearGradient id="bg" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#0b1626"/>'
        '<stop offset="1" stop-color="#12324a"/></linearGradient></defs>',
        '<rect x="1" y="1" width="898" height="224" rx="18" fill="#0A1311" stroke="rgba(255,255,255,0.12)"/>',
        '<g transform="translate(24,20)">',
        '<text x="0" y="12" font-size="10.5" font-family="Consolas, Menlo, monospace" fill="#7fe0c8" letter-spacing="3">LIVE FROM GITHUB</text>',
        '<circle cx="148" cy="8.5" r="3.5" fill="#7fe0c8"><animate attributeName="opacity" values="1;0.25;1" dur="2s" repeatCount="indefinite"/></circle>',
    ]
    for i, (big, label) in enumerate(tiles):
        x = i * 219
        out.append(
            f'<rect x="{x}" y="28" width="195" height="92" rx="16" fill="#101C19" stroke="rgba(255,255,255,0.12)"/>'
            f'<text x="{x+22}" y="78" font-size="30" font-weight="700" fill="#fff">{big}</text>'
            f'<text x="{x+22}" y="102" font-size="12" fill="#9fb8b2">{label}</text>'
        )
    x, legend = 0.0, []
    for i, (name, n) in enumerate(langs.most_common(5)):
        w = 852 * n / total
        out.append(f'<rect x="{x:.1f}" y="140" width="{max(w-3, 2):.1f}" height="10" rx="5" fill="{palette[i]}"/>')
        legend.append((name, round(100 * n / total), palette[i]))
        x += w
    lx = 0.0
    for name, pct, col in legend:
        out.append(f'<circle cx="{lx+5:.1f}" cy="172" r="5" fill="{col}"/><text x="{lx+16:.1f}" y="176" font-size="12.5" fill="#cfe3de">{name} {pct}%</text>')
        lx += 36 + 7.2 * len(f"{name} {pct}%")
    out.append("</g></svg>")
    with open(os.path.join(".github", "stats.svg"), "w", encoding="utf-8", newline="") as f:
        f.write("".join(out))


user = api(f"https://api.github.com/users/{USER}")
repos = api(f"https://api.github.com/users/{USER}/repos?sort=pushed&direction=desc&per_page=100&type=owner")
# repos without a description are skipped so the table stays presentable
rows = [
    r for r in repos
    if not r["fork"] and not r["archived"] and not r["private"] and r["description"] and r["name"].lower() != USER.lower()
][:5]

write_stats(user, repos)

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
