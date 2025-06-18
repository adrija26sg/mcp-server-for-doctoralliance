from vault import fetch_ehr, fetch_billing, fetch_hha_records

def fetch_context(persona: str) -> dict:
    # In reality, map persona→patient_id
    patient_id = persona
    return {
        "ehr":        fetch_ehr(patient_id),
        "billing":    fetch_billing(patient_id),
        "hha":        fetch_hha_records(patient_id),
        "user_email": "jane.doe@example.com",
        "user_phone": "+15555551234",
        "channels":   ["email", "popup"],
    }
