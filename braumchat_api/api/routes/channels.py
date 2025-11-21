from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List

from ...schemas.channel import ChannelCreate, ChannelRead
from ...api.deps import get_db_dep, get_current_user
from ...services.channel_service import create_channel, list_channels, get_channel

router = APIRouter()

@router.post("/workspaces/{workspace_id}/channels", response_model=ChannelRead)
async def create(workspace_id: int, payload: ChannelCreate, db: AsyncSession = Depends(get_db_dep), user=Depends(get_current_user)):
    ch = await create_channel(db, workspace_id=workspace_id, name=payload.name, is_private=payload.is_private)
    return ch

@router.get("/workspaces/{workspace_id}/channels", response_model=List[ChannelRead])
async def list_all(workspace_id: int, db: AsyncSession = Depends(get_db_dep), user=Depends(get_current_user)):
    return await list_channels(db, workspace_id)

@router.get("/{channel_id}", response_model=ChannelRead)
async def get_one(channel_id: int, db: AsyncSession = Depends(get_db_dep), user=Depends(get_current_user)):
    ch = await get_channel(db, channel_id)
    if not ch:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    return ch
