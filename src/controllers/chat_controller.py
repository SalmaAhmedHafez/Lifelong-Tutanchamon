from helpers.api_helper import ChatbotHelper

class ChatController:
    def __init__(self):
        self.chatbot_helper = ChatbotHelper()
    
    def process_message(self, message: str) -> dict:
        try:
            response = self.chatbot_helper.get_chat_response(message)
            return {
                "success": True,
                "response": response,
                "error": None
            }
        except Exception as e:
            return {
                "success": False,
                "response": None,
                "error": str(e)
            }