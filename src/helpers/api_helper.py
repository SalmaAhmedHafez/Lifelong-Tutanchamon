from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.schema import HumanMessage, SystemMessage
from utils.config import Config
from utils.prompts import SYSTEM_PROMPT


class ChatbotHelper:
    def __init__(self):
        self.llm = ChatGoogleGenerativeAI(
            model=Config.MODEL_NAME,
            google_api_key=Config.GOOGLE_API_KEY,
            temperature=Config.TEMPERATURE
        )
    
    def get_chat_response(self, user_message: str) -> str:
        try:
            # Combine system prompt with user message for Gemini
            full_prompt = f"{SYSTEM_PROMPT}\n\nUser: {user_message}\n\nTutankhamun:"
            
            messages = [
                HumanMessage(content=full_prompt)
            ]
            
            response = self.llm.invoke(messages)
            # Ensure we always return a string, never None
            return str(response.content) if response.content else "I am contemplating your question, noble visitor. Please ask again."
            
        except Exception as e:
            return f"I apologize, but the gods are not speaking clearly today. Please try again. (Error: {str(e)})"