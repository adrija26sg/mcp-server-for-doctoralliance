import streamlit as st
import requests

API_BASE = "http://localhost:8000/mcp"

st.set_page_config(page_title="AgenticaIDoctorAlliance", layout="centered")
st.title("🖥️ AI Agent Dashboard (MCP)")

event = st.selectbox("Event Type",
    ["appointment_reminder", "follow_up_call", "billing_update"]
)

if st.button("Run End-to-End"):
    resp1 = requests.post(f"{API_BASE}/retrieve",
                          json={"event_type": event}).json()
    resp2 = requests.post(f"{API_BASE}/plan", json=resp1).json()
    resp3 = requests.post(f"{API_BASE}/generate", json=resp2).json()
    resp4 = requests.post(f"{API_BASE}/respond", json={
        "event_type": event,
        "response":   resp3["response"],
        "context":    resp1["context"]
    }).json()

    st.subheader("AI Response")
    st.write(resp3["response"])

    st.subheader("Delivery Results")
    st.json(resp4)
