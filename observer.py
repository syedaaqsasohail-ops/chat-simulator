# observer.py
# Simple Subject/Observer base classes

class Subject:
    def __init__(self):
        self._observers = []

    def attach(self, observer):
        if observer not in self._observers:
            self._observers.append(observer)

    def detach(self, observer):
        if observer in self._observers:
            self._observers.remove(observer)

    def notify(self, message_text):
        # message_text is a plain string (already .show())
        for obs in self._observers:
            try:
                obs.update(message_text)
            except Exception:
                pass

class Observer:
    def update(self, message_text):
        raise NotImplementedError
