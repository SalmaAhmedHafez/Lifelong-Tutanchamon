from fastapi import FastAPI
from routes.chat_routes import router as chat_router
from utils.config import Config
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="Tutankhamun Chatbot",
    description="Chat with Pharaoh Tutankhamun himself",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc"
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)


# Include routes
app.include_router(chat_router, prefix="/api/v1")

@app.on_event("startup")
async def startup_event():
    if not Config.GOOGLE_API_KEY:
        raise ValueError("GOOGLE_API_KEY not found in environment variables")
    print("✅ Tutankhamun Chatbot initialized! Speak with the Pharaoh... 🏺")

@app.get("/")
async def root():
    return {
        "message": "Tutankhamun Chatbot API", 
        "description": "Chat with Pharaoh Tutankhamun himself",
        "endpoints": {
            "chat": "/api/v1/chat",
            "health": "/api/v1/health",
            "docs": "/docs"
        }
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        app,  # Pass app directly (no reload)
        host=Config.HOST,
        port=Config.PORT
        # Remove reload=True
    )
