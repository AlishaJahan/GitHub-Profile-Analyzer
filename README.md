# GitHub-Profile-Analyzer

A simple Python tool that fetches public repositories of any GitHub user and analyzes:

- Languages used
- Push activity by hour (UTC)

## 📊 Output

- `language_usage.png`: Bar graph of languages used across repositories
- `push_activity.png`: Line graph showing commit activity by hour

## 🔧 Features

- Uses GitHub's public REST API
- Generates visual insights
- Requires no authentication (rate-limited)

## Setup

1. Clone the Repository
   
```bash
git clone https://github.com/AlishaJahan/github-profile-analyzer.git
cd github-profile-analyzer
```
2. Install Dependencies
   
pip install requests matplotlib

3. Run the Script
   
python github_profile_analyzer.py
