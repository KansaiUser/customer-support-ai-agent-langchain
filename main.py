from fastapi import FastAPI
from pydantic import BaseModel
from agent import ask_support_agent
import mlflow

from fastapi.middleware.cors import CORSMiddleware

mlflow.set_tracking_uri("http://localhost:5000") 

app = FastAPI(
    title="customer support ai agent"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_headers=["*"],
    allow_methods=["*"]
)

class ChatRequest(BaseModel): 
    message: str

@app.get("/")
def root():
    return{
        "message": "customer support AI Agent running"
    }

@app.post("/chat")
# @mlflow.trace
def chat(request: ChatRequest):
    response = ask_support_agent(request.message)
    return response