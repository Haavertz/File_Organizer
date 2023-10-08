from app import MainWindow
from PySide6.QtWidgets import QApplication
import sys

if __name__ == "__main__":    
    App = QApplication(sys.argv)
    Janela = MainWindow()
    Janela.show()
    App.exec()