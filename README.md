# AgenticalDoctorAlliance

**Healthcare-focused AI Agent Dashboard & MCP Server**

This repository contains a Model-Context-Protocol (MCP) FastAPI server paired with a Streamlit dashboard, designed to orchestrate AI-driven healthcare workflows (appointment reminders, follow-up calls, billing updates). It integrates with:

* **Gemini/CrewAI** for AI response generation
* **SendGrid** (via Single Sender) for outbound email
* **Twilio** (Test or Live) for outbound SMS
* **Gmail API** for inbound email monitoring
* ** WebSocket** for real-time popup notifications

---
## Flowchart

![Editor _ Mermaid Chart-2025-06-17-154257](https://github.com/user-attachments/assets/4135881c-6657-4804-8a7e-38d31efcb378)


### Sequence Diagram

![Editor _ Mermaid Chart-2025-06-16-192336](https://github.com/user-attachments/assets/97732f1e-2f27-4dd1-97a2-7b310a729f37)

## Repository Structure

```
adrija-crewai-agent/
├── .env.example       # Template for environment variables
├── requirements.txt   # Python dependencies
└── src/
    └── doctoralliance_agent/
        ├── __init__.py
        ├── server.py         # FastAPI MCP endpoints
        ├── streamlit_app.py  # Streamlit UI
        ├── crew.py           # Optional CrewAI kickoff script
        ├── persona_resolver.py
        ├── data_fetcher.py
        ├── summary_builder.py
        ├── vault.py
        ├── agents/
        │   ├── __init__.py
        │   ├── prompt_builder.py
        │   └── gemini_agent.py
        ├── delivery/
        │   ├── __init__.py
        │   ├── channel_selector.py
        │   ├── email.py
        │   ├── sms_gateway.py
        │   ├── popup.py
        │   └── logger.py
        ├── escalation/
        │   ├── __init__.py
        │   ├── reminder_scheduler.py
        │   └── retry_agent.py
        └── gmail/
            ├── __init__.py
            ├── gmail_agent.py
            ├── nlp_parser.py
            └── response_handler.py
```

---

## Quickstart

### 1. Clone the repo

```bash
git clone https://github.com/your-org/adrija-crewai-agent.git
cd mcp-server-for-doctoralliance
```

### 2. Environment Variables

Copy `.env.example` to `.env` and fill in your credentials:

```bash
# Windows PowerShell
Copy-Item .env.example .env
# Linux/macOS
cp .env.example .env
```

Edit `.env`:

```dotenv
FASTAPI_HOST=0.0.0.0
FASTAPI_PORT=8000

# Gemini/CrewAI
GEMINI_API_KEY=sk-...

GEMINI_MODEL=gemini-2.0-flash-001


# SendGrid (Single Sender)
SENDGRID_API_KEY=SG-...
FROM_EMAIL=your_verified@domain.com

# Twilio (for SMS testing)
TWILIO_ACCOUNT_SID=AC...
TWILIO_AUTH_TOKEN=...
TWILIO_FROM_NUMBER=+15005550006

# Gmail (optional)
GMAIL_CREDENTIALS_PATH=./credentials.json

# WebSocket (optional)
WS_URL=ws://localhost:6789
```

Place your `credentials.json` (Gmail OAuth) next to `.env` if using inbound email.

### 3. Install Dependencies

```bash
python -m venv venv
# Windows
venv\Scripts\Activate.ps1
# macOS/Linux
source venv/bin/activate

pip install --upgrade pip
pip install -r requirements.txt
```

### 4. Run the MCP Server

```bash
uvicorn doctoralliance_agent.server:app \
  --reload --host $FASTAPI_HOST --port $FASTAPI_PORT \
  --app-dir src
```

### 5. Launch the Streamlit UI

```bash
streamlit run src/doctoralliance_agent/streamlit_app.py
```

Visit `http://localhost:8501` in your browser.

---

## MCP Endpoints

1. **POST** `/mcp/retrieve`

   * **Body**: `{ "event_type": "appointment_reminder" }`
   * **Response**: `{ "persona": "...", "context": { ... } }`

2. **POST** `/mcp/plan`

   * **Body**: output of `/retrieve`
   * **Response**: `{ "persona": "...", "summary": "..." }`

3. **POST** `/mcp/generate`

   * **Body**: output of `/plan`
   * **Response**: `{ "persona": "...", "response": "..." }`

4. **POST** `/mcp/respond`

   * **Body**: `{ "event_type":"...", "response":"...", "context":{...} }`
   * **Response**: delivery results JSON

---

## Customization

* **Persona Resolver** (`persona_resolver.py`): map events to personas
* **Vault** (`vault.py`): stubbed EHR/Billing/HHA calls
* **Prompt Builder** (`agents/prompt_builder.py`): persona-specific instructions
* **GeminiAgent** (`agents/gemini_agent.py`): integrates with CrewAI/Gemini
* **Delivery Channels** (`delivery/`): email, SMS, popup
* **Escalation** (`escalation/`): retries and reminders
* **Gmail Listener** (`gmail/`): parse inbound replies

---

## Testing

* Use **Invoke-RestMethod** in PowerShell for quick API tests
* Use **test\_sms.py** and **test\_email.py** scripts for isolated channel testing

---

