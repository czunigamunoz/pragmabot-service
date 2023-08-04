from pydantic import BaseModel
import requests

from app.messages.models import Message

URL_PERSISTENCE = "https://url"

class MessageService:
    """Message service."""
    
    def __init__(self):
        """Init."""
        self.messages = [
            {"id": 1, "message": "persistence 1"},
            {"id": 2, "message": "persistence 2"},
        ]

    async def get_all_messages(self) -> list[Message]:
        """Get all messages."""
        return self.messages

    def send_message(self, message: Message) -> []:
        """Send a message."""
        #return await requests.get(URL_PERSISTENCE, data message)
        return {"id": 5, "message": "persistence test"}