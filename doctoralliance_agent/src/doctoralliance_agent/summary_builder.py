def build_summary(context: dict) -> str:
    ehr     = context.get("ehr", {})
    billing = context.get("billing", {})
    hha     = context.get("hha", [])

    parts = [
        f"Age: {ehr.get('age')}",
        f"Diagnoses: {', '.join(ehr.get('diagnoses', []))}",
        f"Balance: ${billing.get('outstanding_balance')}",
        f"HHA visits: {len(hha)}"
    ]
    return " | ".join(parts)
