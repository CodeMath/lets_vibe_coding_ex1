from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Dict
from datetime import datetime

app = FastAPI(title="Breadcrumb API")

class Breadcrumb(BaseModel):
    conversation_id: str
    step: int
    content: str
    timestamp: datetime = datetime.utcnow()

# Simple in-memory storage for demo purposes
conversations: Dict[str, List[Breadcrumb]] = {}

@app.post("/breadcrumbs/", response_model=Breadcrumb)
def create_breadcrumb(breadcrumb: Breadcrumb):
    conv = conversations.setdefault(breadcrumb.conversation_id, [])
    breadcrumb.step = len(conv) + 1
    conv.append(breadcrumb)
    return breadcrumb

@app.get("/breadcrumbs/{conversation_id}", response_model=List[Breadcrumb])
def get_conversation(conversation_id: str):
    if conversation_id not in conversations:
        raise HTTPException(status_code=404, detail="Conversation not found")
    return conversations[conversation_id]
