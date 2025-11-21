from typing import Dict, List
from fastapi import WebSocket
from collections import defaultdict

class ConnectionManager:
    def __init__(self):
        # channel_id -> list[WebSocket]
        self.active_connections: Dict[str, List[WebSocket]] = defaultdict(list)

    async def connect(self, channel_key: str, websocket: WebSocket):
        await websocket.accept()
        self.active_connections[channel_key].append(websocket)

    def disconnect(self, channel_key: str, websocket: WebSocket):
        if websocket in self.active_connections.get(channel_key, []):
            self.active_connections[channel_key].remove(websocket)

    async def broadcast(self, channel_key: str, message: dict):
        conns = list(self.active_connections.get(channel_key, []))
        for conn in conns:
            try:
                await conn.send_json(message)
            except Exception:
                # ignore send errors
                pass

# singleton manager
manager = ConnectionManager()
