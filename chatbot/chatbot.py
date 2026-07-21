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

model = ChatMistralAI(
    model = "mistral-small-latest",
)

mode = "Simple"
choice = input()
if(choice=="0"):
    mode = "Angry"
elif(choice=="1"):
    mode = "Funny"
elif(choice=="2"):
    mode = "Sad"

messages = [
    SystemMessage(f"You act as a {mode} AI ChatBot")
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