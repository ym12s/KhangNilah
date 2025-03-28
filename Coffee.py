import sys
import subprocess
import os
from PySide6.QtWidgets import QApplication
from PySide6.QtGui import QIcon

def ensure_directory_exists(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)

def compile_ui_files():
    try:
        # Đảm bảo các thư mục tồn tại
        ensure_directory_exists(UI_DIR)
        
        # Compile login.ui
        if not os.path.exists(LOGIN_FILE) and os.path.exists(LOGIN_UI):
            subprocess.run(["pyside6-uic", LOGIN_UI, "-o", LOGIN_FILE], check=True)
            
        # Compile form.ui
        form_ui = os.path.join(UI_DIR, "form.ui")
        form_py = os.path.join(UI_DIR, "ui_mainwindow.py")
        if not os.path.exists(form_py) and os.path.exists(form_ui):
            subprocess.run(["pyside6-uic", form_ui, "-o", form_py], check=True)
            
        # Compile resources
        if not os.path.exists(QRC_FILE) and os.path.exists(RESOURCE_QRC):
            subprocess.run(["pyside6-rcc", RESOURCE_QRC, "-o", QRC_FILE], check=True)
            
    except subprocess.CalledProcessError as e:
        print(f"Error compiling UI files: {e}")
        return False
    except Exception as e:
        print(f"Unexpected error: {e}")
        return False
    return True

# Định nghĩa các đường dẫn
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
SRC_DIR = os.path.join(BASE_DIR, "src")
COFFEE_DIR = os.path.join(SRC_DIR, "coffee")
UI_DIR = os.path.join(SRC_DIR, "__ui")
LOGIN_UI = os.path.join(UI_DIR, "login.ui")
LOGIN_FILE = os.path.join(UI_DIR, "ui_login.py")
QRC_FILE = os.path.join(BASE_DIR, "resources_rc.py")
RESOURCE_QRC = os.path.join(BASE_DIR, "resources.qrc")

# Thêm đường dẫn vào sys.path
if SRC_DIR not in sys.path:
    sys.path.append(SRC_DIR)
if COFFEE_DIR not in sys.path:
    sys.path.append(COFFEE_DIR)

# Compile UI files
if not compile_ui_files():
    print("Failed to compile UI files. Please check if PySide6 tools are installed correctly.")
    sys.exit(1)

try:
    from src.coffee.mainwindow import MainWindow
    from src.coffee.loginwindow import LoginWindow
except ModuleNotFoundError as e:
    print(f"Error importing required modules: {e}")
    print("Please check if all required files are present and properly compiled.")
    sys.exit(1)

class Application:
    def __init__(self):
        self.app = QApplication(sys.argv)
        self.app.setStyle("Fusion")
        
        # Sử dụng đường dẫn tương đối cho icon
        icon_path = os.path.join(BASE_DIR, "src", "ass", "icon.ico")
        if os.path.exists(icon_path):
            self.app.setWindowIcon(QIcon(icon_path))
        
        self.login = LoginWindow()
        self.login.login_successful.connect(self.show_main_window)
        self.login.show()

    def show_main_window(self, idNhanVien):
        self.main_window = MainWindow(idNhanVien=idNhanVien)
        self.main_window.show()
        self.login.close()

    def run(self):
        return self.app.exec()

if __name__ == "__main__":
    app = Application()
    sys.exit(app.run())            
