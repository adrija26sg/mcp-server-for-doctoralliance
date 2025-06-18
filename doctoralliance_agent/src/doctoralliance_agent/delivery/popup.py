import threading, asyncio, os, websockets

WS_URL = os.getenv("WS_URL")

async def _push(msg: str):
    async with websockets.connect(WS_URL) as ws:
        await ws.send(msg)

def send_popup(body: str, context: dict):
    threading.Thread(target=lambda: asyncio.run(_push(body))).start()
    return {"status": "queued"}
