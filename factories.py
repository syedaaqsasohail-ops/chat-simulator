# factories.py
# Factory pattern and a simple ChatSessionBuilder

from messages import Message

class MessageFactory:
    @staticmethod
    def create_message(msg_type, content):
        # For now we only use "text" type; extend later if needed
        if msg_type == "text":
            return Message(content)
        return Message(content)

class ChatSession:
    def __init__(self):
        self.participants = []
        self.history = []

class ChatSessionBuilder:
    def __init__(self):
        self.session = ChatSession()

    def add_participant(self, name):
        self.session.participants.append(name)
        return self

    def add_history(self, message_instance):
        # expects a Message (or decorated Message)
        self.session.history.append(message_instance.show())
        return self

    def build(self):
        return self.session
 