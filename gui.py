# gui.py
# Tkinter GUI for the chat simulator. GUI acts as an Observer.

import tkinter as tk
from chat_engine import ChatEngine
from observer import Observer

class ChatGUI(Observer):
    def __init__(self, master):
        self.master = master
        master.title("Simple Chat Simulator")

        # create engine (singleton)
        self.chat_engine = ChatEngine()
        # attach this GUI as observer
        self.chat_engine.attach(self)

        # Frame and widgets
        top_frame = tk.Frame(master)
        top_frame.pack(padx=10, pady=6)

        self.text_area = tk.Text(top_frame, height=15, width=60, state=tk.DISABLED, wrap=tk.WORD)
        self.text_area.pack(side=tk.TOP)

        # Define tags for bold and italic
        self.text_area.tag_configure("bold", font=("TkDefaultFont", 10, "bold"))
        self.text_area.tag_configure("italic", font=("TkDefaultFont", 10, "italic"))

        entry_frame = tk.Frame(master)
        entry_frame.pack(padx=10, pady=6)

        self.entry = tk.Entry(entry_frame, width=45)
        self.entry.pack(side=tk.LEFT, padx=(0,6))
        self.entry.bind("<Return>", lambda event: self.send_message())

        self.send_button = tk.Button(entry_frame, text="Send", command=self.send_message)
        self.send_button.pack(side=tk.LEFT)

        # optional simulate incoming button (for demo)
        demo_frame = tk.Frame(master)
        demo_frame.pack(padx=10, pady=(0,10))
        self.demo_btn = tk.Button(demo_frame, text="Simulate Incoming", command=self.simulate_incoming)
        self.demo_btn.pack()

    def send_message(self):
        content = self.entry.get().strip()
        if not content:
            return
        # send via engine (engine will notify observers)
        self.chat_engine.send_message("text", content, decorate=True)
        self.entry.delete(0, tk.END)

    def update(self, message_data):
        self.text_area.config(state=tk.NORMAL)

        # message_data can be a tuple (text, tag) or just text
        if isinstance(message_data, tuple):
            message_text, tag = message_data
        else:
            message_text, tag = message_data, None

        if tag:
            self.text_area.insert(tk.END, message_text + "\n", tag)
        else:
            self.text_area.insert(tk.END, message_text + "\n")

        self.text_area.see(tk.END)
        self.text_area.config(state=tk.DISABLED)

    def simulate_incoming(self):
        # simple demo: send a fake incoming message from "friend"
        self.chat_engine.send_message("text", "Hello from friend!", decorate=True)

def run_gui():
    root = tk.Tk()
    app = ChatGUI(root)
    root.mainloop()
 