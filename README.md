# VibeSpace 🌐🤖

> Connect with like-minded peers for vibe coding, creative writing, and hobbies like tennis using local open-weight AI matching and standardized Agent Skills.

---

## 🚀 Overview
**VibeSpace** is an open-source platform designed to bridge the gap between virtual collaboration and hyperlocal community building. Whether you are looking for a pair-programming partner for "vibe coding", someone to critique your creative writing, or a hitting partner for tennis, VibeSpace uses a privacy-first, open-weight AI engine to match you with compatible peers globally or locally.

---

## 🛠️ Project Structure

```text
vibespace/
├── agent-skill/          # Standard-compliant Agent Skill (Agent Skills Open Standard)
│   ├── SKILL.md          # Skill metadata & instructions for AI agents
│   └── scripts/          # Local peer-discovery execution scripts
├── backend/              # FastAPI server & open-weight vector embedding engine
│   ├── main.py           # Core FastAPI application & cosine similarity matching
│   └── requirements.txt  # Python dependency manifest
├── LICENSE               # Open-source MIT License
└── README.md             # Project documentation
