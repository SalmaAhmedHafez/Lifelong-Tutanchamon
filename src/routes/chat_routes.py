from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import Optional
from controllers.chat_controller import ChatController

router = APIRouter()
chat_controller = ChatController()

class ChatRequest(BaseModel):
    message: str

class ChatResponse(BaseModel):
    success: bool
    response: Optional[str] = ""
    error: Optional[str] = ""

@router.post("/chat", response_model=ChatResponse)
async def chat_endpoint(chat_request: ChatRequest):
    result = chat_controller.process_message(chat_request.message)
    
    # Create response with explicit values to avoid None issues
    return ChatResponse(
        success=result.get("success", False),
        response=result.get("response", ""),
        error=result.get("error", "")
    )

@router.get("/health")
async def health_check():
    return {
        "status": "healthy", 
        "service": "Tutankhamun Chatbot",
        "message": "Speak with Pharaoh Tutankhamun himself! 🏺"
    }