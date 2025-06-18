import logging
from pathlib import Path

LOG_DIR = Path(__file__).parent.parent / "logs"
LOG_DIR.mkdir(exist_ok=True)
logging.basicConfig(
    filename=LOG_DIR/"app.log",
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s"
)
logger = logging.getLogger("aidoc_alliance")

def audit(event_type: str, payload: dict, channel: str):
    logger.info(f"EVENT={event_type} CHANNEL={channel} PAYLOAD={payload}")
