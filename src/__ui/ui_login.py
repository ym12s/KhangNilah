# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'login.ui'
##
## Created by: Qt User Interface Compiler version 6.8.2
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1200, 800)
        Form.setStyleSheet(u"QWidget#Form {\n"
"    background: qlineargradient(\n"
"        x1: 0, y1: 0,\n"
"        x2: 1, y2: 1,\n"
"        stop: 0 #2193b0,\n"
"        stop: 0.5 #3498db,\n"
"        stop: 1 #6dd5ed\n"
"    );\n"
"}")
        self.wdLOGIN = QWidget(Form)
        self.wdLOGIN.setObjectName(u"wdLOGIN")
        self.wdLOGIN.setGeometry(QRect(110, 140, 1000, 500))
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.wdLOGIN.sizePolicy().hasHeightForWidth())
        self.wdLOGIN.setSizePolicy(sizePolicy)
        self.wdLOGIN.setMinimumSize(QSize(1000, 500))
        self.wdLOGIN.setMaximumSize(QSize(1200, 500))
        self.wdLOGIN.setStyleSheet(u"QWidget#wdLOGIN {\n"
"    background: qlineargradient(\n"
"        x1: 0, y1: 0,\n"
"        x2: 1, y2: 1,\n"
"        stop: 0 rgba(52, 73, 94, 230),\n"
"        stop: 1 rgba(52, 73, 94, 200)\n"
"    );\n"
"    border-radius: 15px;\n"
"    border: 2px solid rgba(255, 255, 255, 0.1);\n"
"}")
        self.horizontalLayout_19 = QHBoxLayout(self.wdLOGIN)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.horizontalLayout_19.setContentsMargins(40, -1, 20, -1)
        self.widget_108 = QWidget(self.wdLOGIN)
        self.widget_108.setObjectName(u"widget_108")
        sizePolicy.setHeightForWidth(self.widget_108.sizePolicy().hasHeightForWidth())
        self.widget_108.setSizePolicy(sizePolicy)
        self.widget_108.setMinimumSize(QSize(400, 400))
        self.widget_108.setStyleSheet(u"QWidget#widget_108{\n"
"border:none;\n"
"\n"
"background-color:transparent;\n"
"border-right: 1px solid rgb(157, 157, 157);}")
        self.lblLogin = QLabel(self.widget_108)
        self.lblLogin.setObjectName(u"lblLogin")
        self.lblLogin.setGeometry(QRect(40, 130, 321, 81))
        font = QFont()
        font.setFamilies([u"8-bit Arcade In"])
        font.setPointSize(48)
        self.lblLogin.setFont(font)
        self.lblLogin.setStyleSheet(u"\n"
"color: rgb(255, 255, 255);\n"
"border:none;\n"
"\n"
"background-color:transparent;\n"
"")

        self.horizontalLayout_19.addWidget(self.widget_108)

        self.wdLogin = QWidget(self.wdLOGIN)
        self.wdLogin.setObjectName(u"wdLogin")
        sizePolicy.setHeightForWidth(self.wdLogin.sizePolicy().hasHeightForWidth())
        self.wdLogin.setSizePolicy(sizePolicy)
        self.wdLogin.setMinimumSize(QSize(500, 350))
        self.wdLogin.setStyleSheet(u"QWidget#wdLogin {\n"
"    background: qlineargradient(\n"
"        x1: 0, y1: 0,\n"
"        x2: 1, y2: 1,\n"
"        stop: 0 rgba(255, 255, 255, 0.95),\n"
"        stop: 1 rgba(240, 255, 255, 0.9)\n"
"    );\n"
"    border-radius: 15px;\n"
"    border: 1px solid rgba(255, 255, 255, 0.3);\n"
"}")
        self.txtUser = QLineEdit(self.wdLogin)
        self.txtUser.setObjectName(u"txtUser")
        self.txtUser.setGeometry(QRect(150, 90, 211, 41))
        self.txtUser.setStyleSheet(u"QLineEdit#txtUser {\n"
"	color: rgb(65, 66, 63);\n"
"    background-color: transparent;\n"
"	border:none;\n"
"	font: 500 20pt \"8-bit Arcade In\";\n"
"    padding top :10px;\n"
"	text-align: center;\n"
"	  border-bottom: 1px solid rgb(179, 179, 179)\n"
"}\n"
"\n"
"QLineEdit#txtUser:focus {\n"
"    border-color: 1px solid rgb(172,12,32);\n"
"}\n"
"\n"
"QLineEdit#txtUser:hover {\n"
"     border-bottom: 1px solid rgb(9, 117, 167);\n"
"}\n"
"\n"
"QLineEdit:disabled {\n"
"    background-color: rgba(226, 226, 226, 1);\n"
"	color: rgb(0, 0, 0);\n"
"}")
        self.txtUser.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.txtPass = QLineEdit(self.wdLogin)
        self.txtPass.setObjectName(u"txtPass")
        self.txtPass.setGeometry(QRect(150, 150, 211, 41))
        self.txtPass.setStyleSheet(u"QLineEdit#txtPass {\n"
"	color: rgb(65, 66, 63);\n"
"    background-color: transparent;\n"
"	border:none;\n"
"	font: 500 10pt \"8-bit Arcade In\";\n"
"    padding top :10px;\n"
"	text-align: center;\n"
"	  border-bottom: 1px solid rgb(179, 179, 179)\n"
"}\n"
"\n"
"QLineEdit#txtPass:focus {\n"
"    border-bottom: 1px solid rgb(9, 117, 167);\n"
"}\n"
"\n"
"QLineEdit#txtPass:hover {\n"
"     border-bottom: 1px solid rgb(9, 117, 167);\n"
"}\n"
"\n"
"QLineEdit:disabled {\n"
"    background-color: rgba(226, 226, 226, 1);\n"
"	color: rgb(0, 0, 0);\n"
"}")
        self.txtPass.setEchoMode(QLineEdit.EchoMode.Password)
        self.txtPass.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.btnLogin_3 = QPushButton(self.wdLogin)
        self.btnLogin_3.setObjectName(u"btnLogin_3")
        self.btnLogin_3.setGeometry(QRect(170, 240, 161, 41))
        font1 = QFont()
        font1.setFamilies([u"8-bit Arcade In"])
        font1.setPointSize(23)
        font1.setWeight(QFont.Medium)
        font1.setItalic(False)
        self.btnLogin_3.setFont(font1)
        self.btnLogin_3.setStyleSheet(u"QPushButton {\n"
"    background: qlineargradient(\n"
"        x1: 0, y1: 0,\n"
"        x2: 1, y2: 0,\n"
"        stop: 0 #2980b9,\n"
"        stop: 1 #3498db\n"
"    );\n"
"    font: 500 23pt \"8-bit Arcade In\";\n"
"    border-radius: 5px;\n"
"    color: white;\n"
"}\n"
"QPushButton:hover {\n"
"    background: qlineargradient(\n"
"        x1: 0, y1: 0,\n"
"        x2: 1, y2: 0,\n"
"        stop: 0 #27ae60,\n"
"        stop: 1 #2ecc71\n"
"    );\n"
"    color: white;\n"
"}\n"
"QPushButton:pressed {\n"
"    background: qlineargradient(\n"
"        x1: 0, y1: 0,\n"
"        x2: 1, y2: 0,\n"
"        stop: 0 #219a52,\n"
"        stop: 1 #27ae60\n"
"    );\n"
"}")

        self.horizontalLayout_19.addWidget(self.wdLogin)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.lblLogin.setText(QCoreApplication.translate("Form", u"COFFEE MTU", None))
        self.txtUser.setText("")
        self.txtUser.setPlaceholderText(QCoreApplication.translate("Form", u"Username", None))
        self.txtPass.setText("")
        self.txtPass.setPlaceholderText(QCoreApplication.translate("Form", u"************", None))
        self.btnLogin_3.setText(QCoreApplication.translate("Form", u"LOGIN", None))
    # retranslateUi

