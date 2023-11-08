from pydantic import BaseModel


class CreateStoryRequest(BaseModel):
    text: str


class CreateResponse(BaseModel):
    id: int
