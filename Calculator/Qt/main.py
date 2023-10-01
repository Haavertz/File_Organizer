# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'untitled.ui'
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

class Ui_Project(object):
    def setupUi(self, Project):
        if not Project.objectName():
            Project.setObjectName(u"Project")
        Project.resize(456, 320)
        self.centralwidget = QWidget(Project)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.end = QFrame(self.centralwidget)
        self.end.setObjectName(u"end")
        self.end.setStyleSheet(u"background-color: black;\n"
"")
        self.end.setFrameShape(QFrame.StyledPanel)
        self.end.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.end)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame_2 = QFrame(self.end)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setStyleSheet(u"background-color: white;\n"
"")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label = QLabel(self.frame_2)
        self.label.setObjectName(u"label")

        self.verticalLayout_2.addWidget(self.label)

        self.line = QFrame(self.frame_2)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.VLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_2.addWidget(self.line)

        self.lineEdit = QLineEdit(self.frame_2)
        self.lineEdit.setObjectName(u"lineEdit")

        self.verticalLayout_2.addWidget(self.lineEdit)


        self.verticalLayout.addWidget(self.frame_2)

        self.frame = QFrame(self.end)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.pushButton_5 = QPushButton(self.frame)
        self.pushButton_5.setObjectName(u"pushButton_5")
        sizePolicy = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(38)
        sizePolicy.setVerticalStretch(12)
        sizePolicy.setHeightForWidth(self.pushButton_5.sizePolicy().hasHeightForWidth())
        self.pushButton_5.setSizePolicy(sizePolicy)
        self.pushButton_5.setMinimumSize(QSize(0, 0))
        self.pushButton_5.setSizeIncrement(QSize(0, 0))
        self.pushButton_5.setBaseSize(QSize(0, 0))
        font = QFont()
        font.setPointSize(8)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setStyleSheet(u"background-color: white;\n"
"")

        self.horizontalLayout_2.addWidget(self.pushButton_5)

        self.pushButton_3 = QPushButton(self.frame)
        self.pushButton_3.setObjectName(u"pushButton_3")
        sizePolicy1 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.pushButton_3.sizePolicy().hasHeightForWidth())
        self.pushButton_3.setSizePolicy(sizePolicy1)
        self.pushButton_3.setStyleSheet(u"background-color: white;\n"
"")

        self.horizontalLayout_2.addWidget(self.pushButton_3)

        self.pushButton_4 = QPushButton(self.frame)
        self.pushButton_4.setObjectName(u"pushButton_4")
        sizePolicy1.setHeightForWidth(self.pushButton_4.sizePolicy().hasHeightForWidth())
        self.pushButton_4.setSizePolicy(sizePolicy1)
        self.pushButton_4.setStyleSheet(u"background-color: white;\n"
"")

        self.horizontalLayout_2.addWidget(self.pushButton_4)

        self.pushButton_2 = QPushButton(self.frame)
        self.pushButton_2.setObjectName(u"pushButton_2")
        sizePolicy1.setHeightForWidth(self.pushButton_2.sizePolicy().hasHeightForWidth())
        self.pushButton_2.setSizePolicy(sizePolicy1)
        self.pushButton_2.setStyleSheet(u"background-color: white;\n"
"")

        self.horizontalLayout_2.addWidget(self.pushButton_2)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)


        self.verticalLayout.addWidget(self.frame)

        self.pushButton = QPushButton(self.end)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setStyleSheet(u"background-color: white;\n"
"")

        self.verticalLayout.addWidget(self.pushButton)


        self.horizontalLayout.addWidget(self.end)

        Project.setCentralWidget(self.centralwidget)

        self.retranslateUi(Project)

        QMetaObject.connectSlotsByName(Project)
    # setupUi

    def retranslateUi(self, Project):
        Project.setWindowTitle(QCoreApplication.translate("Project", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("Project", u"TextLabel", None))
        self.pushButton_5.setText(QCoreApplication.translate("Project", u"/", None))
        self.pushButton_3.setText(QCoreApplication.translate("Project", u"+", None))
        self.pushButton_4.setText(QCoreApplication.translate("Project", u"-", None))
        self.pushButton_2.setText(QCoreApplication.translate("Project", u"X", None))
        self.pushButton.setText(QCoreApplication.translate("Project", u"Calcular", None))
    # retranslateUi

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    main_window = QMainWindow()
    ui = Ui_Project()
    ui.setupUi(main_window)
    main_window.show()
    sys.exit(app.exec())