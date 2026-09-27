
from fastapi import APIRouter, WebSocket
router=APIRouter()
@router.websocket("/ws/medi/{user_id}")
async def medi_ws(ws: WebSocket, user_id: str):
    await ws.accept()
    await ws.send_json({"type":"connected","message":"Medi WebSocket connected - 12 langs streaming","user_id":user_id})
    while True:
        data = await ws.receive_text()
        # Mock streaming via WS (modern alternative to SSE)
        for token in f"I understand {data} is worrying. In Tamil: ... 💙".split():
            await ws.send_json({"type":"token","token":token})
        await ws.send_json({"type":"done"})
