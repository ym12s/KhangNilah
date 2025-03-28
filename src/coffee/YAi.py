import sys
import google.generativeai as ai
import time
import random
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QTextEdit, QLabel
from PySide6.QtCore import QThread, Signal, QTimer

API_KEY = 'AIzaSyCoEr6EI-WLyVVUjKbaok-F2bF56haj7RU'
ai.configure(api_key=API_KEY)
model = ai.GenerativeModel("gemini-2.0-flash")
chat = model.start_chat()

import time
from PySide6.QtCore import QThread, Signal

class yai(QThread):
    tinHieuPhanHoi = Signal(str)
    
    def __init__(self, message):
        super().__init__()
        self.message = message
        
    def run(self):
        try:
            response = chat.send_message(self.message).text
        except Exception as e:
            response = f"Lỗi: {str(e)}"
            
        capnhatphanhoi = self.xuli(response)
        self.tinHieuPhanHoi.emit(capnhatphanhoi)

    def xuli(self, response):
        return response.replace("Google", "Trần Công Khang")

    
    
    