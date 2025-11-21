from fastapi import APIRouter, WebSocket, WebSocketDisconnect, Depends
from ...realtime.manager import manager
from ...api.deps import get_current_user

router = APIRouter()

@router.websocket("/ws/chat/{workspace_id}/{channel_id}")
async def ws_channel(websocket: WebSocket, workspace_id: int, channel_id: int, token: str | None = None):
    # authentication via token param or headers should be implemented
    channel_key = f"w:{workspace_id}:c:{channel_id}"
    await manager.connect(channel_key, websocket)
    try:
        while True:
            data = await websocket.receive_json()
            # basic protocol: {"type": "message", "content": "..."}
            msg_type = data.get("type")
            if msg_type == "message":
                # TODO: validate, persist and broadcast
                await manager.broadcast(channel_key, {"type": "message", "payload": data.get("content")})
            elif msg_type == "typing":
                await manager.broadcast(channel_key, {"type": "typing", "user": data.get("user")})
    except WebSocketDisconnect:
        manager.disconnect(channel_key, websocket)
