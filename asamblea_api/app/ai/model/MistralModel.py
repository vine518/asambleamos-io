from pydantic import BaseModel, Field


class MessageHistoryModel(BaseModel):
    message: str = Field(title='Message')


# Chat form
class ChatForm(BaseModel):
    chat: str = Field(title=' ', max_length=1000)
