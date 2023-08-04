from app.messages.services.message_service import MessageService

def message_service() -> MessageService:
    """Get message service."""
    return MessageService()