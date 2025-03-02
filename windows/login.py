import io
import sys

from PyQt6 import uic  
from PyQt6.QtWidgets import QApplication, QMainWindow
from windows.EventManager import EventManager


class Login(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("design/login.ui", self)
        self.setWindowTitle("Login")
        self.init_ui()

    def init_ui(self):
        self.label_error_register_in_bot.hide()
        self.login_btn.clicked.connect(self.login_processing)
    
    def login_processing(self):
        id = self.input_id.text()
        password = self.input_password.text()
        self.event_manager = EventManager()
        self.event_manager.show()
        self.close()