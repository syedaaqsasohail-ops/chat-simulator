# messages.py
# Base message classes and decorators

class Message:
    def __init__(self, content):
        self.content = content

    def show(self):
        return self.content

# Decorator base that wraps a Message instance
class MessageDecorator(Message):
    def __init__(self, message):
        self._message = message

    def show(self):
        return self._message.show()

class TimestampDecorator(MessageDecorator):
    def show(self):
        import datetime
        return f"[{datetime.datetime.now().strftime('%H:%M:%S')}] {self._message.show()}"

class EmojiDecorator(MessageDecorator):
    def show(self):
        return f"{self._message.show()} 😀"

# --- Slash command decorators for GUI ---
class BoldDecorator(MessageDecorator):
    def show(self):
        return self._message.show()  # return plain text only

class ItalicDecorator(MessageDecorator):
    def show(self):
        return self._message.show()  # return plain text only
