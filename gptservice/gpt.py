from revChatGPT.V1 import Chatbot
from flask import jsonify
import json
class BotHelper:
    def __init__(self, access_token, conv_id=None) -> None:
        self.chatbot = Chatbot(config={
        "access_token":access_token
    }, conversation_id=conv_id)
        self.conv_id = conv_id
    def start_chat(self, prompt):
        response = ""
        for data in self.chatbot.ask(
                prompt
        ):
            response = data["message"]

        return response
    def get_conversations(self, offset=0, limit=20):
        return self.chatbot.get_conversations(offset, limit)
    
    def setup_title(self, prompt):
        # print(self.conv_id)
        # print("message:", json.dumps(self.chatbot.get_msg_history(self.conv_id), indent=4), )
        self.chatbot.change_title(self.conv_id, ' '.join(prompt.split(' ')[:3]))