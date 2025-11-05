from pydantic import BaseModel
from typing import Optional

class NoteIn(BaseModel):
    title: str
    content: str

class Note(NoteIn):
    id: str
