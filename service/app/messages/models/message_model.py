from pydantic import BaseModel, Field

class Message(BaseModel):
    id: int = Field(..., example=1)
    message: str = Field(..., example="Hello World")