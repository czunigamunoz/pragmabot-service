from starlette.requests import Request
from typing import Annotated

from app.messages.models import Message
from app.messages.services.message_service import MessageService

from app.messages.services import message_service

from fastapi import APIRouter, Depends

router = APIRouter()
MessageServiceDep = Annotated[MessageService, Depends(MessageService)]

@router.get("/", response_model=list[Message])
async def get_persistence() -> list[Message]:
    """Get all messages."""
    return await message_service().get_all_messages()

@router.post("/send", response_model=Message)
async def send_message(request: Request) -> Message:
    """Send a message."""
    message = await request.json()
    print(message)
    return message_service().send_message(message)