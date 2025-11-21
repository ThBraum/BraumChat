from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi.security import OAuth2PasswordRequestForm

from ...schemas.auth import Token
from ...schemas.user import UserCreate, UserRead
from ...api.deps import get_db_dep, get_current_user
from ...services.user_service import create_user, get_user_by_email
from ...services.auth_service import authenticate_user, create_tokens_for_user

router = APIRouter()

@router.post("/register", response_model=UserRead)
async def register(payload: UserCreate, db: AsyncSession = Depends(get_db_dep)):
    existing = await get_user_by_email(db, payload.email)
    if existing:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Email already registered")
    user = await create_user(db, email=payload.email, password=payload.password, display_name=payload.display_name)
    return user

@router.post("/login", response_model=Token)
async def login(form_data: OAuth2PasswordRequestForm = Depends(), db: AsyncSession = Depends(get_db_dep)):
    user = await authenticate_user(db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Incorrect credentials")
    tokens = await create_tokens_for_user(user)
    return {"access_token": tokens["access_token"], "token_type": "bearer", "refresh_token": tokens["refresh_token"]}

@router.post("/refresh", response_model=Token)
async def refresh(refresh_token: str):
    # TODO: validate refresh token and rotate
    raise HTTPException(status_code=status.HTTP_501_NOT_IMPLEMENTED, detail="Refresh flow not implemented yet")

@router.get("/me", response_model=UserRead)
async def me(user=Depends(get_current_user)):
    return user
