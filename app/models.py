from pydantic import BaseModel
from typing import List

class StoryInput(BaseModel):
    text: str

class SceneData(BaseModel):
    characters: List[str]
    action: str
    location: str
    prompt: str