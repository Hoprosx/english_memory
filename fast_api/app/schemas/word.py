from pydantic import BaseModel


class Word(BaseModel):
    word: str


class Translate(BaseModel):
    word: str
    russian: list[Word]
