"""Программа планировщик мероприятий."""

import sys

from windows.EventManager import EventManager
from PyQt6.QtWidgets import QApplication

def main():
    app = QApplication(sys.argv)
    ex = EventManager()
    ex.show()
    sys.exit(app.exec())
    

if __name__ == "__main__":
    main()
