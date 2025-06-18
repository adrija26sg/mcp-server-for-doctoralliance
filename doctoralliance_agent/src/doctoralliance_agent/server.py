from fastapi import FastAPI, Body
from doctoralliance_agent.src.doctoralliance_agent.persona_resolver         import resolve_persona
from doctoralliance_agent.src.doctoralliance_agent.data_fetcher             import fetch_context
from doctoralliance_agent.src.doctoralliance_agent.summary_builder          import build_summary
from agents.prompt_builder    import build_prompt
from agents.gemini_agent      import GeminiAgent
from delivery.channel_selector import deliver
from dotenv import load_dotenv
load_dotenv()  # reads the root .env

app = FastAPI(title="AgenticaIDoctorAlliance MCP")

@app.post("/mcp/retrieve")
def retrieve(payload: dict = Body(...)):
    persona = resolve_persona(payload["event_type"])
    ctx     = fetch_context(persona)
    return {"persona": persona, "context": ctx}

@app.post("/mcp/plan")
def plan(payload: dict = Body(...)):
    summary = build_summary(payload["context"])
    return {"persona": payload["persona"], "summary": summary}

@app.post("/mcp/generate")
async def generate(payload: dict = Body(...)):
    prompt = build_prompt(payload["persona"], payload["summary"])
    out    = await GeminiAgent(payload["persona"]).handle(prompt)
    return {"persona": payload["persona"], **out}

@app.post("/mcp/respond")
def respond(payload: dict = Body(...)):
    return deliver(
        payload["event_type"],
        payload["response"],
        payload["context"]
    )
