from PySide6.QtWidgets import (QMainWindow, QTextBrowser,
QVBoxLayout, QPushButton, QWidget, QFrame, QLabel, QLineEdit)
from PySide6.QtGui import QColor, QFont, QIntValidator
from Addiction import Multiplicando, Somando, Subtrair, Dividindo


class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.InitialFunction()
        self.list_values = []

    def InitialFunction(self):
        self.setWindowTitle("Calculator Program")
        self.setFixedSize(500, 350)

        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)
        self.setStyleSheet("background-color: black;")

        central_layout = QVBoxLayout(central_widget)

        self.frame = QFrame(self)
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setStyleSheet("border: 1px solid DarkMagenta;")

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
        self.btn_somar.clicked.connect(self.ClickedButtonSomar)
        self.btn_subtrair.clicked.connect(self.ClickedButtonSubtrair)
        self.btn_dividir.clicked.connect(self.ClickedButtonDividir)


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


########## Multiplicando ###########

    def ClickedButtonMultiplicar(self):

            self.list_values.append(self.inp_result.text())
            self.value12 = int(self.inp_result.text())

            self.lbl_valorantigo = QLabel(f"{self.value12}"+" X", self)

            self.inp_result.clear()

            self.frame_resultado_container.addWidget(self.lbl_valorantigo)
            self.frame_resultado_container.addWidget(self.inp_result)
            
            print(self.list_values) #Print valor atuais na lista 

            self.btn_Calcular.clicked.connect(self.ClickedButtonCalcularM)

    def ClickedButtonCalcularM(self):
        try:   
            self.value2 = int(self.inp_result.text())
        except:
            pass

        result_Multiplicacao = str(Multiplicando(self.value2, self.value12))
        self.lbl_valorantigo.clear()
        self.lbl_valorantigo.setText(result_Multiplicacao)
        self.inp_result.clear()
        self.list_values.clear()


########## Somando ###########

    def ClickedButtonSomar(self):

            self.list_values.append(self.inp_result.text())
            self.value10 = int(self.inp_result.text())

            self.lbl_valorantigo = QLabel(f"{self.value10}"+" +", self)

            self.inp_result.clear()

            self.frame_resultado_container.addWidget(self.lbl_valorantigo)
            self.frame_resultado_container.addWidget(self.inp_result)
            
            print(self.list_values) #Print valor atuais na lista 

            self.btn_Calcular.clicked.connect(self.ClickedButtonCalcularSomar)

    def ClickedButtonCalcularSomar(self):
        try:   
            self.value2 = int(self.inp_result.text())
        except:
            pass

        self.result_Somando = str(Somando(self.value2, self.value10))
        self.lbl_valorantigo.clear()
        self.lbl_valorantigo.setText(self.result_Somando)
        self.inp_result.clear()
        self.list_values.clear()


########## Subtraindo ###########
    
    def ClickedButtonSubtrair(self):

            self.list_values.append(self.inp_result.text())
            self.value11 = int(self.inp_result.text())

            self.lbl_valorantigo = QLabel(f"{self.value11}"+" -", self)

            self.inp_result.clear()

            self.frame_resultado_container.addWidget(self.lbl_valorantigo)
            self.frame_resultado_container.addWidget(self.inp_result)
            
            print(self.list_values) #Print valor atuais na lista 

            self.btn_Calcular.clicked.connect(self.ClickedButtonCalcularSubtrair)

    def ClickedButtonCalcularSubtrair(self):
        try:   
            self.value2 = int(self.inp_result.text())
        except:
            pass

        self.result_Somando = str(Subtrair(self.value2, self.value11))
        self.lbl_valorantigo.clear()
        self.lbl_valorantigo.setText(self.result_Somando)
        self.inp_result.clear()
        # self.lbl_valorantigo.clear()


########## Dividindo ###########

    def ClickedButtonDividir(self):

            self.list_values.append(self.inp_result.text())
            self.value7 = int(self.inp_result.text())

            self.lbl_valorantigo = QLabel(f"{self.value7}"+" /", self)

            self.inp_result.clear()

            self.frame_resultado_container.addWidget(self.lbl_valorantigo)
            self.frame_resultado_container.addWidget(self.inp_result)
            
            print(self.list_values) #Print valor atuais na lista 

            self.btn_Calcular.clicked.connect(self.ClickedButtonCalcularDividir)

    def ClickedButtonCalcularDividir(self):
        try:   
            self.value2 = int(self.inp_result.text())
        except:
            pass

        self.TestingRequerimento()
        self.result_Somando = str(Dividindo(self.value2, self.value7))
        self.lbl_valorantigo.clear()
        self.lbl_valorantigo.setText(self.result_Somando)
        self.inp_result.clear()
        # self.lbl_valorantigo.clear()

################################

    def TestingRequerimento(self):
        for i in self.inp_result.text():
            for j in str(self.Requerimento):      
                print(i)
                print(type(j))
                if i == j:
                     pass

    def Requerimento(self):
        return ["X", "/", "+", "-"]
          