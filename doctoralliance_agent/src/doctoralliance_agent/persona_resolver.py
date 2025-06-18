PERSONA_MAP = {
    "appointment_reminder": "patient",
    "follow_up_call":       "nurse",
    "billing_update":       "billing_clerk",
}

def resolve_persona(event_type: str) -> str:
    return PERSONA_MAP.get(event_type, "default_persona")
