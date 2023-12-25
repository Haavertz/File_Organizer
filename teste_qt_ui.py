# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'teste_qt.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QLineEdit, QMainWindow, QPushButton, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)
import icon_rc as icon_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(751, 624)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.fame_total = QFrame(self.centralwidget)
        self.fame_total.setObjectName(u"fame_total")
        self.fame_total.setStyleSheet(u"background-color: rgb(255, 255, 127);")
        self.fame_total.setFrameShape(QFrame.StyledPanel)
        self.fame_total.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.fame_total)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_3)

        self.label_2 = QLabel(self.fame_total)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setPixmap(QPixmap(u":/icons/file-explorer-folder-libraries-icon-18298.png"))

        self.verticalLayout.addWidget(self.label_2, 0, Qt.AlignHCenter)

        self.label = QLabel(self.fame_total)
        self.label.setObjectName(u"label")

        self.verticalLayout.addWidget(self.label, 0, Qt.AlignHCenter)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.frame = QFrame(self.fame_total)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.lineEdit = QLineEdit(self.frame)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setLayoutDirection(Qt.RightToLeft)
        self.lineEdit.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.lineEdit)

        self.btn_abrir = QPushButton(self.frame)
        self.btn_abrir.setObjectName(u"btn_abrir")

        self.horizontalLayout.addWidget(self.btn_abrir)


        self.verticalLayout.addWidget(self.frame)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.pushButton = QPushButton(self.fame_total)
        self.pushButton.setObjectName(u"pushButton")

        self.verticalLayout.addWidget(self.pushButton)


        self.verticalLayout_2.addWidget(self.fame_total)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_2.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"Organizador de Arquivos", None))
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Selecione a pasta", None))
        self.btn_abrir.setText(QCoreApplication.translate("MainWindow", u"Abrir", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Organizar", None))
    # retranslateUi

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)

    w =QMainWindow()
    ui = Ui_MainWindow( )
    ui.setupUi(w)
    w.show()

    app.exec()