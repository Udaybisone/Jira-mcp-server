import os
import requests
from dotenv import load_dotenv

load_dotenv()

BASE_URL = os.getenv("JIRA_BASE_URL")
AUTH = (os.getenv("JIRA_EMAIL"), os.getenv("JIRA_API_TOKEN"))

HEADERS = {
    "Accept": "application/json",
    "Content-Type": "application/json"
}


def create_issue(project_key: str, summary: str, description: str):
    url = f"{BASE_URL}/rest/api/3/issue"

    payload = {
        "fields": {
            "project": {"key": project_key},
            "summary": summary,
            "description": {
                "type": "doc",
                "version": 1,
                "content": [
                    {
                        "type": "paragraph",
                        "content": [{"type": "text", "text": description}]
                    }
                ]
            },
            "issuetype": {"name": "Task"}
        }
    }

    response = requests.post(url, json=payload, headers=HEADERS, auth=AUTH)
    response.raise_for_status()
    return response.json()


def get_issue(issue_key: str):
    url = f"{BASE_URL}/rest/api/3/issue/{issue_key}"
    response = requests.get(url, headers=HEADERS, auth=AUTH)
    response.raise_for_status()
    return response.json()


def add_comment(issue_key: str, comment: str):
    url = f"{BASE_URL}/rest/api/3/issue/{issue_key}/comment"

    payload = {
        "body": {
            "type": "doc",
            "version": 1,
            "content": [
                {
                    "type": "paragraph",
                    "content": [{"type": "text", "text": comment}]
                }
            ]
        }
    }

    response = requests.post(url, json=payload, headers=HEADERS, auth=AUTH)
    response.raise_for_status()
    return response.json()