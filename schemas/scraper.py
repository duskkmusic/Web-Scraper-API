from pydantic import BaseModel, HttpUrl


class ScrapeRequest(BaseModel):
    url: HttpUrl


class TitleResponse(BaseModel):
    title: str


class H1Response(BaseModel):
    h1: str

