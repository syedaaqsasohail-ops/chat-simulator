# chat_engine.py
from observer import Subject
from factories import MessageFactory
from messages import Message, TimestampDecorator, EmojiDecorator, BoldDecorator, ItalicDecorator

class ChatEngine(Subject):
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(ChatEngine, cls).__new__(cls)
            Subject.__init__(cls._instance)
            cls._instance.chat_log = []
        return cls._instance

    def send_message(self, msg_type, content, decorate=True):
        # Slash commands first
        if content.startswith("/bold "):
            message_obj = BoldDecorator(Message(content[6:].strip()))
            tag = "bold"
        elif content.startswith("/italic "):
            message_obj = ItalicDecorator(Message(content[8:].strip()))
            tag = "italic"
        else:
            message_obj = MessageFactory.create_message(msg_type, content)
            tag = None
            if decorate:
                message_obj = TimestampDecorator(EmojiDecorator(message_obj))

        text = message_obj.show()
        self.chat_log.append((text, tag))  # store text with optional tag
        self.notify((text, tag))
        return message_obj

