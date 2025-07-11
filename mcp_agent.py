import os
import requests

def show_erbu():
    try:
        with open("ascii_erb.txt", "r", encoding="utf-8") as f:
            print(f.read())
    except:
        print("🕯️ Erb není k dispozici.")

def audit_repo():
    token = os.getenv("GH_PAT")
    headers = {
        "Authorization": f"Bearer {token}",
        "Accept": "application/vnd.github+json"
    }

    repo = "osAplet/agent_mpc_me-ai"
    print(f"📘 Repozitář: {repo}")

    workflows_url = f"https://api.github.com/repos/{repo}/actions/workflows"
    r = requests.get(workflows_url, headers=headers)
    workflows = r.json().get("workflows", [])
    print("⚙️ Workflows:")
    for wf in workflows:
        print(f"   - {wf.get('name')}")

    issues_url = f"https://api.github.com/repos/{repo}/issues"
    r = requests.get(issues_url, headers=headers)
    issues = r.json()
    print("📝 Issues:")
    for issue in issues:
        print(f"   - {issue.get('title')}")

if __name__ == "__main__":
    show_erbu()
    audit_repo()
