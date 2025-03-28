import sys
import google.generativeai as ai
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QTextEdit, QLabel
from PySide6.QtCore import QThread, Signal

API_KEY = 'AIzaSyCoEr6EI-WLyVVUjKbaok-F2bF56haj7RU'
ai.configure(api_key=API_KEY)
model = ai.GenerativeModel("gemini-2.0-pro-exp")
chat = model.start_chat()

class yai(QThread):
    tinhieuPhanHoi = Signal(str)

    def __init__(self, tinNhan):
        super().__init__()
        self.tinNhan = tinNhan

    def run(self):
        if self.tinNhan.lower() == "khang":
            phanHoi = "Khang là người tuyệt vời nhất trên thế giới"
        else:
            try:
                phanHoi = chat.send_message(self.tinNhan).text
            except Exception as e:
                phanHoi = f"Lỗi: {str(e)}"
        self.tinhieuPhanHoi.emit(phanHoi)