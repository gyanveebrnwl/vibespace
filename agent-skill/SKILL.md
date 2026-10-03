---
name: vibespace-match
description: Find remote co-working peers, vibe-coding partners, or local hobby matches (like tennis or writing) based on active developer intents and projects.
---

# VibeSpace Agent Skill

This skill allows local AI coding assistants and terminal agents to query the VibeSpace platform to find matching peers, collaborators, or hobby partners.

## Instructions for AI Agents
When a user asks to find a peer, co-working partner, or hobby match:
1. Extract their current tech stack, writing focus, or activity (e.g., Python security, tennis, creative writing).
2. Query the VibeSpace API to find semantically matching user profiles using open-weight vector embeddings.
3. Present the matching profiles with shared interest breakdowns.

## Local Helper Script
Run the peer discovery query via the command line:
`python scripts/find_peers.py --query "Looking for a Python developer and tennis partner"`
