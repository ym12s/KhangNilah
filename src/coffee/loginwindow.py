from PySide6.QtWidgets import QMainWindow, QMessageBox, QPushButton
from PySide6.QtCore import Signal
from src.__ui.ui_login import Ui_Form
from src.coffee.YSql import get_connection
import subprocess
import os

def ensure_login_ui_compiled():
    try:
        ui_file = os.path.join("src", "__ui", "login.ui")
        output_file = os.path.join("src", "__ui", "ui_login.py")
        
        if not os.path.exists(output_file) and os.path.exists(ui_file):
            subprocess.run(["pyside6-uic", ui_file, "-o", output_file], check=True)
            
    except Exception as e:
        print(f"Error compiling login UI: {e}")
        return False
    return True

# Gọi hàm này trước khi import Ui_Form
ensure_login_ui_compiled()

class LoginWindow(QMainWindow):
    login_successful = Signal(str)

    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        
        self.ui.btnLogin_3.clicked.connect(self.handle_login)
        
        self.setWindowTitle("Đăng nhập - Coffee MTU")
        self.setFixedSize(1200, 800) 

    def handle_login(self):
        username = self.ui.txtUser.text().strip()
        password = self.ui.txtPass.text().strip()
        
        if not username or not password:
            QMessageBox.warning(self, "Lỗi", "Vui lòng nhập đầy đủ tên đăng nhập và mật khẩu!")
            return
            
        if self.checklogin(username, password):
            self.login_successful.emit(str(self.idNhanVien))
            self.close()
        else:
            QMessageBox.warning(self, "Lỗi", "Sai tên đăng nhập hoặc mật khẩu!")

    def checklogin(self, username, password):
        try:
            conn = get_connection()
            cursor = conn.cursor()
            query = "SELECT idNhanVien FROM tb_User WHERE username = ? AND password = ?"
            cursor.execute(query, (username, password))
            result = cursor.fetchone()
            
            if result:
                self.idNhanVien = result[0]
                return True
            return False
            
        except Exception as e:
            QMessageBox.critical(self, "Lỗi", f"Lỗi kết nối database: {str(e)}")
            return False
        finally:
            conn.close() 