from PySide6.QtWidgets import (QMainWindow, QHBoxLayout,
QVBoxLayout, QPushButton, QWidget, QFrame, QLabel, QLineEdit)
from PySide6.QtGui import QColor, QFont, QIntValidator
from Multiplicacao import Multiplicando


class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.InitialFunction()
        self.list_values = []

    def InitialFunction(self):
        self.setWindowTitle("Calculator Program")
        self.setFixedSize(450, 300)

        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)
        self.setStyleSheet("background-color: black;")

        central_layout = QVBoxLayout(central_widget)

        self.frame = QFrame(self)
        self.frame.setFrameShape(QFrame.StyledPanel)

        self.qv_2 = QVBoxLayout(self.frame)
        
        self.btn_Calcular = QPushButton("Calcular",self)
        self.btn_somar = QPushButton("+", self)
        self.btn_dividir = QPushButton("/", self)
        self.btn_multiplicar = QPushButton("X", self)
        self.btn_subtrair = QPushButton("-", self)
        
        self.btn_Calcular.setStyleSheet("background-color: white; color: black;")
        self.btn_somar.setStyleSheet("background-color: white; color: black;")
        self.btn_dividir.setStyleSheet("background-color: white; color: black;")
        self.btn_multiplicar.setStyleSheet("background-color: white; color: black;")
        self.btn_subtrair.setStyleSheet("background-color: white; color: black;")

        self.lbl_valor_Digitado = QLabel("Aqui ficarão os valores conforme forem sendo digitados!",self)
        self.lbl_valor_Digitado.setStyleSheet("background-color: white;")

        int_validator = QIntValidator()
        self.inp_result = QLineEdit(self)
        self.inp_result.setValidator(int_validator)
        self.inp_result.setStyleSheet("background-color: white;")
        self.inp_result.setPlaceholderText("Digite o valor a ser calculado:")

        self.frame_resultado = QFrame(self)
        self.frame_resultado.setFrameShape(QFrame.StyledPanel)
        self.frame_resultado.setStyleSheet("background-color: white;")

        self.frame_resultado_container = QVBoxLayout(self.frame_resultado)

        self.font1 = QFont("Arial")
        self.font1.setPixelSize(14)
        self.lbl_valor_Digitado.setFont(self.font1)

        self.btn_multiplicar.clicked.connect(self.ClickedButtonMultiplicar)

        self.frame_resultado_container.addWidget(self.lbl_valor_Digitado)
        self.frame_resultado_container.addSpacing(300)
        self.frame_resultado_container.addWidget(self.inp_result)

        central_layout.addWidget(self.frame_resultado)
        central_layout.addWidget(self.frame)
        self.qv_2.addWidget(self.btn_somar)
        self.qv_2.addWidget(self.btn_dividir)
        self.qv_2.addWidget(self.btn_multiplicar)
        self.qv_2.addWidget(self.btn_subtrair)
        self.qv_2.addWidget(self.btn_Calcular)

    def ClickedButtonMultiplicar(self):
            self.list_values.append(self.inp_result.text())
            self.value12 = self.inp_result.text()
            self.lbl_valorantigo = QLabel(self.value12+" X", self)
            self.frame_resultado_container.addWidget(self.lbl_valorantigo)
            self.frame_resultado_container.addWidget(self.inp_result)
            self.inp_result.clear()
            print(self.list_values)
            for i in (self.value12):
                print(i)
            self.btn_Calcular.clicked.connect(self.ClickedButtonCalcular)

    def ClickedButtonCalcular(self):
        pass        







        

        
        

