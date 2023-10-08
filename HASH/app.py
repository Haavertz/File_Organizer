from PySide6.QtWidgets import (QMainWindow, QApplication, QFrame, QLabel, 
QVBoxLayout, QHBoxLayout, QWidget, QPushButton)
from PySide6.QtGui import QFont
import sys


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.InitialAplication()

    def InitialAplication(self):
        self.setWindowTitle("Jogos Da Velha")
        self.setFixedSize(500,500)

        self.central_Widget = QWidget()
        self.setCentralWidget(self.central_Widget)

        self.layout_frame = QVBoxLayout(self.central_Widget)

        self.frame = QFrame(self)
        self.frame.setFrameShape(QFrame.StyledPanel)

        players1 = ("X")
        players2 = ("Y")

        self.lbl_Title = QLabel("             INSTEAD OF (" + players1+")")

        self.font = QFont("Arial")
        self.font.setPixelSize(30)
        self.lbl_Title.setFont(self.font)


        self.layout_frame.addWidget(self.lbl_Title)
        self.layout_frame.addWidget(self.frame)


        self.layout_frame_box = QVBoxLayout(self.frame)
        
        self.btn_1 = QPushButton(" ", self.frame)
        self.btn_1.setGeometry(10, 10, 250, 250)

        




if __name__ == "__main__":    
    App = QApplication(sys.argv)
    Janela = MainWindow()
    Janela.show()
    App.exec()