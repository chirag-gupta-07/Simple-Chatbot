from dotenv import load_dotenv
load_dotenv()

from langchain_mistralai import ChatMistralAI
from langchain.messages import HumanMessage, AIMessage, SystemMessage

from fastapi import FastAPI
from fastapi.responses import FileResponse
from pydantic import BaseModel
import os
import uvicorn

app = FastAPI()

try:
    model = ChatMistralAI(model="mistral-small-latest")
except Exception as e:
    print(f"Warning: Could not initialize ChatMistralAI. Did you set MISTRAL_API_KEY? Error: {e}")
    model = None

messages = [
    SystemMessage("You act as a Funny AI ChatBot")
]

class ChatRequest(BaseModel):
    message: str
    mode: str = "Funny"

@app.post("/api/chat")
async def chat(request: ChatRequest):
    messages[0] = SystemMessage(f"You act as a {request.mode} AI ChatBot")
    messages.append(HumanMessage(request.message))
    response = model.invoke(messages)
    messages.append(AIMessage(response.content))
    return {"reply": response.content}

frontend_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), "frontend")

@app.get("/")
async def get_index():
    return FileResponse(os.path.join(frontend_dir, "index.html"))

@app.get("/style.css")
async def get_css():
    return FileResponse(os.path.join(frontend_dir, "style.css"))

@app.get("/script.js")
async def get_js():
    return FileResponse(os.path.join(frontend_dir, "script.js"))

if __name__ == "__main__":
    uvicorn.run("chatbot:app", host="0.0.0.0", port=8000, reload=True)