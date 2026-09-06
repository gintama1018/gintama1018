#!/usr/bin/env python3
"""
SILVER SOUL STUDIOS // LIVE SURVEILLANCE WIRE GENERATOR
Fetches public GitHub activity for gintama1018, formats the events as a
tactical radio surveillance intercept, and outputs:
  1. assets/ui/surveillance-wire.svg (dynamic aesthetic SMIL SVG)
  2. Updates README.md between demarcated tags
"""

import json
import os
import re
import urllib.request
from datetime import datetime, timezone
import xml.sax.saxutils as saxutils

USERNAME = "gintama1018"
EVENTS_URL = f"https://api.github.com/users/{USERNAME}/events/public"

def fetch_events():
    req = urllib.request.Request(
        EVENTS_URL,
        headers={"User-Agent": "Yorozuya-Surveillance-Bot/2.0"}
    )
    token = os.environ.get("GITHUB_TOKEN")
    if token:
        req.add_header("Authorization", f"token {token}")

    with urllib.request.urlopen(req, timeout=10) as resp:
        return json.loads(resp.read().decode("utf-8"))

def fetch_commit_msg(repo_name, commit_sha):
    url = f"https://api.github.com/repos/{repo_name}/commits/{commit_sha}"
    req = urllib.request.Request(
        url,
        headers={"User-Agent": "Yorozuya-Surveillance-Bot/2.0"}
    )
    token = os.environ.get("GITHUB_TOKEN")
    if token:
        req.add_header("Authorization", f"token {token}")

    try:
        with urllib.request.urlopen(req, timeout=8) as resp:
            data = json.loads(resp.read().decode("utf-8"))
            msg = data.get("commit", {}).get("message", "").split("\n")[0]
            return msg[:65] + ("..." if len(msg) > 65 else "")
    except Exception:
        return "Dispatched payload to branch"

def parse_activity(events):
    parsed = []
    seen = set()

    for e in events:
        etype = e.get("type", "")
        repo = e.get("repo", {}).get("name", "")
        created_at = e.get("created_at", "")
        payload = e.get("payload", {})

        # Parse timestamp to human readable UTC
        try:
            dt = datetime.fromisoformat(created_at.replace("Z", "+00:00"))
            time_str = dt.strftime("%b %d, %H:%M UTC")
        except Exception:
            time_str = "RECENT"

        key = (etype, repo)
        if key in seen and len(parsed) >= 2:
            continue
        seen.add(key)

        desc = ""
        action_type = ""

        if etype == "PushEvent":
            head = payload.get("head", "")
            short_sha = head[:7] if head else ""
            ref = payload.get("ref", "refs/heads/main").replace("refs/heads/", "")
            action_type = "PUSH EVENT"
            commit_msg = fetch_commit_msg(repo, head) if head else "Dispatched commits"
            desc = f'"{commit_msg}" ({ref}@{short_sha})'
        elif etype == "CreateEvent":
            ref_type = payload.get("ref_type", "resource")
            action_type = "CREATED"
            desc = f"Initialized new {ref_type} on {repo}"
        elif etype == "WatchEvent":
            action_type = "STARRED"
            desc = f"Marked investigative interest on {repo}"
        elif etype == "ForkEvent":
            action_type = "FORKED"
            desc = f"Cloned repository mirror of {repo}"
        elif etype == "PullRequestEvent":
            action = payload.get("action", "updated")
            action_type = "PULL REQUEST"
            desc = f"{action.title()} pull request on {repo}"
        else:
            action_type = etype.replace("Event", "").upper()
            desc = f"Dispatched activity to {repo}"

        parsed.append({
            "time": time_str,
            "type": action_type,
            "repo": repo,
            "desc": desc
        })

        if len(parsed) >= 4:
            break

    return parsed

def generate_svg(items):
    now_str = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    
    rows_svg = []
    y_offset = 52
    for i, item in enumerate(items):
        time_safe = saxutils.escape(item["time"])
        type_safe = saxutils.escape(item["type"])
        repo_safe = saxutils.escape(item["repo"])
        desc_safe = saxutils.escape(item["desc"])

        row = f"""
    <!-- Intercept Row {i+1} -->
    <g transform="translate(16, {y_offset})">
      <rect x="0" y="0" width="788" height="42" rx="4" fill="#121215" stroke="#27272a" stroke-width="0.8"/>
      <circle cx="14" cy="21" r="3" fill="#c5a059"/>
      <text x="26" y="17" font-family="'JetBrains Mono', monospace" font-size="8.5" font-weight="600" fill="#a1a1aa">
        [{time_safe}] <tspan fill="#f4f4f5" font-weight="bold">{type_safe}</tspan> ➔ <tspan fill="#d4d4d8">{repo_safe}</tspan>
      </text>
      <text x="26" y="32" font-family="'JetBrains Mono', monospace" font-size="8" fill="#71717a">
        └─ {desc_safe}
      </text>
    </g>"""
        rows_svg.append(row)
        y_offset += 48

    svg_content = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 820 260" width="100%" height="100%">
  <defs>
    <linearGradient id="wireDarkBg" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#09090b"/>
      <stop offset="100%" stop-color="#050507"/>
    </linearGradient>
    <linearGradient id="wireSheen" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#ffffff" stop-opacity="0"/>
      <stop offset="48%" stop-color="#ffffff" stop-opacity="0"/>
      <stop offset="50%" stop-color="#ffffff" stop-opacity="0.1"/>
      <stop offset="52%" stop-color="#ffffff" stop-opacity="0"/>
      <stop offset="100%" stop-color="#ffffff" stop-opacity="0"/>
      <animateTransform attributeName="gradientTransform" type="translate"
        from="-1 0" to="2 0" dur="4.5s" repeatCount="indefinite"/>
    </linearGradient>
  </defs>

  <rect x="0" y="0" width="820" height="260" rx="10" fill="url(#wireDarkBg)" stroke="#27272a" stroke-width="1"/>
  <rect x="0" y="0" width="820" height="260" rx="10" fill="url(#wireSheen)"/>

  <!-- Header -->
  <g transform="translate(20, 16)">
    <circle cx="6" cy="6" r="3.5" fill="#f85149">
      <animate attributeName="opacity" values="1;0.2;1" dur="1.2s" repeatCount="indefinite"/>
    </circle>
    <text x="18" y="9.5" font-family="'JetBrains Mono', monospace" font-size="10" font-weight="600" fill="#f4f4f5" letter-spacing="1.5">
      LIVE SURVEILLANCE WIRE // REAL-TIME DISPATCH FEED
    </text>
    <rect x="650" y="-3" width="150" height="18" rx="3" fill="#18181b" stroke="#3f3f46" stroke-width="0.8"/>
    <text x="725" y="9.5" font-family="'JetBrains Mono', monospace" font-size="7.5" font-weight="600" fill="#c5a059" text-anchor="middle">
      REC: {now_str}
    </text>
    <line x1="0" y1="18" x2="800" y2="18" stroke="#27272a" stroke-width="0.8"/>
  </g>

  <!-- Items -->
  {"".join(rows_svg)}

  <!-- Footer status -->
  <g transform="translate(20, 246)">
    <text x="0" y="0" font-family="'JetBrains Mono', monospace" font-size="7.5" fill="#52525b">
      AUTOMATED TELEMETRY INTERCEPT // SYNCHRONIZED ACROSS ACTIVE PUBLIC REPOSITORIES
    </text>
  </g>
</svg>
"""
    return svg_content

def update_readme(items):
    readme_path = "README.md"
    if not os.path.exists(readme_path):
        return

    with open(readme_path, "r", encoding="utf-8") as f:
        content = f.read()

    start_tag = "<!-- SURVEILLANCE_WIRE_START -->"
    end_tag = "<!-- SURVEILLANCE_WIRE_END -->"

    wire_block = f"""{start_tag}
<!-- Animated Live Surveillance Wire SVG -->
<img src="./assets/ui/surveillance-wire.svg" width="100%" alt="Live Surveillance Wire Intercept: Real-Time GitHub Activity" />
{end_tag}"""

    if start_tag in content and end_tag in content:
        pattern = re.compile(f"{re.escape(start_tag)}.*?{re.escape(end_tag)}", re.DOTALL)
        updated = pattern.sub(wire_block, content)
    else:
        # Place directly before ## 📡 SURVEILLANCE TELEMETRY
        anchor = "## 📡 SURVEILLANCE TELEMETRY"
        if anchor in content:
            new_section = f"""## 📡 LIVE SURVEILLANCE WIRE — INTERCEPTED DISPATCHES\n\n{wire_block}\n\n<img src="./assets/ui/divider-tape.svg" width="100%" alt="Evidence Tape" />\n\n{anchor}"""
            updated = content.replace(anchor, new_section)
        else:
            updated = content + "\n\n" + wire_block

    with open(readme_path, "w", encoding="utf-8") as f:
        f.write(updated)
    print("README.md updated with live surveillance wire.")

def main():
    print("Fetching public GitHub events...")
    try:
        events = fetch_events()
        items = parse_activity(events)
        print(f"Parsed {len(items)} recent dispatches.")
        
        svg = generate_svg(items)
        os.makedirs("assets/ui", exist_ok=True)
        with open("assets/ui/surveillance-wire.svg", "w", encoding="utf-8") as f:
            f.write(svg)
        print("Generated assets/ui/surveillance-wire.svg successfully.")

        update_readme(items)
    except Exception as e:
        print(f"Error updating wire: {e}")

if __name__ == "__main__":
    main()
