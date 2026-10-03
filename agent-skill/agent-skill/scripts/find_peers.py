#!/usr/bin/env python3
import argparse
import sys
import json

def main():
    parser = argparse.ArgumentParser(description="Find peers and collaborators on VibeSpace.")
    parser.add_argument("--query", type=str, required=True, help="Your current focus, tech stack, or hobby (e.g. Python, tennis, writing)")
    args = parser.parse_args()

    print(f"[*] Querying VibeSpace API for: '{args.query}'...")
    
    # Mocking sample response for hackathon demo demonstration
    mock_results = [
        {"name": "Peer A", "match": "94%", "interest": "Python Security & Tennis", "vibe": "Building low-level tools"},
        {"name": "Peer B", "match": "89%", "interest": "Creative Writing & Vibe Coding", "vibe": "Drafting sci-fi stories"}
    ]
    
    print("\n[+] Top Matching Peers Found:")
    print(json.dumps(mock_results, indent=2))

if __name__ == "__main__":
    main()
