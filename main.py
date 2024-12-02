"""Программа планировщик мероприятий."""

import sys

from windows.login import Login
from PyQt6.QtWidgets import QApplication

def main():
    app = QApplication(sys.argv)
    ex = Login()
    ex.show()
    sys.exit(app.exec())
    

if __name__ == "__main__":
    main()
