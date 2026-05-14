from fastapi import FastAPI
from pydantic import BaseModel
from agent import ask_support_agent

app = FastAPI(
    title="Customer Support AI API",
    version="1.0.0"
)

class ChatRequest(BaseModel):
    message: str

@app.get("/")
def root():
    return {
        "message": "Customer Support AI API Running"
    }

@app.post("/chat")
def chat(request: ChatRequest):

    response = ask_support_agent(request.message)

    return response