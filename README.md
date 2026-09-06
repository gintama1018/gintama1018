<!--
  BEFORE YOU COMMIT:
  1. Drop the assets/ folder (from this delivery) into the repo root, next to this README.
  2. Replace remaining [PLACEHOLDER] repo links: INFRAWATCH_REPO, BHARATKART_REPO,
     ROADSOS_REPO, KISANAI_REPO.
  3. Replace [YOUR_EMAIL] / [YOUR_LINKEDIN] / [YOUR_X], or delete those rows.
  4. If you want the external mini-game live, host case-terminal-game.html on
     gintama.tech or GitHub Pages and swap the placeholder link in FILE 07.
  5. After committing, actually open the README on github.com and on the mobile
     app — confirm the animated SVGs render. If GitHub ever changes how it
     serves repo-relative SVGs, the images still degrade to a static frame,
     nothing breaks.

  DESIGN TOKENS (for future-you, editing this in six months):
    palette   — bg #0d0d0d / panel #141414 / line #2b2b2b / silver #C0C0C0 / gold #D4AF37 (awards only)
    type      — JetBrains Mono throughout, via readme-typing-svg + inline SVG assets
    status    — 🟢 active  🟡 submitted  🏆 awarded  🔵 live  ⚪ cold case  🔴 archived/closed
    structure — everything is a "FILE ##", every project is a "CASE", never break that vocabulary
-->

<div align="center">
<img src="./assets/hero/case-stamp.svg" width="700" alt="Case file stamped OPEN — Silver Soul Studios subject file" />

<br/><br/>

<img src="https://readme-typing-svg.demolab.com?font=JetBrains+Mono&size=20&pause=1400&color=C0C0C0&center=true&vCenter=true&width=680&lines=Every+bug+is+a+cold+case+until+someone+reads+the+logs.;I+don't+specialize+in+a+stack.+I+specialize+in+finding+what's+broken.;Currently+investigating%3A+one+mesh+network%2C+one+sleep+schedule." alt="tagline" />
</div>

<p align="center">
  <a href="https://gintama.tech"><img src="https://img.shields.io/badge/PORTFOLIO-gintama.tech-1c1c1c?style=for-the-badge&logoColor=C0C0C0" /></a>
  <a href="https://github.com/gintama1018"><img src="https://img.shields.io/badge/GITHUB-gintama1018-1c1c1c?style=for-the-badge&logo=github&logoColor=C0C0C0" /></a>
  <img src="https://img.shields.io/badge/STATUS-accepting%20new%20cases-2b2b2b?style=for-the-badge&logoColor=C0C0C0" />
</p>

<img src="./assets/ui/divider-tape.svg" width="100%" alt="" />

## FILE 00 — SUBJECT

```
NAME             Sonu Jangir  (operates as GINTAMA)
AGENCY           Silver Soul Studios (self-run, one-person shop)
STANDING         Final-year BCA, UEM Jaipur — class of 2027
LAST KNOWN BASE  Kaladera → Jaipur, Rajasthan
SPECIALTIES      full-stack · AI/ML integration · cryptography · BLE/mesh
                 networking · automation (n8n) · the occasional game
KNOWN FOR        shipping first, then auditing it like it's someone else's
                 code — most of what's below started as a working demo
                 and got hardened after
```

Off the record: bleeds red and gold for RCB, hoards diecast cars the way
most people hoard tech debt, and yes — "Gintama" is the studio name
because "Yorozuya" (万事屋, "the shop that does everything") is a more
honest job title than anything you'd put on a resume.

<img src="./assets/ui/divider-tape.svg" width="100%" alt="" />

## CASE BOARD — index of everything below

| # | Case | Status | One line |
|---|------|--------|----------|
| 01 | [MeshWhisper](#file-01--meshwhisper) | 🟢 ACTIVE | Encrypted chat for zero signal, zero towers |
| 02 | [InfraWatch Nexus](#file-02--infrawatch-nexus) | 🏆 AWARDED | AI monitoring across 106 real Delhi sanitation points |
| 03 | [AI Teacher — Bharat Academix](#file-03--ai-teacher--bharat-academix) | 🟡 SUBMITTED | An AI that writes and narrates its own lessons |
| 04 | [KISAN-AI](#file-04--kisan-ai) | 🔵 LIVE | Satellite intelligence for farm decisions |
| 05 | [BharatKart](#file-05--bharatkart) | 🏆 AWARDED | Voice-first listings for artisans who won't type |
| 06 | [ROADSoS](#file-06--roadsos) | ⚪ BUILT | Offline-first emergency response, 12+ countries |

<img src="./assets/ui/divider-tape.svg" width="100%" alt="" />

## FILE 01 — MeshWhisper

**🟢 STATUS: ACTIVE** — open case, currently exploring multi-hop mesh topology

Android BLE mesh chat for when there's no signal and no towers. Every
relay in the mesh forwards encrypted packets it cannot read.

<p align="center"><img src="./assets/cases/meshwhisper-diagram.svg" width="640" alt="MeshWhisper BLE mesh routing diagram" /></p>

- **Crypto:** X25519 key agreement, AES-256-GCM with AAD, Ed25519 signing, SQLCipher at rest
- **Routing:** TTL flood routing, chunked media transfer with ACK/NACK + SHA-256 verification
- **Field test:** working through a wall at ~20m with no perceptible delay
- **Notable evidence:** this one's been through two full rounds of adversarial
  auditing since the first demo — background BLE scanning that never stopped
  on app close, unauthenticated ACK packets, a stale-timestamp bug that was
  quietly tripping anti-replay protection. None of that shows up in a demo.
  It shows up when someone tries to break it.

**Open on the desk right now:**
- [ ] Minification pass
- [ ] SQLCipher passphrase rotation on wipe
- [ ] Multi-hop BLE mesh topology (in progress)

[Repo →](https://github.com/gintama1018/BIT-FOR-US)

<br/>

## FILE 02 — InfraWatch Nexus

**🏆 STATUS: AWARDED** — Best Paper, ICAHTE-2026 (Paper ID: AHTE_26_R_101)

Real-time AI monitoring across 106 real Municipal Corporation of Delhi
sanitation collection points. QR-coded bins act as Civic Reference Nodes;
Gemini scores each report for contextual priority.

- **Stack:** Gemini for priority scoring, Pathway for streaming, ElevenLabs
  for Hindi TTS alerts, Leaflet + OSRM for live routing/mapping
- **Notable evidence:** the paper award is on file — a production-hardened
  deployment is a separate, later bar, and this case stays open until that's
  also true

[Repo →][INFRAWATCH_REPO]

<br/>

## FILE 03 — AI Teacher — Bharat Academix

**🟡 STATUS: SUBMITTED** — Round 2, AI Innovation Hackathon 2026

An AI teacher that generates its own lessons end to end: retrieves context,
writes the lesson, and synthesizes a narrated video with an on-screen avatar.

- **Stack:** Next.js/TypeScript frontend, FastAPI + SQLAlchemy backend,
  ChromaDB for retrieval, dual-LLM routing (Claude + Gemini)
- **Output:** auto-synthesized 720p video lessons with an SVG avatar

[Repo →](https://github.com/gintama1018/ML-HACKATHON-2-LEVEL-ASSIGNMENT)

<br/>

## FILE 04 — KISAN-AI

**🔵 STATUS: LIVE**

Live satellite-based agricultural intelligence — because yield decisions
shouldn't run on gut feeling.

[Live demo →](https://kisan-ai-b2lz.onrender.com) · [Repo →][KISANAI_REPO]

<br/>

## FILE 05 — BharatKart

**🏆 STATUS: AWARDED** — HackUEM Winner

Voice-first marketplace listings for artisans who can't or won't type a
product description.

[Repo →][BHARATKART_REPO]

<br/>

## FILE 06 — ROADSoS

**⚪ STATUS: BUILT**

Offline-first emergency response web app with full offline fallback, built
to hold up across 12+ countries.

[Repo →][ROADSOS_REPO]

<img src="./assets/ui/divider-tape.svg" width="100%" alt="" />

<details>
<summary><b>COLD CASES — smaller jobs, still on file</b></summary>
<br/>

| Case | What it was |
|---|---|
| **CarbonPulse** | Carbon-tracking app, Google PromptWars Challenge 2 (Hack2Skill) — AIR 15 of ~30,000 |
| **ThunderCipher CTF** | 3rd place — cracked an ROCA-vulnerable RSA key and recovered a ransomware's PRNG key |
| **Fugacity 2026 (ML)** | Physics-informed stacking ensemble for chemical reactor yield prediction, ~RMSE 17.93 |
| **The Coiled Snake: A Debt in Blood** | HTML5 canvas 2D game, Silver Soul Studios |
| **Elementia** | Gesture-controlled elemental-powers game, Python/Pygame |
| **Reality Cursor** | Computer-vision gesture system, ArUco + MediaPipe |
| **AV Events** | Production web platform, 6 pages, Lighthouse 90+, page-load latency down 35% |
| **DFAP** | Concept blueprint for a govt-grade digital-footprint analytics platform |
| **"The Modern Rat Riddler Theory"** | Behavioral-economics paper — [DOI: 10.5281/zenodo.20966562](https://doi.org/10.5281/zenodo.20966562) |

</details>

<img src="./assets/ui/divider-tape.svg" width="100%" alt="" />

## FILE 07 — EVIDENCE LOCKER (things I do because I'm curious, not because a client asked)

```
[LOCKER 07-A]  ROCA RSA cryptanalysis — ThunderCipher CTF
               STATUS: SOLVED (3rd place)
               Cracked an ROCA-vulnerable RSA key, recovered a
               ransomware's PRNG seed from it.

[LOCKER 07-B]  Custom VM bytecode reversal
               STATUS: SOLVED
               Static analysis + brute-force per-byte chain reversal
               against a bytecode VM with no public spec.

[LOCKER 07-C]  Multi-layer covert-channel forensics
               STATUS: WORKED, "insane" difficulty rating
               A pcap hiding data across DNS, ICMP, ARP, TCP URG,
               UDP TTL, and a custom GOB binary protocol, stacked.

[LOCKER 07-D]  8x8 LED matrix animation/face engine — Arduino
               STATUS: SHIPPED
               MAX7219 + LedControl, PROGMEM bitmap storage, a
               column-transpose rendering bug that took longer to
               find than to fix.
```

Play the game if you want to see how one of these actually goes down →
[**Open the Case Terminal**](https://gintama1018.github.io/case-terminal-game.html)
*(a small standalone page — nothing here executes inside GitHub, obviously)*

<img src="./assets/ui/divider-tape.svg" width="100%" alt="" />

## FILE 08 — ISSUED EQUIPMENT

```
LANGUAGES        Python · JavaScript / TypeScript · Java

AI / ML          Gemini API · Claude API · ChromaDB (RAG) ·
                 physics-informed ensemble modeling · Pathway (streaming)

WEB              Next.js · FastAPI · SQLAlchemy · Tailwind CSS

MOBILE & SYSTEMS Android (native, BLE mesh) · Rust (P2P encrypted
                 messaging — MeshNet)

SECURITY         X25519 · AES-256-GCM · SQLCipher · RSA cryptanalysis
                 (ROCA) · applied CTF forensics

DATA & INFRA     SQLite · OSRM + Leaflet · ffmpeg / PIL pipelines

SIDE ARMS        Pygame · HTML5 Canvas
```

<img src="./assets/ui/divider-tape.svg" width="100%" alt="" />

## CASE LOAD — right now

Not a KPI. Not a burndown chart. Just where my attention actually is.

```
MeshWhisper hardening      ●●●●○○○  "still testing, mostly"
Multi-hop mesh research    ●●○○○○○  "reading more than building"
Sleep schedule             ○○○○○○○  "case closed, badly"
```

<img src="./assets/ui/divider-tape.svg" width="100%" alt="" />

## SURVEILLANCE LOG

<div align="center">
<img src="https://github-stats-extended.vercel.app/api?username=gintama1018&show_icons=true&theme=github_dark&bg_color=0d1117&title_color=C0C0C0&text_color=E5E5E5&icon_color=C0C0C0&border_color=2b2b2b&hide_border=true" alt="stats" height="165"/>
<img src="https://streak-stats.demolab.com/?user=gintama1018&theme=dark&background=0D1117&stroke=2b2b2b&ring=C0C0C0&fire=C0C0C0&currStreakLabel=C0C0C0&sideLabels=E5E5E5&sideNums=E5E5E5&dates=8b8b8b&hide_border=true" alt="streak" height="165"/>
<img src="https://github-stats-extended.vercel.app/api/top-langs/?username=gintama1018&layout=compact&theme=github_dark&bg_color=0d1117&title_color=C0C0C0&text_color=E5E5E5&border_color=2b2b2b&hide_border=true" alt="top langs" height="165"/>
</div>

<br/>

<div align="center">
<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/gintama1018/gintama1018/output/github-contribution-grid-snake-dark.svg" />
  <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/gintama1018/gintama1018/output/github-contribution-grid-snake.svg" />
  <img alt="github contribution grid snake" src="https://raw.githubusercontent.com/gintama1018/gintama1018/output/github-contribution-grid-snake.svg" width="100%" />
</picture>
</div>

*(these are community-hosted cards & automated activity feeds — if one's down, the case board above
still tells the real story)*

<img src="./assets/ui/divider-tape.svg" width="100%" alt="" />

<details>
<summary><b>🔒 REDACTED — FILE ACCESS RESTRICTED (click if you're the type to click this)</b></summary>
<br/>

```
[REDACTED] joined a hackathon once, got disqualified over a Git blob
flag. Root cause, after actually investigating instead of complaining:
a Replit Agent commit's authorship was sitting right there in git log.
Filed under: read the logs before you argue with the judges.
```

</details>

<details>
<summary><b>⌨️ TERMINAL ACCESS — run a diagnostic?</b></summary>
<br/>

```
$ ./diagnostic.sh --deep

> checking open-case queue.............. [6 OPEN]
> checking claimed-vs-shipped ratio...... [MATCHED]
> checking RCB win probability........... [ERROR: DIVISION BY ZERO]
> checking sleep schedule................ [CRITICAL — see CASE LOAD above]

DIAGNOSTIC COMPLETE. one note survived the log wipe:

  "most bugs aren't clever. they're just unread logs."
  — case notes, filed under FILE 07
```

</details>

<img src="./assets/ui/divider-tape.svg" width="100%" alt="" />

## CONTACT THE AGENCY

<p align="center">
  <a href="https://gintama.tech"><img src="https://img.shields.io/badge/Portfolio-gintama.tech-1c1c1c?style=flat-square&logoColor=C0C0C0" /></a>
  <a href="https://github.com/gintama1018"><img src="https://img.shields.io/badge/GitHub-gintama1018-1c1c1c?style=flat-square&logo=github&logoColor=C0C0C0" /></a>
  <a href="mailto:pihujang0@gmail.com"><img src="https://img.shields.io/badge/Email-contact-1c1c1c?style=flat-square&logoColor=C0C0C0" /></a>
  <a href="https://linkedin.com/in/sonu-jangir-98968b390"><img src="https://img.shields.io/badge/LinkedIn-connect-1c1c1c?style=flat-square&logo=linkedin&logoColor=C0C0C0" /></a>
</p>

<div align="center">

```
$ ./yorozuya --status

> case queue     : not empty. never will be.
> accepting      : real problems only.
> payment method : interesting bugs.

$ _
```

</div>

[INFRAWATCH_REPO]: https://github.com/gintama1018/HACK-FOR-GREEN-BHARAT-HACKATHON
[BHARATKART_REPO]: https://github.com/gintama1018/BHARAT-KART---AUTONOMOUS-HACKS-FINALE-PROJECT
[ROADSOS_REPO]: https://github.com/gintama1018/ROAD-SAFETY-PROJECT
[KISANAI_REPO]: https://github.com/gintama1018/KISAN-AI
