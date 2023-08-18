# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'arquivo.ui'
##
## Created by: Qt User Interface Compiler version 6.5.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QLineEdit,
    QMainWindow, QSizePolicy, QVBoxLayout, QWidget)
import image_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(651, 804)
        MainWindow.setStyleSheet(u"background-color: rgb(0, 198, 159);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_4 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.QPixmap_login = QLabel(self.centralwidget)
        self.QPixmap_login.setObjectName(u"QPixmap_login")
        self.QPixmap_login.setEnabled(True)
        self.QPixmap_login.setPixmap(QPixmap(u":/image_One/pexels-photo-3687770.jpeg"))
        self.QPixmap_login.setScaledContents(True)
        self.QPixmap_login.setMargin(-61)

        self.verticalLayout_4.addWidget(self.QPixmap_login)

        self.QFrame_Login = QFrame(self.centralwidget)
        self.QFrame_Login.setObjectName(u"QFrame_Login")
        self.QFrame_Login.setFrameShape(QFrame.StyledPanel)
        self.QFrame_Login.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.QFrame_Login)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.QFrame_Usuario = QFrame(self.QFrame_Login)
        self.QFrame_Usuario.setObjectName(u"QFrame_Usuario")
        self.QFrame_Usuario.setFrameShape(QFrame.StyledPanel)
        self.QFrame_Usuario.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.QFrame_Usuario)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.Qlabel_Usuario = QLabel(self.QFrame_Usuario)
        self.Qlabel_Usuario.setObjectName(u"Qlabel_Usuario")
        font = QFont()
        font.setPointSize(16)
        self.Qlabel_Usuario.setFont(font)

        self.verticalLayout.addWidget(self.Qlabel_Usuario)

        self.Qline_Usuario = QLineEdit(self.QFrame_Usuario)
        self.Qline_Usuario.setObjectName(u"Qline_Usuario")
        self.Qline_Usuario.setEchoMode(QLineEdit.Normal)

        self.verticalLayout.addWidget(self.Qline_Usuario)


        self.verticalLayout_3.addWidget(self.QFrame_Usuario)

        self.QFrame_Senha = QFrame(self.QFrame_Login)
        self.QFrame_Senha.setObjectName(u"QFrame_Senha")
        self.QFrame_Senha.setFrameShape(QFrame.StyledPanel)
        self.QFrame_Senha.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.QFrame_Senha)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.Qlabel_Senha = QLabel(self.QFrame_Senha)
        self.Qlabel_Senha.setObjectName(u"Qlabel_Senha")
        self.Qlabel_Senha.setFont(font)

        self.verticalLayout_2.addWidget(self.Qlabel_Senha)

        self.Qline_Senha = QLineEdit(self.QFrame_Senha)
        self.Qline_Senha.setObjectName(u"Qline_Senha")
        self.Qline_Senha.setEchoMode(QLineEdit.Password)

        self.verticalLayout_2.addWidget(self.Qline_Senha)


        self.verticalLayout_3.addWidget(self.QFrame_Senha)


        self.verticalLayout_4.addWidget(self.QFrame_Login)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.QPixmap_login.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><img src=\":/image_One/pexels-photo-3687770.jpeg\"/></p></body></html>", None))
        self.Qlabel_Usuario.setText(QCoreApplication.translate("MainWindow", u"Usuario", None))
        self.Qline_Usuario.setPlaceholderText(QCoreApplication.translate("MainWindow", u"digite seu usuario:", None))
        self.Qlabel_Senha.setText(QCoreApplication.translate("MainWindow", u"Senha", None))
        self.Qline_Senha.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Digite sua senha:", None))
    # retranslateUi


if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    w = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(w)
    w.show()
    app.exec()