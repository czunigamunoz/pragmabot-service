from fastapi import APIRouter

from app.messages.routers.message_router import router as persistence_router

router = APIRouter()

router.include_router(persistence_router, prefix="/message", tags=["Message"])