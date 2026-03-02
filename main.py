from fastmcp import FastMCP
from jira_client import create_issue, get_issue, add_comment
import json

mcp = FastMCP("jira-mcp-server")


@mcp.tool()
def create_jira_ticket(project_key: str, summary: str, description: str) -> str:
    try:
        issue = create_issue(project_key, summary, description)
        return f"Ticket created: {issue['key']}"
    except Exception as e:
        return f"Error: {str(e)}"


@mcp.tool()
def get_jira_ticket(issue_key: str) -> str:
    try:
        issue = get_issue(issue_key)
        return json.dumps(issue, indent=2)
    except Exception as e:
        return f"Error: {str(e)}"


@mcp.tool()
def add_jira_comment(issue_key: str, comment: str) -> str:
    try:
        add_comment(issue_key, comment)
        return "Comment added successfully."
    except Exception as e:
        return f"Error: {str(e)}"


if __name__ == "__main__":
    mcp.run()