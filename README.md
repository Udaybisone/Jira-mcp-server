# Jira MCP Server

A local MCP (Model Context Protocol) server that integrates with Jira Cloud and allows LLMs (e.g., Claude Desktop) to create, update, assign, and transition Jira tickets.

---

## 🚀 Features

- Create Jira tickets
- Get Jira ticket details
- Add comments to tickets
- Assign tickets by user name (future integration) 
- Change ticket status (future integratioin)
- Fully compatible with Claude Desktop (Local MCP)

---

## 🏗 Architecture
```
┌─────────────────┐
│ Claude Desktop  │
└────────┬────────┘
         │ (Model Context Protocol)
         ▼
┌───────────────────────┐
│ MCP Server (FastMCP)  │
└────────┬──────────────┘
         │
         ▼
┌──────────────────┐
│  jira_client.py  │
└────────┬─────────┘
         │ (REST API)
         ▼
┌──────────────────────┐
│  Jira Cloud API      │
└──────────────────────┘
```
---
## 📦 Requirements

- Python 3.10+
- Jira Cloud account
- Jira API token

---
## 🔐 Generate Jira API Token

1. Go to:
   https://id.atlassian.com/manage-profile/security/api-tokens
2. Click **Create API token**
3. Copy the generated token

---
## ⚙️ Setup
### 1️⃣ Clone the Repository
Open your terminal and run:
```bash
git clone https://github.com/Udaybisone/Jira-mcp-server
cd jira-mcp-server
```
### 2️⃣ Install Dependencies
```bash
# Install uv if you haven't already
brew install uv

# Sync the project environment
uv sync
```
### 3️⃣ Configure Environment Variables
```bash
# Create a .env file:
JIRA_BASE_URL=https://your-domain.atlassian.net
JIRA_EMAIL=your-email@example.com
JIRA_API_TOKEN=your-api-token
```
## ▶ Running the Server (Using uv)
```bash
uv run python main.py
```
## 🔗 Connect to Claude Desktop
```bash
# Edit:
~/Library/Application Support/Claude/claude_desktop_config.json
# add :
{
  "mcpServers": {
    "jira": {
      "command": "<output-of-which-uv>",
      "args": [
        "run",
        "python",
        "</full/path/to/main.py>"
      ]
    }
  }
}
```
