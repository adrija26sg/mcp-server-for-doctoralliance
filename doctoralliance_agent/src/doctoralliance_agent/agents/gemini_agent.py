import os
import httpx
import logging
from typing import Dict

logger = logging.getLogger(__name__)

CREWAI_API_KEY     = os.getenv("CREWAI_API_KEY")
CREWAI_ENDPOINT    = os.getenv("CREWAI_ENDPOINT")
CREWAI_MODEL       = os.getenv("CREWAI_MODEL", "gemini-pro")
CREWAI_TEMPERATURE = float(os.getenv("CREWAI_TEMPERATURE", "0.7"))

class GeminiAgent:
    def __init__(self, persona: str):
        if not CREWAI_API_KEY:
            raise RuntimeError("CREWAI_API_KEY not set")
        self.persona = persona

    async def handle(self, prompt: str) -> Dict[str, str]:
        headers = {
            "Authorization": f"Bearer {CREWAI_API_KEY}",
            "Content-Type": "application/json",
        }
        payload = {
            "model": CREWAI_MODEL,
            "messages": [
                {"role":"system","content":f"Persona: {self.persona}"},
                {"role":"user","content":prompt}
            ],
            "temperature": CREWAI_TEMPERATURE,
        }
        async with httpx.AsyncClient(timeout=30.0) as client:
            try:
                resp = await client.post(CREWAI_ENDPOINT, json=payload, headers=headers)
                resp.raise_for_status()
            except Exception as e:
                logger.exception("CrewAI error")
                return {"response": f"Error: {e}"}

        data = resp.json()
        text = data.get("choices",[{}])[0].get("message",{}).get("content","").strip()
        return {"response": text}
