from fastapi import FastAPI

from app.models import StoryInput
from app.context_manager import ContextManager
from app.story_processor import process_story

app = FastAPI()

context_manager = ContextManager()


@app.get("/")
def home():
    return {"message": "Story Visualizer API Running"}


@app.post("/generate-story")
def generate_story(story: StoryInput):

    # Reset memory for new story
    global context_manager
    context_manager = ContextManager()

    scenes = process_story(
        story.text,
        context_manager
    )

    return {
        "scenes": scenes,
        "final_memory": context_manager.context
    }