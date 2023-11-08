from pydantic import BaseModel


class CreatePostRequest(BaseModel):
    code: str


class CreateResponse(BaseModel):
    id: int


class PostsResponse(BaseModel):
    id: int
    code: str
    likes: int
    comment_1: str
    comment_2: str


class CreateComment(BaseModel):
    text: str
    parent_id: int | None


class FeedResponseItem(BaseModel):
    code: str
    likes: int
    comment_1: str | None
    comment_2: str | None
