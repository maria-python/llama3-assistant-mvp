import json
from typing import List, Dict

class Memory:
    def __init__(self):
        self.chat_history: List[Dict[str, str]] = []

    def add_message(self, role: str, content: str):
        self.chat_history.append({"role": role, "content": content})

    def get_history(self) -> List[Dict[str, str]]:
        return self.chat_history

    def get_recent_messages(self, limit: int = 10) -> List[Dict[str, str]]:
        return self.chat_history[-limit:]

    def save(self, filename: str = "memory.json"):
        with open(filename, "w", encoding="utf-8") as f:
            json.dump(self.chat_history, f, indent=2, ensure_ascii=False)

    def load(self, filename: str = "memory.json"):
        try:
            with open(filename, "r", encoding="utf-8") as f:
                self.chat_history = json.load(f)
        except FileNotFoundError:
            self.chat_history = []