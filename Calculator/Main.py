from PySide6.QtWidgets import QApplication
from App import MainWindow
import sys

if __name__ == '__main__':
    app = QApplication(sys.argv)
    windown = MainWindow()
    windown.show()
    app.exec()