def build_prompt(persona: str, summary: str) -> str:
    instructions = {
        "patient":       "You are speaking to the patient. Use layman terms.",
        "nurse":         "You are speaking to a nurse. Use clinical clarity.",
        "billing_clerk": "You are speaking to billing staff. Be precise.",
        "default_persona": "Provide a concise, professional response."
    }
    instr = instructions.get(persona, instructions["default_persona"])
    return (
        f"{instr}\n\n"
        f"Context (de-identified):\n{summary}\n\n"
        "Respond without PHI."
    )
