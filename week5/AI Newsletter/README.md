# 📰 AI Auto Newsletter (n8n → OpenAI → Slack)

An automated AI news intelligence pipeline that generates a premium executive-style AI newsletter and delivers it directly to Slack.

Built using **n8n**, **OpenAI**, and **Slack API**.

---

## 🚀 Overview

This workflow automatically:

1. Triggers on a schedule  
2. Uses an LLM to identify the top 3 verified AI developments from the last 7 days  
3. Formats the output as a structured executive newsletter  
4. Sends it directly to a Slack channel  

No manual research. No copy-paste. Fully automated intelligence delivery.

---

## 🏗 Architecture

```
Schedule Trigger
        ↓
OpenAI (LLM Content Generation)
        ↓
JavaScript Formatter Node
        ↓
Slack Message Node
```

---

## ⚙️ Tech Stack

- **n8n** – Workflow automation engine  
- **OpenAI GPT-4.1-mini** – AI content generation  
- **Slack API** – Newsletter distribution  
- **JavaScript (n8n Code Node)** – Custom message formatting  

---

## 🧠 Prompt Design

The model is instructed to:

- Act as a Senior AI News Editor  
- Identify the 3 most important AI developments from the last 7 days  
- Avoid hype and speculation  
- Focus on business impact and technical relevance  

For each story, it generates:

- A compelling headline (≤ 12 words)
- 120–150 word strategic analysis
- TL;DR summary (< 25 words)

Output format is strictly structured for consistent delivery.

---

## 📦 Workflow Breakdown

### 1️⃣ Schedule Trigger
- Configurable interval (minutes/hours/days)
- Automatically starts the workflow

### 2️⃣ OpenAI Node
- Model: `gpt-4.1-mini`
- Temperature: `0.7`
- Structured system prompt
- Returns formatted newsletter content

### 3️⃣ JavaScript Formatter

Adds branding and formatting:

```javascript
const item = $input.first();
const content = item.json?.output?.[0]?.content?.[0]?.text || "No content generated.";

const formattedMessage = `
*📰 AI INSIDER DAILY*
_Your automated AI intelligence brief_

${content}

---
🤖 Automated via n8n AI Workflow
`;

return [
  {
    json: {
      message: formattedMessage
    }
  }
];
```

### 4️⃣ Slack Node
- Sends formatted message
- Posts directly to configured Slack channel

---

## 🔐 Required Credentials

- OpenAI API Key  
- Slack Bot Token (with `chat:write` permission)

---

## 📊 Example Output Structure

```
🚀 AI Insider: The Top 3

━━━━━━━━━━━━━━━━━━

1. [Headline]

The Full Story:
<analysis>

The Short Version:
⚡ <TL;DR>

━━━━━━━━━━━━━━━━━━
```

## 💡 Use Cases

- AI-focused Slack communities  
- Executive intelligence briefings  
- Internal innovation teams  
- VC / startup monitoring  
- Tech leadership insights  

---

## 🧩 Why This Matters

This workflow turns AI from a writing tool into an autonomous intelligence system.

Instead of manually scanning headlines, the system:

- Synthesizes signal  
- Applies editorial structure  
- Delivers insight automatically  

From dashboards → to decision pipelines.

---

## 👤 Author

**Prabu Deivendran**  
Senior Technical Lead | BI & AI Engineering  
Expertise: AI Automation, Tableau, SQL, Python, Snowflake, Databricks, Automation
