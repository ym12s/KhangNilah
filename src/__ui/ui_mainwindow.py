# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QComboBox, QFrame,
    QHBoxLayout, QHeaderView, QLabel, QLineEdit,
    QMainWindow, QPushButton, QScrollArea, QSizePolicy,
    QSpacerItem, QSpinBox, QStackedWidget, QTableView,
    QTextBrowser, QVBoxLayout, QWidget)
import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setWindowModality(Qt.WindowModality.ApplicationModal)
        MainWindow.resize(1400, 793)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(0, 720))
        MainWindow.setMaximumSize(QSize(16777215, 16777215))
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet(u"QMainWindow {\n"
"    background: qlineargradient(\n"
"        x1: 0, y1: 0,\n"
"        x2: 1, y2: 1,\n"
"        stop: 0 #2c3e50,\n"
"        stop: 0.5 #3498db,\n"
"        stop: 1 #2980b9\n"
"    );\n"
"}\n"
"QWidget#centralwidget {\n"
"    background: transparent;\n"
"}\n"
"QWidget#paneleft {\n"
"    background: qlineargradient(\n"
"        x1: 0, y1: 0,\n"
"        x2: 1, y2: 0,\n"
"        stop: 0 rgba(44, 62, 80, 240),\n"
"        stop: 1 rgba(44, 62, 80, 220)\n"
"    );\n"
"    border-radius: 10px;\n"
"}\n"
"QWidget#wdbtn {\n"
"    background: transparent;\n"
"}\n"
"QWidget#wdtile {\n"
"    background: rgba(52, 152, 219, 0.3);\n"
"    border-radius: 10px;\n"
"}\n"
"QWidget#wdtool {\n"
"    background: rgba(41, 128, 185, 0.3);\n"
"    border-radius: 10px;\n"
"}\n"
"QWidget#WgPWG {\n"
"    background: rgba(255, 255, 255, 0.95);\n"
"    border-radius: 15px;\n"
"}\n"
"QWidget#wgThanhToan {\n"
"    background: qlineargradient(\n"
"        x1: 0, y1: 0,\n"
"        x2: 1, y2: 1,\n"
"        stop: 0 rgba(44, "
                        "62, 80, 0.95),\n"
"        stop: 1 rgba(52, 152, 219, 0.95)\n"
"    );\n"
"    border-radius: 10px;\n"
"}\n"
"\n"
"QLabel {\n"
"    color: white;\n"
"}\n"
"QLineEdit {\n"
"    background: rgba(255, 255, 255, 0.8);\n"
"    border-radius: 5px;\n"
"    padding: 5px;\n"
"}\n"
"QComboBox {\n"
"    background: rgba(255, 255, 255, 0.8);\n"
"    border-radius: 5px;\n"
"    padding: 5px;\n"
"}\n"
"QSpinBox {\n"
"    background: rgba(255, 255, 255, 0.8);\n"
"    border-radius: 5px;\n"
"    padding: 5px;\n"
"}\n"
"QTableView {\n"
"    background: rgba(255, 255, 255, 0.95);\n"
"    border-radius: 10px;\n"
"}\n"
"QScrollArea {\n"
"    background: transparent;\n"
"}\n"
"QScrollArea > QWidget > QWidget {\n"
"    background: transparent;\n"
"}\n"
"QScrollBar:vertical {\n"
"    background: rgba(255, 255, 255, 0.1);\n"
"    width: 10px;\n"
"    border-radius: 5px;\n"
"}\n"
"QScrollBar::handle:vertical {\n"
"    background: rgba(52, 152, 219, 0.5);\n"
"    border-radius: 5px;\n"
"}\n"
"QScrollBar::add-line:vertical, QScrollBar::"
                        "sub-line:vertical {\n"
"    height: 0px;\n"
"}\n"
"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setMinimumSize(QSize(1400, 600))
        self.horizontalLayout_18 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.paneleft = QWidget(self.centralwidget)
        self.paneleft.setObjectName(u"paneleft")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.paneleft.sizePolicy().hasHeightForWidth())
        self.paneleft.setSizePolicy(sizePolicy1)
        self.paneleft.setMinimumSize(QSize(200, 800))
        self.paneleft.setMaximumSize(QSize(250, 16777215))
        self.paneleft.setStyleSheet(u"QWidget#paneleft{\n"
"background-color:\n"
"transparent;\n"
"}\n"
"")
        self.verticalLayout_38 = QVBoxLayout(self.paneleft)
        self.verticalLayout_38.setObjectName(u"verticalLayout_38")
        self.wdtile = QWidget(self.paneleft)
        self.wdtile.setObjectName(u"wdtile")
        self.wdtile.setStyleSheet(u"QWidget#wdtile{\n"
"background-color: rgb(65, 66, 63);\n"
"border-radius: 15px;\n"
"}\n"
"")
        self.wg511 = QWidget(self.wdtile)
        self.wg511.setObjectName(u"wg511")
        self.wg511.setGeometry(QRect(30, 30, 120, 120))
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.wg511.sizePolicy().hasHeightForWidth())
        self.wg511.setSizePolicy(sizePolicy2)
        self.wg511.setMinimumSize(QSize(120, 120))
        self.wg511.setMaximumSize(QSize(120, 120))
        self.wg511.setStyleSheet(u"background-color:transparent;\n"
"border-radius:60px;")
        self.label_11 = QLabel(self.wdtile)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(40, 180, 101, 20))
        self.label_11.setStyleSheet(u"font: 700 13pt \"Sontay\";\n"
"background:transparent;\n"
"")

        self.verticalLayout_38.addWidget(self.wdtile)

        self.wdbtn = QWidget(self.paneleft)
        self.wdbtn.setObjectName(u"wdbtn")
        self.wdbtn.setStyleSheet(u"QWidget#wdbtn{\n"
"background-color: rgb(65, 66, 63);\n"
"border-radius: 15px;\n"
"}\n"
"")
        self.btnMenu = QPushButton(self.wdbtn)
        self.btnMenu.setObjectName(u"btnMenu")
        self.btnMenu.setGeometry(QRect(21, 20, 161, 41))
        font = QFont()
        font.setFamilies([u"Sontay"])
        font.setPointSize(13)
        font.setBold(True)
        font.setItalic(False)
        self.btnMenu.setFont(font)
        self.btnMenu.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.btnMenu.setAutoFillBackground(False)
        self.btnMenu.setStyleSheet(u"QPushButton#btnMenu {\n"
"                background-color: rgb(65, 66, 63);\n"
"                text-align: left;\n"
"                padding-bottom: 4px;\n"
"                font: 700 13pt \"Sontay\";\n"
"                padding-left: 15px;\n"
"border:none\n"
"    }\n"
"            QPushButton#btnMenu:hover {\n"
"                border-right: 1px solid rgb(239, 50, 104); \n"
"                color: white;\n"
"            }\n"
"            QPushButton#btnMenu:checked {\n"
"                color: white;\n"
"                border-right: 1px solid rgb(239, 50, 104); \n"
"                background-color: rgb(65, 66, 63);\n"
"            }\n"
"        ")
        icon = QIcon()
        icon.addFile(u":/src/ass/icon/homeWhite.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnMenu.setIcon(icon)
        self.btnMenu.setIconSize(QSize(25, 25))
        self.btnMenu.setCheckable(False)
        self.btnOrder = QPushButton(self.wdbtn)
        self.btnOrder.setObjectName(u"btnOrder")
        self.btnOrder.setGeometry(QRect(20, 80, 161, 41))
        self.btnOrder.setFont(font)
        self.btnOrder.setStyleSheet(u"QPushButton#btnOrder {\n"
"                background-color: rgb(65, 66, 63);\n"
"                text-align: left;\n"
"                padding-bottom: 4px;\n"
"                font: 700 13pt \"Sontay\";\n"
"                padding-left: 15px;\n"
"border:none\n"
"    }\n"
"            QPushButton#btnOrder:hover {\n"
"                border-right: 1px solid rgb(239, 50, 104); \n"
"                color: white;\n"
"            }\n"
"            QPushButton#btnOrder:checked {\n"
"                color: white;\n"
"                border-right: 1px solid rgb(239, 50, 104); \n"
"                background-color: rgb(65, 66, 63);\n"
"            }\n"
"        ")
        icon1 = QIcon()
        icon1.addFile(u":/src/ass/icon/shopping-cart.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.btnOrder.setIcon(icon1)
        self.btnOrder.setIconSize(QSize(25, 30))
        self.btnOrder.setCheckable(False)
        self.btnAI = QPushButton(self.wdbtn)
        self.btnAI.setObjectName(u"btnAI")
        self.btnAI.setGeometry(QRect(20, 140, 161, 41))
        self.btnAI.setFont(font)
        self.btnAI.setStyleSheet(u"QPushButton#btnAI {\n"
"                background-color: rgb(65, 66, 63);\n"
"                text-align: left;\n"
"                padding-bottom: 4px;\n"
"                font: 700 13pt \"Sontay\";\n"
"                padding-left: 15px;\n"
"border:none\n"
"    }\n"
"            QPushButton#btnAI:hover {\n"
"                border-right: 1px solid rgb(239, 50, 104); \n"
"                color: white;\n"
"            }\n"
"            QPushButton#btnAI:checked {\n"
"                color: white;\n"
"                border-right: 1px solid rgb(239, 50, 104); \n"
"               background-color: rgb(65, 66, 63);\n"
"            }\n"
"        ")
        icon2 = QIcon()
        icon2.addFile(u":/src/ass/icon/AIWhite.png.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.btnAI.setIcon(icon2)
        self.btnAI.setIconSize(QSize(25, 30))
        self.btnAdmin = QPushButton(self.wdbtn)
        self.btnAdmin.setObjectName(u"btnAdmin")
        self.btnAdmin.setGeometry(QRect(20, 200, 161, 41))
        self.btnAdmin.setFont(font)
        self.btnAdmin.setStyleSheet(u"QPushButton#btnAdmin {\n"
"                background-color: rgb(65, 66, 63);\n"
"                text-align: left;\n"
"                padding-bottom: 4px;\n"
"                font: 700 13pt \"Sontay\";\n"
"                padding-left: 15px;\n"
"border:none\n"
"    }\n"
"            QPushButton#btnAdmin:hover {\n"
"                border-right: 1px solid rgb(239, 50, 104); \n"
"                color: white;\n"
"            }\n"
"            QPushButton#btnAdmin:checked {\n"
"                color: white;\n"
"                border-right: 1px solid rgb(239, 50, 104); \n"
"               background-color: rgb(65, 66, 63);\n"
"            }\n"
"        ")
        icon3 = QIcon()
        icon3.addFile(u":/src/ass/icon/user-gearWhite.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnAdmin.setIcon(icon3)
        self.btnAdmin.setIconSize(QSize(25, 30))

        self.verticalLayout_38.addWidget(self.wdbtn)

        self.wdtool = QWidget(self.paneleft)
        self.wdtool.setObjectName(u"wdtool")
        self.wdtool.setStyleSheet(u"QWidget#wdtool{\n"
"background-color: rgb(65, 66, 63);\n"
"border-radius: 15px;\n"
"}\n"
"")
        self.label_2 = QLabel(self.wdtool)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(30, 200, 25, 25))
        self.label_2.setStyleSheet(u"background-color: transparent")
        self.label_2.setTextFormat(Qt.TextFormat.MarkdownText)
        self.label_2.setPixmap(QPixmap(u":/src/ass/icon/github (1).png"))
        self.label_2.setScaledContents(True)
        self.label_5 = QLabel(self.wdtool)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(30, 140, 25, 25))
        self.label_5.setStyleSheet(u"background-color: transparent")
        self.label_5.setTextFormat(Qt.TextFormat.MarkdownText)
        self.label_5.setPixmap(QPixmap(u":/src/ass/icon/python (1).png"))
        self.label_5.setScaledContents(True)
        self.label_6 = QLabel(self.wdtool)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(30, 80, 25, 25))
        self.label_6.setStyleSheet(u"background-color: transparent")
        self.label_6.setTextFormat(Qt.TextFormat.MarkdownText)
        self.label_6.setPixmap(QPixmap(u":/src/ass/icon/visual-basic.png"))
        self.label_6.setScaledContents(True)
        self.label_7 = QLabel(self.wdtool)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(30, 20, 25, 25))
        self.label_7.setStyleSheet(u"background-color: transparent")
        self.label_7.setTextFormat(Qt.TextFormat.MarkdownText)
        self.label_7.setPixmap(QPixmap(u":/src/ass/icon/pinterest.png"))
        self.label_7.setScaledContents(True)
        self.label_3 = QLabel(self.wdtool)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(75, 20, 91, 20))
        self.label_3.setStyleSheet(u"font: 700 13pt \"Sontay\";\n"
"background:transparent;\n"
"")
        self.label_8 = QLabel(self.wdtool)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(75, 80, 91, 20))
        self.label_8.setStyleSheet(u"font: 700 13pt \"Sontay\";\n"
"background:transparent;\n"
"")
        self.label_9 = QLabel(self.wdtool)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(75, 140, 91, 20))
        self.label_9.setStyleSheet(u"font: 700 13pt \"Sontay\";\n"
"background:transparent;\n"
"")
        self.label_10 = QLabel(self.wdtool)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(75, 200, 91, 20))
        self.label_10.setStyleSheet(u"font: 700 13pt \"Sontay\";\n"
"background:transparent;\n"
"")

        self.verticalLayout_38.addWidget(self.wdtool)


        self.horizontalLayout_18.addWidget(self.paneleft)

        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setMinimumSize(QSize(0, 720))
        self.stackedWidget.setMaximumSize(QSize(16777215, 1200))
        self.stackedWidget.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.stackedWidget.setStyleSheet(u"background-color: transparent;\n"
"")
        self.pageMenu = QWidget()
        self.pageMenu.setObjectName(u"pageMenu")
        self.verticalLayout_4 = QVBoxLayout(self.pageMenu)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.widget = QWidget(self.pageMenu)
        self.widget.setObjectName(u"widget")
        self.widget.setStyleSheet(u"")
        self.verticalLayout = QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(-1, 0, -1, -1)
        self.widget_2 = QWidget(self.widget)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setMinimumSize(QSize(1000, 70))
        self.widget_2.setMaximumSize(QSize(180, 70))
        self.widget_2.setStyleSheet(u"")
        self.lblWelcome = QLabel(self.widget_2)
        self.lblWelcome.setObjectName(u"lblWelcome")
        self.lblWelcome.setGeometry(QRect(10, 0, 861, 41))
        font1 = QFont()
        font1.setFamilies([u"8-bit Arcade In"])
        font1.setPointSize(40)
        font1.setWeight(QFont.Medium)
        font1.setItalic(False)
        font1.setUnderline(False)
        font1.setStrikeOut(False)
        font1.setKerning(True)
        font1.setStyleStrategy(QFont.PreferAntialias)
        font1.setHintingPreference(QFont.PreferDefaultHinting)
        self.lblWelcome.setFont(font1)
        self.lblWelcome.setStyleSheet(u"color: white;\n"
"border: none;\n"
"font: 500 40pt \"8-bit Arcade In\";")
        self.lblWelcome.setTextFormat(Qt.TextFormat.PlainText)
        self.lblWelcome.setScaledContents(False)
        self.lblWelcome.setWordWrap(False)
        self.lblWelcome.setOpenExternalLinks(False)
        self.lbWelCome = QLabel(self.widget_2)
        self.lbWelCome.setObjectName(u"lbWelCome")
        self.lbWelCome.setGeometry(QRect(10, 40, 271, 31))
        font2 = QFont()
        font2.setFamilies([u"System"])
        font2.setPointSize(9)
        font2.setBold(True)
        font2.setItalic(False)
        self.lbWelCome.setFont(font2)
        self.lbWelCome.setStyleSheet(u"border: none;\n"
"color: white;")
        self.lbWelCome.setTextFormat(Qt.TextFormat.PlainText)
        self.lbWelCome.setScaledContents(False)
        self.lbWelCome.setWordWrap(False)
        self.lbWelCome.setOpenExternalLinks(False)

        self.verticalLayout.addWidget(self.widget_2, 0, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignTop)

        self.widget_66 = QWidget(self.widget)
        self.widget_66.setObjectName(u"widget_66")
        self.widget_66.setStyleSheet(u"border-bottom: 1px solid rgb(65, 66, 63)")

        self.verticalLayout.addWidget(self.widget_66)

        self.scrollMenu = QScrollArea(self.widget)
        self.scrollMenu.setObjectName(u"scrollMenu")
        self.scrollMenu.setStyleSheet(u"border:none;")
        self.scrollMenu.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.scrollMenu.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.scrollMenu.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 1140, 6744))
        self.scrollAreaWidgetContents.setStyleSheet(u"border:none;")
        self.verticalLayout_3 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.wdPicMenu = QWidget(self.scrollAreaWidgetContents)
        self.wdPicMenu.setObjectName(u"wdPicMenu")
        sizePolicy1.setHeightForWidth(self.wdPicMenu.sizePolicy().hasHeightForWidth())
        self.wdPicMenu.setSizePolicy(sizePolicy1)
        self.wdPicMenu.setMinimumSize(QSize(900, 0))
        self.wdPicMenu.setMaximumSize(QSize(900, 16777215))
        self.wdPicMenu.setStyleSheet(u"background-color: transparent;")
        self.verticalLayout_6 = QVBoxLayout(self.wdPicMenu)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.wg1 = QWidget(self.wdPicMenu)
        self.wg1.setObjectName(u"wg1")
        self.wg1.setMinimumSize(QSize(550, 400))
        self.wg1.setStyleSheet(u"background-color: transparent;")
        self.horizontalLayout_12 = QHBoxLayout(self.wg1)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.ww_2 = QWidget(self.wg1)
        self.ww_2.setObjectName(u"ww_2")
        self.ww_2.setStyleSheet(u"background-color: transparent;")
        self.verticalLayout_5 = QVBoxLayout(self.ww_2)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.wb1 = QWidget(self.ww_2)
        self.wb1.setObjectName(u"wb1")
        sizePolicy2.setHeightForWidth(self.wb1.sizePolicy().hasHeightForWidth())
        self.wb1.setSizePolicy(sizePolicy2)
        self.wb1.setMinimumSize(QSize(220, 200))
        self.wb1.setMaximumSize(QSize(220, 200))
        self.wb1.setStyleSheet(u"background-color:transparent;")

        self.verticalLayout_5.addWidget(self.wb1, 0, Qt.AlignmentFlag.AlignHCenter)

        self.widget_4 = QWidget(self.ww_2)
        self.widget_4.setObjectName(u"widget_4")
        self.btnAdd1 = QPushButton(self.widget_4)
        self.btnAdd1.setObjectName(u"btnAdd1")
        self.btnAdd1.setGeometry(QRect(60, 100, 151, 51))
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.btnAdd1.sizePolicy().hasHeightForWidth())
        self.btnAdd1.setSizePolicy(sizePolicy3)
        font3 = QFont()
        font3.setPointSize(15)
        font3.setBold(True)
        self.btnAdd1.setFont(font3)
        self.btnAdd1.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btnAdd1.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(255, 255, 255);\n"
"border-radius: 8px;\n"
"	color: rgb(65, 66, 63);\n"
"}\n"
"QPushButton:hover{\n"
"background-color:#4CAF50;\n"
"    color: white;\n"
"}\n"
"")
        self.lblCost1 = QLabel(self.widget_4)
        self.lblCost1.setObjectName(u"lblCost1")
        self.lblCost1.setGeometry(QRect(0, 5, 261, 81))
        font4 = QFont()
        font4.setFamilies([u"Segoe UI"])
        font4.setBold(True)
        font4.setHintingPreference(QFont.PreferFullHinting)
        self.lblCost1.setFont(font4)
        self.lblCost1.setStyleSheet(u"color: white;\n"
"text-align: center;\n"
"padding-left:10px;\n"
"font-size: 20px;")
        self.lblCost1.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_5.addWidget(self.widget_4)


        self.horizontalLayout_12.addWidget(self.ww_2)

        self.widget_5 = QWidget(self.wg1)
        self.widget_5.setObjectName(u"widget_5")
        self.verticalLayout_11 = QVBoxLayout(self.widget_5)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.wb2 = QWidget(self.widget_5)
        self.wb2.setObjectName(u"wb2")
        sizePolicy2.setHeightForWidth(self.wb2.sizePolicy().hasHeightForWidth())
        self.wb2.setSizePolicy(sizePolicy2)
        self.wb2.setMinimumSize(QSize(220, 200))
        self.wb2.setMaximumSize(QSize(220, 200))
        self.wb2.setStyleSheet(u"background-color:transparent;")

        self.verticalLayout_11.addWidget(self.wb2, 0, Qt.AlignmentFlag.AlignHCenter)

        self.widget_9 = QWidget(self.widget_5)
        self.widget_9.setObjectName(u"widget_9")
        self.btnAdd2 = QPushButton(self.widget_9)
        self.btnAdd2.setObjectName(u"btnAdd2")
        self.btnAdd2.setGeometry(QRect(60, 100, 151, 51))
        sizePolicy3.setHeightForWidth(self.btnAdd2.sizePolicy().hasHeightForWidth())
        self.btnAdd2.setSizePolicy(sizePolicy3)
        self.btnAdd2.setFont(font3)
        self.btnAdd2.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btnAdd2.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(255, 255, 255);\n"
"border-radius: 8px;\n"
"	color: rgb(65, 66, 63);\n"
"t\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(239, 50, 104); \n"
"    color: white;\n"
"}\n"
"QPushButton:checked{\n"
" background-color: rgb(239, 50, 104);\n"
" color: white;\n"
"}")
        self.lblCost2 = QLabel(self.widget_9)
        self.lblCost2.setObjectName(u"lblCost2")
        self.lblCost2.setGeometry(QRect(0, 5, 260, 81))
        self.lblCost2.setFont(font4)
        self.lblCost2.setStyleSheet(u"color: white;\n"
"text-align: center;\n"
"padding-left:10px;\n"
"font-size: 20px;")
        self.lblCost2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_11.addWidget(self.widget_9)


        self.horizontalLayout_12.addWidget(self.widget_5)

        self.ww = QWidget(self.wg1)
        self.ww.setObjectName(u"ww")
        self.verticalLayout_12 = QVBoxLayout(self.ww)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.wb3 = QWidget(self.ww)
        self.wb3.setObjectName(u"wb3")
        sizePolicy2.setHeightForWidth(self.wb3.sizePolicy().hasHeightForWidth())
        self.wb3.setSizePolicy(sizePolicy2)
        self.wb3.setMinimumSize(QSize(220, 200))
        self.wb3.setMaximumSize(QSize(220, 200))
        self.wb3.setStyleSheet(u"background-color:transparent;")

        self.verticalLayout_12.addWidget(self.wb3, 0, Qt.AlignmentFlag.AlignHCenter)

        self.widget_13 = QWidget(self.ww)
        self.widget_13.setObjectName(u"widget_13")
        self.btnAdd3 = QPushButton(self.widget_13)
        self.btnAdd3.setObjectName(u"btnAdd3")
        self.btnAdd3.setGeometry(QRect(60, 100, 151, 51))
        sizePolicy3.setHeightForWidth(self.btnAdd3.sizePolicy().hasHeightForWidth())
        self.btnAdd3.setSizePolicy(sizePolicy3)
        self.btnAdd3.setFont(font3)
        self.btnAdd3.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btnAdd3.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(255, 255, 255);\n"
"border-radius: 8px;\n"
"	color: rgb(65, 66, 63);\n"
"t\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(239, 50, 104); \n"
"    color: white;\n"
"}\n"
"QPushButton:checked{\n"
" background-color: rgb(239, 50, 104);\n"
" color: white;\n"
"}")
        self.lblCost3 = QLabel(self.widget_13)
        self.lblCost3.setObjectName(u"lblCost3")
        self.lblCost3.setGeometry(QRect(10, 10, 261, 76))
        self.lblCost3.setFont(font4)
        self.lblCost3.setStyleSheet(u"color: white;\n"
"text-align: center;\n"
"\n"
"font-size: 20px;")
        self.lblCost3.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_12.addWidget(self.widget_13)


        self.horizontalLayout_12.addWidget(self.ww)


        self.verticalLayout_6.addWidget(self.wg1)

        self.verticalSpacer_5 = QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_6.addItem(self.verticalSpacer_5)

        self.wg2 = QWidget(self.wdPicMenu)
        self.wg2.setObjectName(u"wg2")
        self.wg2.setMinimumSize(QSize(550, 400))
        self.wg2.setMaximumSize(QSize(16777215, 400))
        self.wg2.setStyleSheet(u"")
        self.horizontalLayout = QHBoxLayout(self.wg2)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.widget_47 = QWidget(self.wg2)
        self.widget_47.setObjectName(u"widget_47")
        self.verticalLayout_33 = QVBoxLayout(self.widget_47)
        self.verticalLayout_33.setObjectName(u"verticalLayout_33")
        self.wb4 = QWidget(self.widget_47)
        self.wb4.setObjectName(u"wb4")
        sizePolicy2.setHeightForWidth(self.wb4.sizePolicy().hasHeightForWidth())
        self.wb4.setSizePolicy(sizePolicy2)
        self.wb4.setMinimumSize(QSize(220, 200))
        self.wb4.setMaximumSize(QSize(220, 200))
        self.wb4.setStyleSheet(u"background-color:transparent;")

        self.verticalLayout_33.addWidget(self.wb4, 0, Qt.AlignmentFlag.AlignHCenter)

        self.widget_57 = QWidget(self.widget_47)
        self.widget_57.setObjectName(u"widget_57")
        self.btnAdd4 = QPushButton(self.widget_57)
        self.btnAdd4.setObjectName(u"btnAdd4")
        self.btnAdd4.setGeometry(QRect(60, 100, 151, 51))
        sizePolicy3.setHeightForWidth(self.btnAdd4.sizePolicy().hasHeightForWidth())
        self.btnAdd4.setSizePolicy(sizePolicy3)
        self.btnAdd4.setFont(font3)
        self.btnAdd4.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btnAdd4.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(255, 255, 255);\n"
"border-radius: 8px;\n"
"	color: rgb(65, 66, 63);\n"
"t\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(239, 50, 104); \n"
"    color: white;\n"
"}\n"
"QPushButton:checked{\n"
" background-color: rgb(239, 50, 104);\n"
" color: white;\n"
"}")
        self.lblCost4 = QLabel(self.widget_57)
        self.lblCost4.setObjectName(u"lblCost4")
        self.lblCost4.setGeometry(QRect(30, 10, 211, 76))
        self.lblCost4.setFont(font4)
        self.lblCost4.setStyleSheet(u"color: white;\n"
"text-align: center;\n"
"padding-left:10px;\n"
"font-size: 20px;")
        self.lblCost4.setFrameShadow(QFrame.Shadow.Plain)
        self.lblCost4.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_33.addWidget(self.widget_57)


        self.horizontalLayout.addWidget(self.widget_47)

        self.widget_60 = QWidget(self.wg2)
        self.widget_60.setObjectName(u"widget_60")
        self.verticalLayout_35 = QVBoxLayout(self.widget_60)
        self.verticalLayout_35.setObjectName(u"verticalLayout_35")
        self.wb5 = QWidget(self.widget_60)
        self.wb5.setObjectName(u"wb5")
        sizePolicy2.setHeightForWidth(self.wb5.sizePolicy().hasHeightForWidth())
        self.wb5.setSizePolicy(sizePolicy2)
        self.wb5.setMinimumSize(QSize(220, 200))
        self.wb5.setMaximumSize(QSize(220, 200))
        self.wb5.setStyleSheet(u"background-color:transparent;")

        self.verticalLayout_35.addWidget(self.wb5, 0, Qt.AlignmentFlag.AlignHCenter)

        self.widget_61 = QWidget(self.widget_60)
        self.widget_61.setObjectName(u"widget_61")
        self.btnAdd5 = QPushButton(self.widget_61)
        self.btnAdd5.setObjectName(u"btnAdd5")
        self.btnAdd5.setGeometry(QRect(60, 100, 151, 51))
        sizePolicy3.setHeightForWidth(self.btnAdd5.sizePolicy().hasHeightForWidth())
        self.btnAdd5.setSizePolicy(sizePolicy3)
        self.btnAdd5.setFont(font3)
        self.btnAdd5.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btnAdd5.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(255, 255, 255);\n"
"border-radius: 8px;\n"
"	color: rgb(65, 66, 63);\n"
"t\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(239, 50, 104); \n"
"    color: white;\n"
"}\n"
"QPushButton:checked{\n"
" background-color: rgb(239, 50, 104);\n"
" color: white;\n"
"}")
        self.lblCost5 = QLabel(self.widget_61)
        self.lblCost5.setObjectName(u"lblCost5")
        self.lblCost5.setGeometry(QRect(30, 10, 211, 76))
        self.lblCost5.setFont(font4)
        self.lblCost5.setStyleSheet(u"color: white;\n"
"text-align: center;\n"
"padding-left:10px;\n"
"font-size: 20px;")
        self.lblCost5.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_35.addWidget(self.widget_61)


        self.horizontalLayout.addWidget(self.widget_60)

        self.widget_58 = QWidget(self.wg2)
        self.widget_58.setObjectName(u"widget_58")
        self.verticalLayout_34 = QVBoxLayout(self.widget_58)
        self.verticalLayout_34.setObjectName(u"verticalLayout_34")
        self.wb6 = QWidget(self.widget_58)
        self.wb6.setObjectName(u"wb6")
        sizePolicy2.setHeightForWidth(self.wb6.sizePolicy().hasHeightForWidth())
        self.wb6.setSizePolicy(sizePolicy2)
        self.wb6.setMinimumSize(QSize(220, 200))
        self.wb6.setMaximumSize(QSize(220, 200))
        self.wb6.setStyleSheet(u"background-color:transparent;")

        self.verticalLayout_34.addWidget(self.wb6, 0, Qt.AlignmentFlag.AlignHCenter)

        self.widget_59 = QWidget(self.widget_58)
        self.widget_59.setObjectName(u"widget_59")
        self.btnAdd6 = QPushButton(self.widget_59)
        self.btnAdd6.setObjectName(u"btnAdd6")
        self.btnAdd6.setGeometry(QRect(60, 100, 151, 51))
        sizePolicy3.setHeightForWidth(self.btnAdd6.sizePolicy().hasHeightForWidth())
        self.btnAdd6.setSizePolicy(sizePolicy3)
        self.btnAdd6.setFont(font3)
        self.btnAdd6.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btnAdd6.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(255, 255, 255);\n"
"border-radius: 8px;\n"
"	color: rgb(65, 66, 63);\n"
"t\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(239, 50, 104); \n"
"    color: white;\n"
"}\n"
"QPushButton:checked{\n"
" background-color: rgb(239, 50, 104);\n"
" color: white;\n"
"}")
        self.lblCost6 = QLabel(self.widget_59)
        self.lblCost6.setObjectName(u"lblCost6")
        self.lblCost6.setGeometry(QRect(30, 10, 211, 76))
        self.lblCost6.setFont(font4)
        self.lblCost6.setStyleSheet(u"color: white;\n"
"text-align: center;\n"
"padding-left:10px;\n"
"font-size: 20px;")
        self.lblCost6.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_34.addWidget(self.widget_59)


        self.horizontalLayout.addWidget(self.widget_58)


        self.verticalLayout_6.addWidget(self.wg2)

        self.verticalSpacer_10 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_6.addItem(self.verticalSpacer_10)

        self.wg3 = QWidget(self.wdPicMenu)
        self.wg3.setObjectName(u"wg3")
        self.wg3.setMinimumSize(QSize(550, 400))
        self.wg3.setStyleSheet(u"")
        self.horizontalLayout_9 = QHBoxLayout(self.wg3)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.widget_53 = QWidget(self.wg3)
        self.widget_53.setObjectName(u"widget_53")
        self.verticalLayout_31 = QVBoxLayout(self.widget_53)
        self.verticalLayout_31.setObjectName(u"verticalLayout_31")
        self.wb8 = QWidget(self.widget_53)
        self.wb8.setObjectName(u"wb8")
        sizePolicy2.setHeightForWidth(self.wb8.sizePolicy().hasHeightForWidth())
        self.wb8.setSizePolicy(sizePolicy2)
        self.wb8.setMinimumSize(QSize(220, 200))
        self.wb8.setMaximumSize(QSize(220, 200))
        self.wb8.setStyleSheet(u"background-color:transparent;")

        self.verticalLayout_31.addWidget(self.wb8, 0, Qt.AlignmentFlag.AlignHCenter)

        self.widget_54 = QWidget(self.widget_53)
        self.widget_54.setObjectName(u"widget_54")
        self.btnAdd8 = QPushButton(self.widget_54)
        self.btnAdd8.setObjectName(u"btnAdd8")
        self.btnAdd8.setGeometry(QRect(60, 100, 151, 51))
        sizePolicy3.setHeightForWidth(self.btnAdd8.sizePolicy().hasHeightForWidth())
        self.btnAdd8.setSizePolicy(sizePolicy3)
        self.btnAdd8.setFont(font3)
        self.btnAdd8.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btnAdd8.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(255, 255, 255);\n"
"border-radius: 8px;\n"
"	color: rgb(65, 66, 63);\n"
"t\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(239, 50, 104); \n"
"    color: white;\n"
"}\n"
"QPushButton:checked{\n"
" background-color: rgb(239, 50, 104);\n"
" color: white;\n"
"}")
        self.lblCost8 = QLabel(self.widget_54)
        self.lblCost8.setObjectName(u"lblCost8")
        self.lblCost8.setGeometry(QRect(30, 10, 211, 76))
        self.lblCost8.setFont(font4)
        self.lblCost8.setStyleSheet(u"color: white;\n"
"text-align: center;\n"
"padding-left:10px;\n"
"font-size: 20px;")
        self.lblCost8.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_31.addWidget(self.widget_54)


        self.horizontalLayout_9.addWidget(self.widget_53)

        self.widget_55 = QWidget(self.wg3)
        self.widget_55.setObjectName(u"widget_55")
        self.verticalLayout_32 = QVBoxLayout(self.widget_55)
        self.verticalLayout_32.setObjectName(u"verticalLayout_32")
        self.wb7 = QWidget(self.widget_55)
        self.wb7.setObjectName(u"wb7")
        sizePolicy2.setHeightForWidth(self.wb7.sizePolicy().hasHeightForWidth())
        self.wb7.setSizePolicy(sizePolicy2)
        self.wb7.setMinimumSize(QSize(220, 200))
        self.wb7.setMaximumSize(QSize(220, 200))
        self.wb7.setStyleSheet(u"background-color:transparent;")

        self.verticalLayout_32.addWidget(self.wb7, 0, Qt.AlignmentFlag.AlignHCenter)

        self.widget_56 = QWidget(self.widget_55)
        self.widget_56.setObjectName(u"widget_56")
        self.btnAdd7 = QPushButton(self.widget_56)
        self.btnAdd7.setObjectName(u"btnAdd7")
        self.btnAdd7.setGeometry(QRect(60, 100, 151, 51))
        sizePolicy3.setHeightForWidth(self.btnAdd7.sizePolicy().hasHeightForWidth())
        self.btnAdd7.setSizePolicy(sizePolicy3)
        self.btnAdd7.setFont(font3)
        self.btnAdd7.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btnAdd7.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(255, 255, 255);\n"
"border-radius: 8px;\n"
"	color: rgb(65, 66, 63);\n"
"t\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(239, 50, 104); \n"
"    color: white;\n"
"}\n"
"QPushButton:checked{\n"
" background-color: rgb(239, 50, 104);\n"
" color: white;\n"
"}")
        self.lblCost7 = QLabel(self.widget_56)
        self.lblCost7.setObjectName(u"lblCost7")
        self.lblCost7.setGeometry(QRect(30, 10, 211, 76))
        self.lblCost7.setFont(font4)
        self.lblCost7.setStyleSheet(u"color: white;\n"
"text-align: center;\n"
"padding-left:10px;\n"
"font-size: 20px;")
        self.lblCost7.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_32.addWidget(self.widget_56)


        self.horizontalLayout_9.addWidget(self.widget_55)

        self.widget_51 = QWidget(self.wg3)
        self.widget_51.setObjectName(u"widget_51")
        self.verticalLayout_30 = QVBoxLayout(self.widget_51)
        self.verticalLayout_30.setObjectName(u"verticalLayout_30")
        self.wb9 = QWidget(self.widget_51)
        self.wb9.setObjectName(u"wb9")
        sizePolicy2.setHeightForWidth(self.wb9.sizePolicy().hasHeightForWidth())
        self.wb9.setSizePolicy(sizePolicy2)
        self.wb9.setMinimumSize(QSize(220, 200))
        self.wb9.setMaximumSize(QSize(220, 200))
        self.wb9.setStyleSheet(u"background-color:transparent;")

        self.verticalLayout_30.addWidget(self.wb9, 0, Qt.AlignmentFlag.AlignHCenter)

        self.widget_52 = QWidget(self.widget_51)
        self.widget_52.setObjectName(u"widget_52")
        self.btnAdd9 = QPushButton(self.widget_52)
        self.btnAdd9.setObjectName(u"btnAdd9")
        self.btnAdd9.setGeometry(QRect(60, 100, 151, 51))
        sizePolicy3.setHeightForWidth(self.btnAdd9.sizePolicy().hasHeightForWidth())
        self.btnAdd9.setSizePolicy(sizePolicy3)
        self.btnAdd9.setFont(font3)
        self.btnAdd9.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btnAdd9.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(255, 255, 255);\n"
"border-radius: 8px;\n"
"	color: rgb(65, 66, 63);\n"
"t\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(239, 50, 104); \n"
"    color: white;\n"
"}\n"
"QPushButton:checked{\n"
" background-color: rgb(239, 50, 104);\n"
" color: white;\n"
"}")
        self.lblCost9 = QLabel(self.widget_52)
        self.lblCost9.setObjectName(u"lblCost9")
        self.lblCost9.setGeometry(QRect(30, 10, 211, 76))
        self.lblCost9.setFont(font4)
        self.lblCost9.setStyleSheet(u"color: white;\n"
"text-align: center;\n"
"padding-left:10px;\n"
"font-size: 20px;")
        self.lblCost9.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_30.addWidget(self.widget_52)


        self.horizontalLayout_9.addWidget(self.widget_51)


        self.verticalLayout_6.addWidget(self.wg3)

        self.verticalSpacer_11 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_6.addItem(self.verticalSpacer_11)

        self.wg4 = QWidget(self.wdPicMenu)
        self.wg4.setObjectName(u"wg4")
        self.wg4.setMinimumSize(QSize(550, 400))
        self.horizontalLayout_2 = QHBoxLayout(self.wg4)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.widget_49 = QWidget(self.wg4)
        self.widget_49.setObjectName(u"widget_49")
        self.verticalLayout_29 = QVBoxLayout(self.widget_49)
        self.verticalLayout_29.setObjectName(u"verticalLayout_29")
        self.wb10 = QWidget(self.widget_49)
        self.wb10.setObjectName(u"wb10")
        sizePolicy2.setHeightForWidth(self.wb10.sizePolicy().hasHeightForWidth())
        self.wb10.setSizePolicy(sizePolicy2)
        self.wb10.setMinimumSize(QSize(220, 200))
        self.wb10.setMaximumSize(QSize(220, 200))
        self.wb10.setStyleSheet(u"background-color:transparent;")

        self.verticalLayout_29.addWidget(self.wb10, 0, Qt.AlignmentFlag.AlignHCenter)

        self.widget_50 = QWidget(self.widget_49)
        self.widget_50.setObjectName(u"widget_50")
        self.btnAdd10 = QPushButton(self.widget_50)
        self.btnAdd10.setObjectName(u"btnAdd10")
        self.btnAdd10.setGeometry(QRect(60, 100, 151, 51))
        sizePolicy3.setHeightForWidth(self.btnAdd10.sizePolicy().hasHeightForWidth())
        self.btnAdd10.setSizePolicy(sizePolicy3)
        self.btnAdd10.setFont(font3)
        self.btnAdd10.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btnAdd10.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(255, 255, 255);\n"
"border-radius: 8px;\n"
"	color: rgb(65, 66, 63);\n"
"t\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(239, 50, 104); \n"
"    color: white;\n"
"}\n"
"QPushButton:checked{\n"
" background-color: rgb(239, 50, 104);\n"
" color: white;\n"
"}")
        self.lblCost10 = QLabel(self.widget_50)
        self.lblCost10.setObjectName(u"lblCost10")
        self.lblCost10.setGeometry(QRect(30, 10, 211, 76))
        self.lblCost10.setFont(font4)
        self.lblCost10.setStyleSheet(u"color: white;\n"
"text-align: center;\n"
"padding-left:10px;\n"
"font-size: 20px;")
        self.lblCost10.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_29.addWidget(self.widget_50)


        self.horizontalLayout_2.addWidget(self.widget_49)

        self.widget_128 = QWidget(self.wg4)
        self.widget_128.setObjectName(u"widget_128")
        self.verticalLayout_71 = QVBoxLayout(self.widget_128)
        self.verticalLayout_71.setObjectName(u"verticalLayout_71")
        self.wb11 = QWidget(self.widget_128)
        self.wb11.setObjectName(u"wb11")
        sizePolicy2.setHeightForWidth(self.wb11.sizePolicy().hasHeightForWidth())
        self.wb11.setSizePolicy(sizePolicy2)
        self.wb11.setMinimumSize(QSize(220, 200))
        self.wb11.setMaximumSize(QSize(220, 200))
        self.wb11.setStyleSheet(u"background-color:transparent;")

        self.verticalLayout_71.addWidget(self.wb11, 0, Qt.AlignmentFlag.AlignHCenter)

        self.widget_129 = QWidget(self.widget_128)
        self.widget_129.setObjectName(u"widget_129")
        self.btnAdd11 = QPushButton(self.widget_129)
        self.btnAdd11.setObjectName(u"btnAdd11")
        self.btnAdd11.setGeometry(QRect(60, 100, 151, 51))
        sizePolicy3.setHeightForWidth(self.btnAdd11.sizePolicy().hasHeightForWidth())
        self.btnAdd11.setSizePolicy(sizePolicy3)
        self.btnAdd11.setFont(font3)
        self.btnAdd11.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btnAdd11.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(255, 255, 255);\n"
"border-radius: 8px;\n"
"	color: rgb(65, 66, 63);\n"
"t\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(239, 50, 104); \n"
"    color: white;\n"
"}\n"
"QPushButton:checked{\n"
" background-color: rgb(239, 50, 104);\n"
" color: white;\n"
"}")
        self.lblCost11 = QLabel(self.widget_129)
        self.lblCost11.setObjectName(u"lblCost11")
        self.lblCost11.setGeometry(QRect(30, 10, 211, 76))
        self.lblCost11.setFont(font4)
        self.lblCost11.setStyleSheet(u"color: white;\n"
"text-align: center;\n"
"padding-left:10px;\n"
"font-size: 20px;")
        self.lblCost11.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_71.addWidget(self.widget_129)


        self.horizontalLayout_2.addWidget(self.widget_128)

        self.widget_45 = QWidget(self.wg4)
        self.widget_45.setObjectName(u"widget_45")
        self.verticalLayout_27 = QVBoxLayout(self.widget_45)
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.wb12 = QWidget(self.widget_45)
        self.wb12.setObjectName(u"wb12")
        sizePolicy2.setHeightForWidth(self.wb12.sizePolicy().hasHeightForWidth())
        self.wb12.setSizePolicy(sizePolicy2)
        self.wb12.setMinimumSize(QSize(220, 200))
        self.wb12.setMaximumSize(QSize(220, 200))
        self.wb12.setStyleSheet(u"background-color:transparent;")

        self.verticalLayout_27.addWidget(self.wb12, 0, Qt.AlignmentFlag.AlignHCenter)

        self.widget_46 = QWidget(self.widget_45)
        self.widget_46.setObjectName(u"widget_46")
        self.btnAdd12 = QPushButton(self.widget_46)
        self.btnAdd12.setObjectName(u"btnAdd12")
        self.btnAdd12.setGeometry(QRect(60, 100, 151, 51))
        sizePolicy3.setHeightForWidth(self.btnAdd12.sizePolicy().hasHeightForWidth())
        self.btnAdd12.setSizePolicy(sizePolicy3)
        self.btnAdd12.setFont(font3)
        self.btnAdd12.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btnAdd12.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(255, 255, 255);\n"
"border-radius: 8px;\n"
"	color: rgb(65, 66, 63);\n"
"t\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(239, 50, 104); \n"
"    color: white;\n"
"}\n"
"QPushButton:checked{\n"
" background-color: rgb(239, 50, 104);\n"
" color: white;\n"
"}")
        self.lblCost12 = QLabel(self.widget_46)
        self.lblCost12.setObjectName(u"lblCost12")
        self.lblCost12.setGeometry(QRect(30, 10, 211, 76))
        self.lblCost12.setFont(font4)
        self.lblCost12.setStyleSheet(u"color: white;\n"
"text-align: center;\n"
"padding-left:10px;\n"
"font-size: 20px;")
        self.lblCost12.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_27.addWidget(self.widget_46)


        self.horizontalLayout_2.addWidget(self.widget_45)


        self.verticalLayout_6.addWidget(self.wg4)

        self.verticalSpacer_12 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_6.addItem(self.verticalSpacer_12)

        self.wg5 = QWidget(self.wdPicMenu)
        self.wg5.setObjectName(u"wg5")
        self.wg5.setMinimumSize(QSize(550, 400))
        self.horizontalLayout_4 = QHBoxLayout(self.wg5)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.widget_43 = QWidget(self.wg5)
        self.widget_43.setObjectName(u"widget_43")
        self.verticalLayout_26 = QVBoxLayout(self.widget_43)
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.wb13 = QWidget(self.widget_43)
        self.wb13.setObjectName(u"wb13")
        sizePolicy2.setHeightForWidth(self.wb13.sizePolicy().hasHeightForWidth())
        self.wb13.setSizePolicy(sizePolicy2)
        self.wb13.setMinimumSize(QSize(220, 200))
        self.wb13.setMaximumSize(QSize(220, 200))
        self.wb13.setStyleSheet(u"background-color:transparent;")

        self.verticalLayout_26.addWidget(self.wb13, 0, Qt.AlignmentFlag.AlignHCenter)

        self.widget_44 = QWidget(self.widget_43)
        self.widget_44.setObjectName(u"widget_44")
        self.btnAdd13 = QPushButton(self.widget_44)
        self.btnAdd13.setObjectName(u"btnAdd13")
        self.btnAdd13.setGeometry(QRect(60, 100, 151, 51))
        sizePolicy3.setHeightForWidth(self.btnAdd13.sizePolicy().hasHeightForWidth())
        self.btnAdd13.setSizePolicy(sizePolicy3)
        self.btnAdd13.setFont(font3)
        self.btnAdd13.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btnAdd13.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(255, 255, 255);\n"
"border-radius: 8px;\n"
"	color: rgb(65, 66, 63);\n"
"t\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(239, 50, 104); \n"
"    color: white;\n"
"}\n"
"QPushButton:checked{\n"
" background-color: rgb(239, 50, 104);\n"
" color: white;\n"
"}")
        self.lblCost13 = QLabel(self.widget_44)
        self.lblCost13.setObjectName(u"lblCost13")
        self.lblCost13.setGeometry(QRect(30, 10, 211, 76))
        self.lblCost13.setFont(font4)
        self.lblCost13.setStyleSheet(u"color: white;\n"
"text-align: center;\n"
"padding-left:10px;\n"
"font-size: 20px;")
        self.lblCost13.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_26.addWidget(self.widget_44)


        self.horizontalLayout_4.addWidget(self.widget_43)

        self.widget_41 = QWidget(self.wg5)
        self.widget_41.setObjectName(u"widget_41")
        self.verticalLayout_25 = QVBoxLayout(self.widget_41)
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.wb14 = QWidget(self.widget_41)
        self.wb14.setObjectName(u"wb14")
        sizePolicy2.setHeightForWidth(self.wb14.sizePolicy().hasHeightForWidth())
        self.wb14.setSizePolicy(sizePolicy2)
        self.wb14.setMinimumSize(QSize(220, 200))
        self.wb14.setMaximumSize(QSize(220, 200))
        self.wb14.setStyleSheet(u"background-color:transparent;")

        self.verticalLayout_25.addWidget(self.wb14, 0, Qt.AlignmentFlag.AlignHCenter)

        self.widget_42 = QWidget(self.widget_41)
        self.widget_42.setObjectName(u"widget_42")
        self.btnAdd14 = QPushButton(self.widget_42)
        self.btnAdd14.setObjectName(u"btnAdd14")
        self.btnAdd14.setGeometry(QRect(60, 100, 151, 51))
        sizePolicy3.setHeightForWidth(self.btnAdd14.sizePolicy().hasHeightForWidth())
        self.btnAdd14.setSizePolicy(sizePolicy3)
        self.btnAdd14.setFont(font3)
        self.btnAdd14.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btnAdd14.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(255, 255, 255);\n"
"border-radius: 8px;\n"
"	color: rgb(65, 66, 63);\n"
"t\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(239, 50, 104); \n"
"    color: white;\n"
"}\n"
"QPushButton:checked{\n"
" background-color: rgb(239, 50, 104);\n"
" color: white;\n"
"}")
        self.lblCost14 = QLabel(self.widget_42)
        self.lblCost14.setObjectName(u"lblCost14")
        self.lblCost14.setGeometry(QRect(30, 10, 211, 76))
        self.lblCost14.setFont(font4)
        self.lblCost14.setStyleSheet(u"color: white;\n"
"text-align: center;\n"
"padding-left:10px;\n"
"font-size: 20px;")
        self.lblCost14.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_25.addWidget(self.widget_42)


        self.horizontalLayout_4.addWidget(self.widget_41)

        self.widget_39 = QWidget(self.wg5)
        self.widget_39.setObjectName(u"widget_39")
        self.verticalLayout_24 = QVBoxLayout(self.widget_39)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.wb15 = QWidget(self.widget_39)
        self.wb15.setObjectName(u"wb15")
        sizePolicy2.setHeightForWidth(self.wb15.sizePolicy().hasHeightForWidth())
        self.wb15.setSizePolicy(sizePolicy2)
        self.wb15.setMinimumSize(QSize(220, 200))
        self.wb15.setMaximumSize(QSize(220, 200))
        self.wb15.setStyleSheet(u"background-color:transparent;")

        self.verticalLayout_24.addWidget(self.wb15, 0, Qt.AlignmentFlag.AlignHCenter)

        self.widget_40 = QWidget(self.widget_39)
        self.widget_40.setObjectName(u"widget_40")
        self.btnAdd15 = QPushButton(self.widget_40)
        self.btnAdd15.setObjectName(u"btnAdd15")
        self.btnAdd15.setGeometry(QRect(60, 100, 151, 51))
        sizePolicy3.setHeightForWidth(self.btnAdd15.sizePolicy().hasHeightForWidth())
        self.btnAdd15.setSizePolicy(sizePolicy3)
        self.btnAdd15.setFont(font3)
        self.btnAdd15.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btnAdd15.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(255, 255, 255);\n"
"border-radius: 8px;\n"
"	color: rgb(65, 66, 63);\n"
"t\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(239, 50, 104); \n"
"    color: white;\n"
"}\n"
"QPushButton:checked{\n"
" background-color: rgb(239, 50, 104);\n"
" color: white;\n"
"}")
        self.lblCost15 = QLabel(self.widget_40)
        self.lblCost15.setObjectName(u"lblCost15")
        self.lblCost15.setGeometry(QRect(30, 10, 211, 76))
        self.lblCost15.setFont(font4)
        self.lblCost15.setStyleSheet(u"color: white;\n"
"text-align: center;\n"
"padding-left:10px;\n"
"font-size: 20px;")
        self.lblCost15.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_24.addWidget(self.widget_40)


        self.horizontalLayout_4.addWidget(self.widget_39)


        self.verticalLayout_6.addWidget(self.wg5)

        self.verticalSpacer_20 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_6.addItem(self.verticalSpacer_20)

        self.wg6 = QWidget(self.wdPicMenu)
        self.wg6.setObjectName(u"wg6")
        self.wg6.setMinimumSize(QSize(550, 400))
        self.horizontalLayout_5 = QHBoxLayout(self.wg6)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.widget_37 = QWidget(self.wg6)
        self.widget_37.setObjectName(u"widget_37")
        self.verticalLayout_23 = QVBoxLayout(self.widget_37)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.wb16 = QWidget(self.widget_37)
        self.wb16.setObjectName(u"wb16")
        sizePolicy2.setHeightForWidth(self.wb16.sizePolicy().hasHeightForWidth())
        self.wb16.setSizePolicy(sizePolicy2)
        self.wb16.setMinimumSize(QSize(220, 200))
        self.wb16.setMaximumSize(QSize(220, 200))
        self.wb16.setStyleSheet(u"background-color:transparent;")

        self.verticalLayout_23.addWidget(self.wb16, 0, Qt.AlignmentFlag.AlignHCenter)

        self.widget_38 = QWidget(self.widget_37)
        self.widget_38.setObjectName(u"widget_38")
        self.btnAdd16 = QPushButton(self.widget_38)
        self.btnAdd16.setObjectName(u"btnAdd16")
        self.btnAdd16.setGeometry(QRect(60, 100, 151, 51))
        sizePolicy3.setHeightForWidth(self.btnAdd16.sizePolicy().hasHeightForWidth())
        self.btnAdd16.setSizePolicy(sizePolicy3)
        self.btnAdd16.setFont(font3)
        self.btnAdd16.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btnAdd16.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(255, 255, 255);\n"
"border-radius: 8px;\n"
"	color: rgb(65, 66, 63);\n"
"t\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(239, 50, 104); \n"
"    color: white;\n"
"}\n"
"QPushButton:checked{\n"
" background-color: rgb(239, 50, 104);\n"
" color: white;\n"
"}")
        self.lblCost16 = QLabel(self.widget_38)
        self.lblCost16.setObjectName(u"lblCost16")
        self.lblCost16.setGeometry(QRect(30, 10, 211, 76))
        self.lblCost16.setFont(font4)
        self.lblCost16.setStyleSheet(u"color: white;\n"
"text-align: center;\n"
"padding-left:10px;\n"
"font-size: 20px;")
        self.lblCost16.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_23.addWidget(self.widget_38)


        self.horizontalLayout_5.addWidget(self.widget_37)

        self.widget_35 = QWidget(self.wg6)
        self.widget_35.setObjectName(u"widget_35")
        self.verticalLayout_22 = QVBoxLayout(self.widget_35)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.wb17 = QWidget(self.widget_35)
        self.wb17.setObjectName(u"wb17")
        sizePolicy2.setHeightForWidth(self.wb17.sizePolicy().hasHeightForWidth())
        self.wb17.setSizePolicy(sizePolicy2)
        self.wb17.setMinimumSize(QSize(220, 200))
        self.wb17.setMaximumSize(QSize(220, 200))
        self.wb17.setStyleSheet(u"background-color:transparent;")

        self.verticalLayout_22.addWidget(self.wb17, 0, Qt.AlignmentFlag.AlignHCenter)

        self.widget_36 = QWidget(self.widget_35)
        self.widget_36.setObjectName(u"widget_36")
        self.btnAdd17 = QPushButton(self.widget_36)
        self.btnAdd17.setObjectName(u"btnAdd17")
        self.btnAdd17.setGeometry(QRect(60, 100, 151, 51))
        sizePolicy3.setHeightForWidth(self.btnAdd17.sizePolicy().hasHeightForWidth())
        self.btnAdd17.setSizePolicy(sizePolicy3)
        self.btnAdd17.setFont(font3)
        self.btnAdd17.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btnAdd17.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(255, 255, 255);\n"
"border-radius: 8px;\n"
"	color: rgb(65, 66, 63);\n"
"t\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(239, 50, 104); \n"
"    color: white;\n"
"}\n"
"QPushButton:checked{\n"
" background-color: rgb(239, 50, 104);\n"
" color: white;\n"
"}")
        self.lblCost17 = QLabel(self.widget_36)
        self.lblCost17.setObjectName(u"lblCost17")
        self.lblCost17.setGeometry(QRect(30, 10, 211, 76))
        self.lblCost17.setFont(font4)
        self.lblCost17.setStyleSheet(u"color: white;\n"
"text-align: center;\n"
"padding-left:10px;\n"
"font-size: 20px;")
        self.lblCost17.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_22.addWidget(self.widget_36)


        self.horizontalLayout_5.addWidget(self.widget_35)

        self.widget_33 = QWidget(self.wg6)
        self.widget_33.setObjectName(u"widget_33")
        self.verticalLayout_21 = QVBoxLayout(self.widget_33)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.wb18 = QWidget(self.widget_33)
        self.wb18.setObjectName(u"wb18")
        sizePolicy2.setHeightForWidth(self.wb18.sizePolicy().hasHeightForWidth())
        self.wb18.setSizePolicy(sizePolicy2)
        self.wb18.setMinimumSize(QSize(220, 200))
        self.wb18.setMaximumSize(QSize(220, 200))
        self.wb18.setStyleSheet(u"background-color:transparent;")

        self.verticalLayout_21.addWidget(self.wb18, 0, Qt.AlignmentFlag.AlignHCenter)

        self.widget_34 = QWidget(self.widget_33)
        self.widget_34.setObjectName(u"widget_34")
        self.btnAdd18 = QPushButton(self.widget_34)
        self.btnAdd18.setObjectName(u"btnAdd18")
        self.btnAdd18.setGeometry(QRect(60, 100, 151, 51))
        sizePolicy3.setHeightForWidth(self.btnAdd18.sizePolicy().hasHeightForWidth())
        self.btnAdd18.setSizePolicy(sizePolicy3)
        self.btnAdd18.setFont(font3)
        self.btnAdd18.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btnAdd18.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(255, 255, 255);\n"
"border-radius: 8px;\n"
"	color: rgb(65, 66, 63);\n"
"t\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(239, 50, 104); \n"
"    color: white;\n"
"}\n"
"QPushButton:checked{\n"
" background-color: rgb(239, 50, 104);\n"
" color: white;\n"
"}")
        self.lblCost18 = QLabel(self.widget_34)
        self.lblCost18.setObjectName(u"lblCost18")
        self.lblCost18.setGeometry(QRect(30, 10, 211, 76))
        self.lblCost18.setFont(font4)
        self.lblCost18.setStyleSheet(u"color: white;\n"
"text-align: center;\n"
"padding-left:10px;\n"
"font-size: 20px;")
        self.lblCost18.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_21.addWidget(self.widget_34)


        self.horizontalLayout_5.addWidget(self.widget_33)


        self.verticalLayout_6.addWidget(self.wg6)

        self.verticalSpacer_13 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_6.addItem(self.verticalSpacer_13)

        self.wg7 = QWidget(self.wdPicMenu)
        self.wg7.setObjectName(u"wg7")
        self.wg7.setMinimumSize(QSize(550, 400))
        self.horizontalLayout_6 = QHBoxLayout(self.wg7)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.widget_31 = QWidget(self.wg7)
        self.widget_31.setObjectName(u"widget_31")
        self.verticalLayout_10 = QVBoxLayout(self.widget_31)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.wb19 = QWidget(self.widget_31)
        self.wb19.setObjectName(u"wb19")
        sizePolicy2.setHeightForWidth(self.wb19.sizePolicy().hasHeightForWidth())
        self.wb19.setSizePolicy(sizePolicy2)
        self.wb19.setMinimumSize(QSize(220, 200))
        self.wb19.setMaximumSize(QSize(220, 200))
        self.wb19.setStyleSheet(u"background-color:transparent;")

        self.verticalLayout_10.addWidget(self.wb19, 0, Qt.AlignmentFlag.AlignHCenter)

        self.widget_32 = QWidget(self.widget_31)
        self.widget_32.setObjectName(u"widget_32")
        self.btnAdd19 = QPushButton(self.widget_32)
        self.btnAdd19.setObjectName(u"btnAdd19")
        self.btnAdd19.setGeometry(QRect(60, 100, 151, 51))
        sizePolicy3.setHeightForWidth(self.btnAdd19.sizePolicy().hasHeightForWidth())
        self.btnAdd19.setSizePolicy(sizePolicy3)
        self.btnAdd19.setFont(font3)
        self.btnAdd19.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btnAdd19.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(255, 255, 255);\n"
"border-radius: 8px;\n"
"	color: rgb(65, 66, 63);\n"
"t\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(239, 50, 104); \n"
"    color: white;\n"
"}\n"
"QPushButton:checked{\n"
" background-color: rgb(239, 50, 104);\n"
" color: white;\n"
"}")
        self.lblCost19 = QLabel(self.widget_32)
        self.lblCost19.setObjectName(u"lblCost19")
        self.lblCost19.setGeometry(QRect(30, 10, 211, 76))
        self.lblCost19.setFont(font4)
        self.lblCost19.setStyleSheet(u"color: white;\n"
"text-align: center;\n"
"padding-left:10px;\n"
"font-size: 20px;")
        self.lblCost19.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_10.addWidget(self.widget_32)


        self.horizontalLayout_6.addWidget(self.widget_31)

        self.widget_29 = QWidget(self.wg7)
        self.widget_29.setObjectName(u"widget_29")
        self.verticalLayout_20 = QVBoxLayout(self.widget_29)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.wb20 = QWidget(self.widget_29)
        self.wb20.setObjectName(u"wb20")
        sizePolicy2.setHeightForWidth(self.wb20.sizePolicy().hasHeightForWidth())
        self.wb20.setSizePolicy(sizePolicy2)
        self.wb20.setMinimumSize(QSize(220, 200))
        self.wb20.setMaximumSize(QSize(220, 200))
        self.wb20.setStyleSheet(u"background-color:transparent;")

        self.verticalLayout_20.addWidget(self.wb20, 0, Qt.AlignmentFlag.AlignHCenter)

        self.widget_30 = QWidget(self.widget_29)
        self.widget_30.setObjectName(u"widget_30")
        self.btnAdd20 = QPushButton(self.widget_30)
        self.btnAdd20.setObjectName(u"btnAdd20")
        self.btnAdd20.setGeometry(QRect(60, 100, 151, 51))
        sizePolicy3.setHeightForWidth(self.btnAdd20.sizePolicy().hasHeightForWidth())
        self.btnAdd20.setSizePolicy(sizePolicy3)
        self.btnAdd20.setFont(font3)
        self.btnAdd20.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btnAdd20.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(255, 255, 255);\n"
"border-radius: 8px;\n"
"	color: rgb(65, 66, 63);\n"
"t\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(239, 50, 104); \n"
"    color: white;\n"
"}\n"
"QPushButton:checked{\n"
" background-color: rgb(239, 50, 104);\n"
" color: white;\n"
"}")
        self.lblCost20 = QLabel(self.widget_30)
        self.lblCost20.setObjectName(u"lblCost20")
        self.lblCost20.setGeometry(QRect(30, 10, 211, 76))
        self.lblCost20.setFont(font4)
        self.lblCost20.setStyleSheet(u"color: white;\n"
"text-align: center;\n"
"padding-left:10px;\n"
"font-size: 20px;")
        self.lblCost20.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_20.addWidget(self.widget_30)


        self.horizontalLayout_6.addWidget(self.widget_29)

        self.widget_27 = QWidget(self.wg7)
        self.widget_27.setObjectName(u"widget_27")
        self.verticalLayout_19 = QVBoxLayout(self.widget_27)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.wb21 = QWidget(self.widget_27)
        self.wb21.setObjectName(u"wb21")
        sizePolicy2.setHeightForWidth(self.wb21.sizePolicy().hasHeightForWidth())
        self.wb21.setSizePolicy(sizePolicy2)
        self.wb21.setMinimumSize(QSize(220, 200))
        self.wb21.setMaximumSize(QSize(220, 200))
        self.wb21.setStyleSheet(u"background-color:transparent;")

        self.verticalLayout_19.addWidget(self.wb21, 0, Qt.AlignmentFlag.AlignHCenter)

        self.widget_28 = QWidget(self.widget_27)
        self.widget_28.setObjectName(u"widget_28")
        self.btnAdd21 = QPushButton(self.widget_28)
        self.btnAdd21.setObjectName(u"btnAdd21")
        self.btnAdd21.setGeometry(QRect(60, 100, 151, 51))
        sizePolicy3.setHeightForWidth(self.btnAdd21.sizePolicy().hasHeightForWidth())
        self.btnAdd21.setSizePolicy(sizePolicy3)
        self.btnAdd21.setFont(font3)
        self.btnAdd21.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btnAdd21.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(255, 255, 255);\n"
"border-radius: 8px;\n"
"	color: rgb(65, 66, 63);\n"
"t\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(239, 50, 104); \n"
"    color: white;\n"
"}\n"
"QPushButton:checked{\n"
" background-color: rgb(239, 50, 104);\n"
" color: white;\n"
"}")
        self.lblCost21 = QLabel(self.widget_28)
        self.lblCost21.setObjectName(u"lblCost21")
        self.lblCost21.setGeometry(QRect(30, 10, 211, 76))
        self.lblCost21.setFont(font4)
        self.lblCost21.setStyleSheet(u"color: white;\n"
"text-align: center;\n"
"padding-left:10px;\n"
"font-size: 20px;")
        self.lblCost21.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_19.addWidget(self.widget_28)


        self.horizontalLayout_6.addWidget(self.widget_27)


        self.verticalLayout_6.addWidget(self.wg7)

        self.verticalSpacer_14 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_6.addItem(self.verticalSpacer_14)

        self.wg8 = QWidget(self.wdPicMenu)
        self.wg8.setObjectName(u"wg8")
        self.wg8.setMinimumSize(QSize(550, 400))
        self.horizontalLayout_8 = QHBoxLayout(self.wg8)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.widget_25 = QWidget(self.wg8)
        self.widget_25.setObjectName(u"widget_25")
        self.verticalLayout_9 = QVBoxLayout(self.widget_25)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.wb22 = QWidget(self.widget_25)
        self.wb22.setObjectName(u"wb22")
        sizePolicy2.setHeightForWidth(self.wb22.sizePolicy().hasHeightForWidth())
        self.wb22.setSizePolicy(sizePolicy2)
        self.wb22.setMinimumSize(QSize(220, 200))
        self.wb22.setMaximumSize(QSize(220, 200))
        self.wb22.setStyleSheet(u"background-color:transparent;")

        self.verticalLayout_9.addWidget(self.wb22, 0, Qt.AlignmentFlag.AlignHCenter)

        self.widget_26 = QWidget(self.widget_25)
        self.widget_26.setObjectName(u"widget_26")
        self.btnAdd22 = QPushButton(self.widget_26)
        self.btnAdd22.setObjectName(u"btnAdd22")
        self.btnAdd22.setGeometry(QRect(60, 100, 151, 51))
        sizePolicy3.setHeightForWidth(self.btnAdd22.sizePolicy().hasHeightForWidth())
        self.btnAdd22.setSizePolicy(sizePolicy3)
        self.btnAdd22.setFont(font3)
        self.btnAdd22.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btnAdd22.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(255, 255, 255);\n"
"border-radius: 8px;\n"
"	color: rgb(65, 66, 63);\n"
"t\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(239, 50, 104); \n"
"    color: white;\n"
"}\n"
"QPushButton:checked{\n"
" background-color: rgb(239, 50, 104);\n"
" color: white;\n"
"}")
        self.lblCost22 = QLabel(self.widget_26)
        self.lblCost22.setObjectName(u"lblCost22")
        self.lblCost22.setGeometry(QRect(30, 10, 211, 76))
        self.lblCost22.setFont(font4)
        self.lblCost22.setStyleSheet(u"color: white;\n"
"text-align: center;\n"
"padding-left:10px;\n"
"font-size: 20px;")
        self.lblCost22.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_9.addWidget(self.widget_26)


        self.horizontalLayout_8.addWidget(self.widget_25)

        self.widget_23 = QWidget(self.wg8)
        self.widget_23.setObjectName(u"widget_23")
        self.verticalLayout_18 = QVBoxLayout(self.widget_23)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.wb23 = QWidget(self.widget_23)
        self.wb23.setObjectName(u"wb23")
        sizePolicy2.setHeightForWidth(self.wb23.sizePolicy().hasHeightForWidth())
        self.wb23.setSizePolicy(sizePolicy2)
        self.wb23.setMinimumSize(QSize(220, 200))
        self.wb23.setMaximumSize(QSize(220, 200))
        self.wb23.setStyleSheet(u"background-color:transparent;")

        self.verticalLayout_18.addWidget(self.wb23, 0, Qt.AlignmentFlag.AlignHCenter)

        self.widget_24 = QWidget(self.widget_23)
        self.widget_24.setObjectName(u"widget_24")
        self.btnAdd23 = QPushButton(self.widget_24)
        self.btnAdd23.setObjectName(u"btnAdd23")
        self.btnAdd23.setGeometry(QRect(60, 100, 151, 51))
        sizePolicy3.setHeightForWidth(self.btnAdd23.sizePolicy().hasHeightForWidth())
        self.btnAdd23.setSizePolicy(sizePolicy3)
        self.btnAdd23.setFont(font3)
        self.btnAdd23.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btnAdd23.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(255, 255, 255);\n"
"border-radius: 8px;\n"
"	color: rgb(65, 66, 63);\n"
"t\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(239, 50, 104); \n"
"    color: white;\n"
"}\n"
"QPushButton:checked{\n"
" background-color: rgb(239, 50, 104);\n"
" color: white;\n"
"}")
        self.lblCost23 = QLabel(self.widget_24)
        self.lblCost23.setObjectName(u"lblCost23")
        self.lblCost23.setGeometry(QRect(30, 10, 211, 76))
        self.lblCost23.setFont(font4)
        self.lblCost23.setStyleSheet(u"color: white;\n"
"text-align: center;\n"
"padding-left:10px;\n"
"font-size: 20px;")
        self.lblCost23.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_18.addWidget(self.widget_24)


        self.horizontalLayout_8.addWidget(self.widget_23)

        self.widget_21 = QWidget(self.wg8)
        self.widget_21.setObjectName(u"widget_21")
        self.verticalLayout_17 = QVBoxLayout(self.widget_21)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.wb24 = QWidget(self.widget_21)
        self.wb24.setObjectName(u"wb24")
        sizePolicy2.setHeightForWidth(self.wb24.sizePolicy().hasHeightForWidth())
        self.wb24.setSizePolicy(sizePolicy2)
        self.wb24.setMinimumSize(QSize(220, 200))
        self.wb24.setMaximumSize(QSize(220, 200))
        self.wb24.setStyleSheet(u"background-color:transparent;")

        self.verticalLayout_17.addWidget(self.wb24, 0, Qt.AlignmentFlag.AlignHCenter)

        self.widget_22 = QWidget(self.widget_21)
        self.widget_22.setObjectName(u"widget_22")
        self.btnAdd24 = QPushButton(self.widget_22)
        self.btnAdd24.setObjectName(u"btnAdd24")
        self.btnAdd24.setGeometry(QRect(60, 100, 151, 51))
        sizePolicy3.setHeightForWidth(self.btnAdd24.sizePolicy().hasHeightForWidth())
        self.btnAdd24.setSizePolicy(sizePolicy3)
        self.btnAdd24.setFont(font3)
        self.btnAdd24.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btnAdd24.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(255, 255, 255);\n"
"border-radius: 8px;\n"
"	color: rgb(65, 66, 63);\n"
"t\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(239, 50, 104); \n"
"    color: white;\n"
"}\n"
"QPushButton:checked{\n"
" background-color: rgb(239, 50, 104);\n"
" color: white;\n"
"}")
        self.lblCost24 = QLabel(self.widget_22)
        self.lblCost24.setObjectName(u"lblCost24")
        self.lblCost24.setGeometry(QRect(30, 10, 211, 76))
        self.lblCost24.setFont(font4)
        self.lblCost24.setStyleSheet(u"color: white;\n"
"text-align: center;\n"
"padding-left:10px;\n"
"font-size: 20px;")
        self.lblCost24.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_17.addWidget(self.widget_22)


        self.horizontalLayout_8.addWidget(self.widget_21)


        self.verticalLayout_6.addWidget(self.wg8)

        self.verticalSpacer_15 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_6.addItem(self.verticalSpacer_15)

        self.wg9 = QWidget(self.wdPicMenu)
        self.wg9.setObjectName(u"wg9")
        self.wg9.setMinimumSize(QSize(550, 400))
        self.horizontalLayout_7 = QHBoxLayout(self.wg9)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.widget_11 = QWidget(self.wg9)
        self.widget_11.setObjectName(u"widget_11")
        self.verticalLayout_8 = QVBoxLayout(self.widget_11)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.wb27 = QWidget(self.widget_11)
        self.wb27.setObjectName(u"wb27")
        sizePolicy2.setHeightForWidth(self.wb27.sizePolicy().hasHeightForWidth())
        self.wb27.setSizePolicy(sizePolicy2)
        self.wb27.setMinimumSize(QSize(220, 200))
        self.wb27.setMaximumSize(QSize(220, 200))
        self.wb27.setStyleSheet(u"background-color:transparent;")

        self.verticalLayout_8.addWidget(self.wb27, 0, Qt.AlignmentFlag.AlignHCenter)

        self.widget_16 = QWidget(self.widget_11)
        self.widget_16.setObjectName(u"widget_16")
        self.btnAdd27 = QPushButton(self.widget_16)
        self.btnAdd27.setObjectName(u"btnAdd27")
        self.btnAdd27.setGeometry(QRect(60, 100, 151, 51))
        sizePolicy3.setHeightForWidth(self.btnAdd27.sizePolicy().hasHeightForWidth())
        self.btnAdd27.setSizePolicy(sizePolicy3)
        self.btnAdd27.setFont(font3)
        self.btnAdd27.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btnAdd27.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(255, 255, 255);\n"
"border-radius: 8px;\n"
"	color: rgb(65, 66, 63);\n"
"t\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(239, 50, 104); \n"
"    color: white;\n"
"}\n"
"QPushButton:checked{\n"
" background-color: rgb(239, 50, 104);\n"
" color: white;\n"
"}")
        self.lblCost27 = QLabel(self.widget_16)
        self.lblCost27.setObjectName(u"lblCost27")
        self.lblCost27.setGeometry(QRect(30, 10, 211, 76))
        self.lblCost27.setFont(font4)
        self.lblCost27.setStyleSheet(u"color: white;\n"
"text-align: center;\n"
"padding-left:10px;\n"
"font-size: 20px;")
        self.lblCost27.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_8.addWidget(self.widget_16)


        self.horizontalLayout_7.addWidget(self.widget_11)

        self.widget_17 = QWidget(self.wg9)
        self.widget_17.setObjectName(u"widget_17")
        self.verticalLayout_15 = QVBoxLayout(self.widget_17)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.wb26 = QWidget(self.widget_17)
        self.wb26.setObjectName(u"wb26")
        sizePolicy2.setHeightForWidth(self.wb26.sizePolicy().hasHeightForWidth())
        self.wb26.setSizePolicy(sizePolicy2)
        self.wb26.setMinimumSize(QSize(220, 200))
        self.wb26.setMaximumSize(QSize(220, 200))
        self.wb26.setStyleSheet(u"background-color:transparent;")

        self.verticalLayout_15.addWidget(self.wb26, 0, Qt.AlignmentFlag.AlignHCenter)

        self.widget_18 = QWidget(self.widget_17)
        self.widget_18.setObjectName(u"widget_18")
        self.btnAdd26 = QPushButton(self.widget_18)
        self.btnAdd26.setObjectName(u"btnAdd26")
        self.btnAdd26.setGeometry(QRect(60, 100, 151, 51))
        sizePolicy3.setHeightForWidth(self.btnAdd26.sizePolicy().hasHeightForWidth())
        self.btnAdd26.setSizePolicy(sizePolicy3)
        self.btnAdd26.setFont(font3)
        self.btnAdd26.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btnAdd26.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(255, 255, 255);\n"
"border-radius: 8px;\n"
"	color: rgb(65, 66, 63);\n"
"t\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(239, 50, 104); \n"
"    color: white;\n"
"}\n"
"QPushButton:checked{\n"
" background-color: rgb(239, 50, 104);\n"
" color: white;\n"
"}")
        self.lblCost26 = QLabel(self.widget_18)
        self.lblCost26.setObjectName(u"lblCost26")
        self.lblCost26.setGeometry(QRect(30, 10, 211, 76))
        self.lblCost26.setFont(font4)
        self.lblCost26.setStyleSheet(u"color: white;\n"
"text-align: center;\n"
"padding-left:10px;\n"
"font-size: 20px;")
        self.lblCost26.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_15.addWidget(self.widget_18)


        self.horizontalLayout_7.addWidget(self.widget_17)

        self.widget_19 = QWidget(self.wg9)
        self.widget_19.setObjectName(u"widget_19")
        self.verticalLayout_16 = QVBoxLayout(self.widget_19)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.wb25 = QWidget(self.widget_19)
        self.wb25.setObjectName(u"wb25")
        sizePolicy2.setHeightForWidth(self.wb25.sizePolicy().hasHeightForWidth())
        self.wb25.setSizePolicy(sizePolicy2)
        self.wb25.setMinimumSize(QSize(220, 200))
        self.wb25.setMaximumSize(QSize(220, 200))
        self.wb25.setStyleSheet(u"background-color:transparent;")

        self.verticalLayout_16.addWidget(self.wb25, 0, Qt.AlignmentFlag.AlignHCenter)

        self.widget_20 = QWidget(self.widget_19)
        self.widget_20.setObjectName(u"widget_20")
        self.btnAdd25 = QPushButton(self.widget_20)
        self.btnAdd25.setObjectName(u"btnAdd25")
        self.btnAdd25.setGeometry(QRect(60, 100, 151, 51))
        sizePolicy3.setHeightForWidth(self.btnAdd25.sizePolicy().hasHeightForWidth())
        self.btnAdd25.setSizePolicy(sizePolicy3)
        self.btnAdd25.setFont(font3)
        self.btnAdd25.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btnAdd25.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(255, 255, 255);\n"
"border-radius: 8px;\n"
"	color: rgb(65, 66, 63);\n"
"t\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(239, 50, 104); \n"
"    color: white;\n"
"}\n"
"QPushButton:checked{\n"
" background-color: rgb(239, 50, 104);\n"
" color: white;\n"
"}")
        self.lblCost25 = QLabel(self.widget_20)
        self.lblCost25.setObjectName(u"lblCost25")
        self.lblCost25.setGeometry(QRect(30, 10, 211, 76))
        self.lblCost25.setFont(font4)
        self.lblCost25.setStyleSheet(u"color: white;\n"
"text-align: center;\n"
"padding-left:10px;\n"
"font-size: 20px;")
        self.lblCost25.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_16.addWidget(self.widget_20)


        self.horizontalLayout_7.addWidget(self.widget_19)


        self.verticalLayout_6.addWidget(self.wg9)

        self.verticalSpacer_16 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_6.addItem(self.verticalSpacer_16)

        self.wg10 = QWidget(self.wdPicMenu)
        self.wg10.setObjectName(u"wg10")
        self.wg10.setMinimumSize(QSize(550, 400))
        self.horizontalLayout_3 = QHBoxLayout(self.wg10)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.widget_7 = QWidget(self.wg10)
        self.widget_7.setObjectName(u"widget_7")
        self.verticalLayout_7 = QVBoxLayout(self.widget_7)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.wb28 = QWidget(self.widget_7)
        self.wb28.setObjectName(u"wb28")
        sizePolicy2.setHeightForWidth(self.wb28.sizePolicy().hasHeightForWidth())
        self.wb28.setSizePolicy(sizePolicy2)
        self.wb28.setMinimumSize(QSize(220, 200))
        self.wb28.setMaximumSize(QSize(220, 200))
        self.wb28.setStyleSheet(u"background-color:transparent;")

        self.verticalLayout_7.addWidget(self.wb28, 0, Qt.AlignmentFlag.AlignHCenter)

        self.widget_8 = QWidget(self.widget_7)
        self.widget_8.setObjectName(u"widget_8")
        self.btnAdd28 = QPushButton(self.widget_8)
        self.btnAdd28.setObjectName(u"btnAdd28")
        self.btnAdd28.setGeometry(QRect(60, 100, 151, 51))
        sizePolicy3.setHeightForWidth(self.btnAdd28.sizePolicy().hasHeightForWidth())
        self.btnAdd28.setSizePolicy(sizePolicy3)
        self.btnAdd28.setFont(font3)
        self.btnAdd28.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btnAdd28.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(255, 255, 255);\n"
"border-radius: 8px;\n"
"	color: rgb(65, 66, 63);\n"
"t\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(239, 50, 104); \n"
"    color: white;\n"
"}\n"
"QPushButton:checked{\n"
" background-color: rgb(239, 50, 104);\n"
" color: white;\n"
"}")
        self.lblCost28 = QLabel(self.widget_8)
        self.lblCost28.setObjectName(u"lblCost28")
        self.lblCost28.setGeometry(QRect(30, 10, 211, 76))
        self.lblCost28.setFont(font4)
        self.lblCost28.setStyleSheet(u"color: white;\n"
"text-align: center;\n"
"padding-left:10px;\n"
"font-size: 20px;")
        self.lblCost28.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_7.addWidget(self.widget_8)


        self.horizontalLayout_3.addWidget(self.widget_7)

        self.widget_6 = QWidget(self.wg10)
        self.widget_6.setObjectName(u"widget_6")
        self.verticalLayout_13 = QVBoxLayout(self.widget_6)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.wb29 = QWidget(self.widget_6)
        self.wb29.setObjectName(u"wb29")
        sizePolicy2.setHeightForWidth(self.wb29.sizePolicy().hasHeightForWidth())
        self.wb29.setSizePolicy(sizePolicy2)
        self.wb29.setMinimumSize(QSize(220, 200))
        self.wb29.setMaximumSize(QSize(220, 200))
        self.wb29.setStyleSheet(u"background-color:transparent;")

        self.verticalLayout_13.addWidget(self.wb29, 0, Qt.AlignmentFlag.AlignHCenter)

        self.widget_10 = QWidget(self.widget_6)
        self.widget_10.setObjectName(u"widget_10")
        self.btnAdd29 = QPushButton(self.widget_10)
        self.btnAdd29.setObjectName(u"btnAdd29")
        self.btnAdd29.setGeometry(QRect(60, 100, 151, 51))
        sizePolicy3.setHeightForWidth(self.btnAdd29.sizePolicy().hasHeightForWidth())
        self.btnAdd29.setSizePolicy(sizePolicy3)
        self.btnAdd29.setFont(font3)
        self.btnAdd29.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btnAdd29.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(255, 255, 255);\n"
"border-radius: 8px;\n"
"	color: rgb(65, 66, 63);\n"
"t\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(239, 50, 104); \n"
"    color: white;\n"
"}\n"
"QPushButton:checked{\n"
" background-color: rgb(239, 50, 104);\n"
" color: white;\n"
"}")
        self.lblCost29 = QLabel(self.widget_10)
        self.lblCost29.setObjectName(u"lblCost29")
        self.lblCost29.setGeometry(QRect(30, 10, 211, 76))
        self.lblCost29.setFont(font4)
        self.lblCost29.setStyleSheet(u"color: white;\n"
"text-align: center;\n"
"padding-left:10px;\n"
"font-size: 20px;")
        self.lblCost29.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_13.addWidget(self.widget_10)


        self.horizontalLayout_3.addWidget(self.widget_6)

        self.widget_14 = QWidget(self.wg10)
        self.widget_14.setObjectName(u"widget_14")
        self.verticalLayout_14 = QVBoxLayout(self.widget_14)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.wb30 = QWidget(self.widget_14)
        self.wb30.setObjectName(u"wb30")
        sizePolicy2.setHeightForWidth(self.wb30.sizePolicy().hasHeightForWidth())
        self.wb30.setSizePolicy(sizePolicy2)
        self.wb30.setMinimumSize(QSize(220, 200))
        self.wb30.setMaximumSize(QSize(220, 200))
        self.wb30.setStyleSheet(u"background-color:transparent;")

        self.verticalLayout_14.addWidget(self.wb30, 0, Qt.AlignmentFlag.AlignHCenter)

        self.widget_15 = QWidget(self.widget_14)
        self.widget_15.setObjectName(u"widget_15")
        self.btnAdd30 = QPushButton(self.widget_15)
        self.btnAdd30.setObjectName(u"btnAdd30")
        self.btnAdd30.setGeometry(QRect(60, 100, 151, 51))
        sizePolicy3.setHeightForWidth(self.btnAdd30.sizePolicy().hasHeightForWidth())
        self.btnAdd30.setSizePolicy(sizePolicy3)
        self.btnAdd30.setFont(font3)
        self.btnAdd30.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btnAdd30.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(255, 255, 255);\n"
"border-radius: 8px;\n"
"	color: rgb(65, 66, 63);\n"
"t\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(239, 50, 104); \n"
"    color: white;\n"
"}\n"
"QPushButton:checked{\n"
" background-color: rgb(239, 50, 104);\n"
" color: white;\n"
"}")
        self.lblCost30 = QLabel(self.widget_15)
        self.lblCost30.setObjectName(u"lblCost30")
        self.lblCost30.setGeometry(QRect(30, 10, 211, 76))
        self.lblCost30.setFont(font4)
        self.lblCost30.setStyleSheet(u"color: white;\n"
"text-align: center;\n"
"padding-left:10px;\n"
"font-size: 20px;")
        self.lblCost30.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_14.addWidget(self.widget_15)


        self.horizontalLayout_3.addWidget(self.widget_14)


        self.verticalLayout_6.addWidget(self.wg10)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_6.addItem(self.verticalSpacer)

        self.wg11 = QWidget(self.wdPicMenu)
        self.wg11.setObjectName(u"wg11")
        self.wg11.setMinimumSize(QSize(550, 400))
        self.horizontalLayout_10 = QHBoxLayout(self.wg11)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.widget_12 = QWidget(self.wg11)
        self.widget_12.setObjectName(u"widget_12")
        self.verticalLayout_36 = QVBoxLayout(self.widget_12)
        self.verticalLayout_36.setObjectName(u"verticalLayout_36")
        self.wb31 = QWidget(self.widget_12)
        self.wb31.setObjectName(u"wb31")
        sizePolicy2.setHeightForWidth(self.wb31.sizePolicy().hasHeightForWidth())
        self.wb31.setSizePolicy(sizePolicy2)
        self.wb31.setMinimumSize(QSize(220, 200))
        self.wb31.setMaximumSize(QSize(220, 200))
        self.wb31.setStyleSheet(u"background-color:transparent;")

        self.verticalLayout_36.addWidget(self.wb31, 0, Qt.AlignmentFlag.AlignHCenter)

        self.widget_62 = QWidget(self.widget_12)
        self.widget_62.setObjectName(u"widget_62")
        self.btnAdd31 = QPushButton(self.widget_62)
        self.btnAdd31.setObjectName(u"btnAdd31")
        self.btnAdd31.setGeometry(QRect(60, 100, 151, 51))
        sizePolicy3.setHeightForWidth(self.btnAdd31.sizePolicy().hasHeightForWidth())
        self.btnAdd31.setSizePolicy(sizePolicy3)
        self.btnAdd31.setFont(font3)
        self.btnAdd31.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btnAdd31.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(255, 255, 255);\n"
"border-radius: 8px;\n"
"	color: rgb(65, 66, 63);\n"
"t\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(239, 50, 104); \n"
"    color: white;\n"
"}\n"
"QPushButton:checked{\n"
" background-color: rgb(239, 50, 104);\n"
" color: white;\n"
"}")
        self.lblCost31 = QLabel(self.widget_62)
        self.lblCost31.setObjectName(u"lblCost31")
        self.lblCost31.setGeometry(QRect(30, 10, 211, 76))
        self.lblCost31.setFont(font4)
        self.lblCost31.setStyleSheet(u"color: white;\n"
"text-align: center;\n"
"padding-left:10px;\n"
"font-size: 20px;")
        self.lblCost31.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_36.addWidget(self.widget_62)


        self.horizontalLayout_10.addWidget(self.widget_12)

        self.widget_63 = QWidget(self.wg11)
        self.widget_63.setObjectName(u"widget_63")
        self.verticalLayout_37 = QVBoxLayout(self.widget_63)
        self.verticalLayout_37.setObjectName(u"verticalLayout_37")
        self.wb32 = QWidget(self.widget_63)
        self.wb32.setObjectName(u"wb32")
        sizePolicy2.setHeightForWidth(self.wb32.sizePolicy().hasHeightForWidth())
        self.wb32.setSizePolicy(sizePolicy2)
        self.wb32.setMinimumSize(QSize(220, 200))
        self.wb32.setMaximumSize(QSize(220, 200))
        self.wb32.setStyleSheet(u"background-color:transparent;")

        self.verticalLayout_37.addWidget(self.wb32, 0, Qt.AlignmentFlag.AlignHCenter)

        self.widget_65 = QWidget(self.widget_63)
        self.widget_65.setObjectName(u"widget_65")
        self.btnAdd32 = QPushButton(self.widget_65)
        self.btnAdd32.setObjectName(u"btnAdd32")
        self.btnAdd32.setGeometry(QRect(60, 100, 151, 51))
        sizePolicy3.setHeightForWidth(self.btnAdd32.sizePolicy().hasHeightForWidth())
        self.btnAdd32.setSizePolicy(sizePolicy3)
        self.btnAdd32.setFont(font3)
        self.btnAdd32.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btnAdd32.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(255, 255, 255);\n"
"border-radius: 8px;\n"
"	color: rgb(65, 66, 63);\n"
"t\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(239, 50, 104); \n"
"    color: white;\n"
"}\n"
"QPushButton:checked{\n"
" background-color: rgb(239, 50, 104);\n"
" color: white;\n"
"}")
        self.lblCost32 = QLabel(self.widget_65)
        self.lblCost32.setObjectName(u"lblCost32")
        self.lblCost32.setGeometry(QRect(30, 10, 211, 76))
        self.lblCost32.setFont(font4)
        self.lblCost32.setStyleSheet(u"color: white;\n"
"text-align: center;\n"
"padding-left:10px;\n"
"font-size: 20px;")
        self.lblCost32.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_37.addWidget(self.widget_65)


        self.horizontalLayout_10.addWidget(self.widget_63)

        self.widget_67 = QWidget(self.wg11)
        self.widget_67.setObjectName(u"widget_67")
        self.verticalLayout_40 = QVBoxLayout(self.widget_67)
        self.verticalLayout_40.setObjectName(u"verticalLayout_40")
        self.wb33 = QWidget(self.widget_67)
        self.wb33.setObjectName(u"wb33")
        sizePolicy2.setHeightForWidth(self.wb33.sizePolicy().hasHeightForWidth())
        self.wb33.setSizePolicy(sizePolicy2)
        self.wb33.setMinimumSize(QSize(220, 200))
        self.wb33.setMaximumSize(QSize(220, 200))
        self.wb33.setStyleSheet(u"background-color:transparent;")

        self.verticalLayout_40.addWidget(self.wb33, 0, Qt.AlignmentFlag.AlignHCenter)

        self.widget_68 = QWidget(self.widget_67)
        self.widget_68.setObjectName(u"widget_68")
        self.btnAdd33 = QPushButton(self.widget_68)
        self.btnAdd33.setObjectName(u"btnAdd33")
        self.btnAdd33.setGeometry(QRect(60, 100, 151, 51))
        sizePolicy3.setHeightForWidth(self.btnAdd33.sizePolicy().hasHeightForWidth())
        self.btnAdd33.setSizePolicy(sizePolicy3)
        self.btnAdd33.setFont(font3)
        self.btnAdd33.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btnAdd33.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(255, 255, 255);\n"
"border-radius: 8px;\n"
"	color: rgb(65, 66, 63);\n"
"t\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(239, 50, 104); \n"
"    color: white;\n"
"}\n"
"QPushButton:checked{\n"
" background-color: rgb(239, 50, 104);\n"
" color: white;\n"
"}")
        self.lblCost33 = QLabel(self.widget_68)
        self.lblCost33.setObjectName(u"lblCost33")
        self.lblCost33.setGeometry(QRect(30, 10, 211, 76))
        self.lblCost33.setFont(font4)
        self.lblCost33.setStyleSheet(u"color: white;\n"
"text-align: center;\n"
"padding-left:10px;\n"
"font-size: 20px;")
        self.lblCost33.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_40.addWidget(self.widget_68)


        self.horizontalLayout_10.addWidget(self.widget_67)


        self.verticalLayout_6.addWidget(self.wg11)

        self.verticalSpacer_6 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_6.addItem(self.verticalSpacer_6)

        self.wg12 = QWidget(self.wdPicMenu)
        self.wg12.setObjectName(u"wg12")
        self.wg12.setMinimumSize(QSize(550, 400))
        self.horizontalLayout_11 = QHBoxLayout(self.wg12)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.widget_69 = QWidget(self.wg12)
        self.widget_69.setObjectName(u"widget_69")
        self.verticalLayout_41 = QVBoxLayout(self.widget_69)
        self.verticalLayout_41.setObjectName(u"verticalLayout_41")
        self.wb34 = QWidget(self.widget_69)
        self.wb34.setObjectName(u"wb34")
        sizePolicy2.setHeightForWidth(self.wb34.sizePolicy().hasHeightForWidth())
        self.wb34.setSizePolicy(sizePolicy2)
        self.wb34.setMinimumSize(QSize(220, 200))
        self.wb34.setMaximumSize(QSize(220, 200))
        self.wb34.setStyleSheet(u"background-color:transparent;")

        self.verticalLayout_41.addWidget(self.wb34, 0, Qt.AlignmentFlag.AlignHCenter)

        self.widget_70 = QWidget(self.widget_69)
        self.widget_70.setObjectName(u"widget_70")
        self.btnAdd34 = QPushButton(self.widget_70)
        self.btnAdd34.setObjectName(u"btnAdd34")
        self.btnAdd34.setGeometry(QRect(60, 100, 151, 51))
        sizePolicy3.setHeightForWidth(self.btnAdd34.sizePolicy().hasHeightForWidth())
        self.btnAdd34.setSizePolicy(sizePolicy3)
        self.btnAdd34.setFont(font3)
        self.btnAdd34.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btnAdd34.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(255, 255, 255);\n"
"border-radius: 8px;\n"
"	color: rgb(65, 66, 63);\n"
"t\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(239, 50, 104); \n"
"    color: white;\n"
"}\n"
"QPushButton:checked{\n"
" background-color: rgb(239, 50, 104);\n"
" color: white;\n"
"}")
        self.lblCost34 = QLabel(self.widget_70)
        self.lblCost34.setObjectName(u"lblCost34")
        self.lblCost34.setGeometry(QRect(30, 10, 211, 76))
        self.lblCost34.setFont(font4)
        self.lblCost34.setStyleSheet(u"color: white;\n"
"text-align: center;\n"
"padding-left:10px;\n"
"font-size: 20px;")
        self.lblCost34.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_41.addWidget(self.widget_70)


        self.horizontalLayout_11.addWidget(self.widget_69)

        self.widget_71 = QWidget(self.wg12)
        self.widget_71.setObjectName(u"widget_71")
        self.verticalLayout_42 = QVBoxLayout(self.widget_71)
        self.verticalLayout_42.setObjectName(u"verticalLayout_42")
        self.wb35 = QWidget(self.widget_71)
        self.wb35.setObjectName(u"wb35")
        sizePolicy2.setHeightForWidth(self.wb35.sizePolicy().hasHeightForWidth())
        self.wb35.setSizePolicy(sizePolicy2)
        self.wb35.setMinimumSize(QSize(220, 200))
        self.wb35.setMaximumSize(QSize(220, 200))
        self.wb35.setStyleSheet(u"background-color:transparent;")

        self.verticalLayout_42.addWidget(self.wb35, 0, Qt.AlignmentFlag.AlignHCenter)

        self.widget_72 = QWidget(self.widget_71)
        self.widget_72.setObjectName(u"widget_72")
        self.btnAdd35 = QPushButton(self.widget_72)
        self.btnAdd35.setObjectName(u"btnAdd35")
        self.btnAdd35.setGeometry(QRect(60, 100, 151, 51))
        sizePolicy3.setHeightForWidth(self.btnAdd35.sizePolicy().hasHeightForWidth())
        self.btnAdd35.setSizePolicy(sizePolicy3)
        self.btnAdd35.setFont(font3)
        self.btnAdd35.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btnAdd35.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(255, 255, 255);\n"
"border-radius: 8px;\n"
"	color: rgb(65, 66, 63);\n"
"t\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(239, 50, 104); \n"
"    color: white;\n"
"}\n"
"QPushButton:checked{\n"
" background-color: rgb(239, 50, 104);\n"
" color: white;\n"
"}")
        self.lblCost35 = QLabel(self.widget_72)
        self.lblCost35.setObjectName(u"lblCost35")
        self.lblCost35.setGeometry(QRect(30, 10, 211, 76))
        self.lblCost35.setFont(font4)
        self.lblCost35.setStyleSheet(u"color: white;\n"
"text-align: center;\n"
"padding-left:10px;\n"
"font-size: 20px;")
        self.lblCost35.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_42.addWidget(self.widget_72)


        self.horizontalLayout_11.addWidget(self.widget_71)

        self.widget_73 = QWidget(self.wg12)
        self.widget_73.setObjectName(u"widget_73")
        self.verticalLayout_43 = QVBoxLayout(self.widget_73)
        self.verticalLayout_43.setObjectName(u"verticalLayout_43")
        self.wb36 = QWidget(self.widget_73)
        self.wb36.setObjectName(u"wb36")
        sizePolicy2.setHeightForWidth(self.wb36.sizePolicy().hasHeightForWidth())
        self.wb36.setSizePolicy(sizePolicy2)
        self.wb36.setMinimumSize(QSize(220, 200))
        self.wb36.setMaximumSize(QSize(220, 200))
        self.wb36.setStyleSheet(u"background-color:transparent;")

        self.verticalLayout_43.addWidget(self.wb36, 0, Qt.AlignmentFlag.AlignHCenter)

        self.widget_74 = QWidget(self.widget_73)
        self.widget_74.setObjectName(u"widget_74")
        self.btnAdd36 = QPushButton(self.widget_74)
        self.btnAdd36.setObjectName(u"btnAdd36")
        self.btnAdd36.setGeometry(QRect(60, 100, 151, 51))
        sizePolicy3.setHeightForWidth(self.btnAdd36.sizePolicy().hasHeightForWidth())
        self.btnAdd36.setSizePolicy(sizePolicy3)
        self.btnAdd36.setFont(font3)
        self.btnAdd36.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btnAdd36.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(255, 255, 255);\n"
"border-radius: 8px;\n"
"	color: rgb(65, 66, 63);\n"
"t\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(239, 50, 104); \n"
"    color: white;\n"
"}\n"
"QPushButton:checked{\n"
" background-color: rgb(239, 50, 104);\n"
" color: white;\n"
"}")
        self.lblCost36 = QLabel(self.widget_74)
        self.lblCost36.setObjectName(u"lblCost36")
        self.lblCost36.setGeometry(QRect(30, 10, 211, 76))
        self.lblCost36.setFont(font4)
        self.lblCost36.setStyleSheet(u"color: white;\n"
"text-align: center;\n"
"padding-left:10px;\n"
"font-size: 20px;")
        self.lblCost36.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_43.addWidget(self.widget_74)


        self.horizontalLayout_11.addWidget(self.widget_73)


        self.verticalLayout_6.addWidget(self.wg12)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_6.addItem(self.verticalSpacer_4)

        self.wg13 = QWidget(self.wdPicMenu)
        self.wg13.setObjectName(u"wg13")
        self.wg13.setMinimumSize(QSize(550, 400))
        self.horizontalLayout_13 = QHBoxLayout(self.wg13)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.widget_75 = QWidget(self.wg13)
        self.widget_75.setObjectName(u"widget_75")
        self.verticalLayout_44 = QVBoxLayout(self.widget_75)
        self.verticalLayout_44.setObjectName(u"verticalLayout_44")
        self.wb37 = QWidget(self.widget_75)
        self.wb37.setObjectName(u"wb37")
        sizePolicy2.setHeightForWidth(self.wb37.sizePolicy().hasHeightForWidth())
        self.wb37.setSizePolicy(sizePolicy2)
        self.wb37.setMinimumSize(QSize(220, 200))
        self.wb37.setMaximumSize(QSize(220, 200))
        self.wb37.setStyleSheet(u"background-color:transparent;")

        self.verticalLayout_44.addWidget(self.wb37, 0, Qt.AlignmentFlag.AlignHCenter)

        self.widget_76 = QWidget(self.widget_75)
        self.widget_76.setObjectName(u"widget_76")
        self.btnAdd37 = QPushButton(self.widget_76)
        self.btnAdd37.setObjectName(u"btnAdd37")
        self.btnAdd37.setGeometry(QRect(60, 100, 151, 51))
        sizePolicy3.setHeightForWidth(self.btnAdd37.sizePolicy().hasHeightForWidth())
        self.btnAdd37.setSizePolicy(sizePolicy3)
        self.btnAdd37.setFont(font3)
        self.btnAdd37.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btnAdd37.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(255, 255, 255);\n"
"border-radius: 8px;\n"
"	color: rgb(65, 66, 63);\n"
"t\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(239, 50, 104); \n"
"    color: white;\n"
"}\n"
"QPushButton:checked{\n"
" background-color: rgb(239, 50, 104);\n"
" color: white;\n"
"}")
        self.lblCost37 = QLabel(self.widget_76)
        self.lblCost37.setObjectName(u"lblCost37")
        self.lblCost37.setGeometry(QRect(30, 10, 211, 76))
        self.lblCost37.setFont(font4)
        self.lblCost37.setStyleSheet(u"color: white;\n"
"text-align: center;\n"
"padding-left:10px;\n"
"font-size: 20px;")
        self.lblCost37.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_44.addWidget(self.widget_76)


        self.horizontalLayout_13.addWidget(self.widget_75)

        self.widget_77 = QWidget(self.wg13)
        self.widget_77.setObjectName(u"widget_77")
        self.verticalLayout_45 = QVBoxLayout(self.widget_77)
        self.verticalLayout_45.setObjectName(u"verticalLayout_45")
        self.wb38 = QWidget(self.widget_77)
        self.wb38.setObjectName(u"wb38")
        sizePolicy2.setHeightForWidth(self.wb38.sizePolicy().hasHeightForWidth())
        self.wb38.setSizePolicy(sizePolicy2)
        self.wb38.setMinimumSize(QSize(220, 200))
        self.wb38.setMaximumSize(QSize(220, 200))
        self.wb38.setStyleSheet(u"background-color:transparent;")

        self.verticalLayout_45.addWidget(self.wb38, 0, Qt.AlignmentFlag.AlignHCenter)

        self.widget_78 = QWidget(self.widget_77)
        self.widget_78.setObjectName(u"widget_78")
        self.btnAdd38 = QPushButton(self.widget_78)
        self.btnAdd38.setObjectName(u"btnAdd38")
        self.btnAdd38.setGeometry(QRect(60, 100, 151, 51))
        sizePolicy3.setHeightForWidth(self.btnAdd38.sizePolicy().hasHeightForWidth())
        self.btnAdd38.setSizePolicy(sizePolicy3)
        self.btnAdd38.setFont(font3)
        self.btnAdd38.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btnAdd38.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(255, 255, 255);\n"
"border-radius: 8px;\n"
"	color: rgb(65, 66, 63);\n"
"t\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(239, 50, 104); \n"
"    color: white;\n"
"}\n"
"QPushButton:checked{\n"
" background-color: rgb(239, 50, 104);\n"
" color: white;\n"
"}")
        self.lblCost38 = QLabel(self.widget_78)
        self.lblCost38.setObjectName(u"lblCost38")
        self.lblCost38.setGeometry(QRect(30, 10, 211, 76))
        self.lblCost38.setFont(font4)
        self.lblCost38.setStyleSheet(u"color: white;\n"
"text-align: center;\n"
"padding-left:10px;\n"
"font-size: 20px;")
        self.lblCost38.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_45.addWidget(self.widget_78)


        self.horizontalLayout_13.addWidget(self.widget_77)

        self.widget_79 = QWidget(self.wg13)
        self.widget_79.setObjectName(u"widget_79")
        self.verticalLayout_46 = QVBoxLayout(self.widget_79)
        self.verticalLayout_46.setObjectName(u"verticalLayout_46")
        self.wb39 = QWidget(self.widget_79)
        self.wb39.setObjectName(u"wb39")
        sizePolicy2.setHeightForWidth(self.wb39.sizePolicy().hasHeightForWidth())
        self.wb39.setSizePolicy(sizePolicy2)
        self.wb39.setMinimumSize(QSize(220, 200))
        self.wb39.setMaximumSize(QSize(220, 200))
        self.wb39.setStyleSheet(u"background-color:transparent;")

        self.verticalLayout_46.addWidget(self.wb39, 0, Qt.AlignmentFlag.AlignHCenter)

        self.widget_80 = QWidget(self.widget_79)
        self.widget_80.setObjectName(u"widget_80")
        self.btnAdd39 = QPushButton(self.widget_80)
        self.btnAdd39.setObjectName(u"btnAdd39")
        self.btnAdd39.setGeometry(QRect(60, 100, 151, 51))
        sizePolicy3.setHeightForWidth(self.btnAdd39.sizePolicy().hasHeightForWidth())
        self.btnAdd39.setSizePolicy(sizePolicy3)
        self.btnAdd39.setFont(font3)
        self.btnAdd39.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btnAdd39.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(255, 255, 255);\n"
"border-radius: 8px;\n"
"	color: rgb(65, 66, 63);\n"
"t\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(239, 50, 104); \n"
"    color: white;\n"
"}\n"
"QPushButton:checked{\n"
" background-color: rgb(239, 50, 104);\n"
" color: white;\n"
"}")
        self.lblCost39 = QLabel(self.widget_80)
        self.lblCost39.setObjectName(u"lblCost39")
        self.lblCost39.setGeometry(QRect(30, 10, 211, 76))
        self.lblCost39.setFont(font4)
        self.lblCost39.setStyleSheet(u"color: white;\n"
"text-align: center;\n"
"padding-left:10px;\n"
"font-size: 20px;")
        self.lblCost39.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_46.addWidget(self.widget_80)


        self.horizontalLayout_13.addWidget(self.widget_79)


        self.verticalLayout_6.addWidget(self.wg13)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_6.addItem(self.verticalSpacer_3)

        self.wg14 = QWidget(self.wdPicMenu)
        self.wg14.setObjectName(u"wg14")
        self.wg14.setMinimumSize(QSize(550, 400))
        self.horizontalLayout_14 = QHBoxLayout(self.wg14)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.widget_81 = QWidget(self.wg14)
        self.widget_81.setObjectName(u"widget_81")
        self.verticalLayout_47 = QVBoxLayout(self.widget_81)
        self.verticalLayout_47.setObjectName(u"verticalLayout_47")
        self.wb40 = QWidget(self.widget_81)
        self.wb40.setObjectName(u"wb40")
        sizePolicy2.setHeightForWidth(self.wb40.sizePolicy().hasHeightForWidth())
        self.wb40.setSizePolicy(sizePolicy2)
        self.wb40.setMinimumSize(QSize(220, 200))
        self.wb40.setMaximumSize(QSize(220, 200))
        self.wb40.setStyleSheet(u"background-color:transparent;")

        self.verticalLayout_47.addWidget(self.wb40, 0, Qt.AlignmentFlag.AlignHCenter)

        self.widget_82 = QWidget(self.widget_81)
        self.widget_82.setObjectName(u"widget_82")
        self.btnAdd40 = QPushButton(self.widget_82)
        self.btnAdd40.setObjectName(u"btnAdd40")
        self.btnAdd40.setGeometry(QRect(60, 100, 151, 51))
        sizePolicy3.setHeightForWidth(self.btnAdd40.sizePolicy().hasHeightForWidth())
        self.btnAdd40.setSizePolicy(sizePolicy3)
        self.btnAdd40.setFont(font3)
        self.btnAdd40.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btnAdd40.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(255, 255, 255);\n"
"border-radius: 8px;\n"
"	color: rgb(65, 66, 63);\n"
"t\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(239, 50, 104); \n"
"    color: white;\n"
"}\n"
"QPushButton:checked{\n"
" background-color: rgb(239, 50, 104);\n"
" color: white;\n"
"}")
        self.lblCost40 = QLabel(self.widget_82)
        self.lblCost40.setObjectName(u"lblCost40")
        self.lblCost40.setGeometry(QRect(30, 10, 211, 76))
        self.lblCost40.setFont(font4)
        self.lblCost40.setStyleSheet(u"color: white;\n"
"text-align: center;\n"
"padding-left:10px;\n"
"font-size: 20px;")
        self.lblCost40.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_47.addWidget(self.widget_82)


        self.horizontalLayout_14.addWidget(self.widget_81)

        self.widget_83 = QWidget(self.wg14)
        self.widget_83.setObjectName(u"widget_83")
        self.verticalLayout_48 = QVBoxLayout(self.widget_83)
        self.verticalLayout_48.setObjectName(u"verticalLayout_48")
        self.wb41 = QWidget(self.widget_83)
        self.wb41.setObjectName(u"wb41")
        sizePolicy2.setHeightForWidth(self.wb41.sizePolicy().hasHeightForWidth())
        self.wb41.setSizePolicy(sizePolicy2)
        self.wb41.setMinimumSize(QSize(220, 200))
        self.wb41.setMaximumSize(QSize(220, 200))
        self.wb41.setStyleSheet(u"background-color:transparent;")

        self.verticalLayout_48.addWidget(self.wb41, 0, Qt.AlignmentFlag.AlignHCenter)

        self.widget_84 = QWidget(self.widget_83)
        self.widget_84.setObjectName(u"widget_84")
        self.btnAdd41 = QPushButton(self.widget_84)
        self.btnAdd41.setObjectName(u"btnAdd41")
        self.btnAdd41.setGeometry(QRect(60, 100, 151, 51))
        sizePolicy3.setHeightForWidth(self.btnAdd41.sizePolicy().hasHeightForWidth())
        self.btnAdd41.setSizePolicy(sizePolicy3)
        self.btnAdd41.setFont(font3)
        self.btnAdd41.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btnAdd41.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(255, 255, 255);\n"
"border-radius: 8px;\n"
"	color: rgb(65, 66, 63);\n"
"t\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(239, 50, 104); \n"
"    color: white;\n"
"}\n"
"QPushButton:checked{\n"
" background-color: rgb(239, 50, 104);\n"
" color: white;\n"
"}")
        self.lblCost41 = QLabel(self.widget_84)
        self.lblCost41.setObjectName(u"lblCost41")
        self.lblCost41.setGeometry(QRect(30, 10, 211, 76))
        self.lblCost41.setFont(font4)
        self.lblCost41.setStyleSheet(u"color: white;\n"
"text-align: center;\n"
"padding-left:10px;\n"
"font-size: 20px;")
        self.lblCost41.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_48.addWidget(self.widget_84)


        self.horizontalLayout_14.addWidget(self.widget_83)

        self.widget_85 = QWidget(self.wg14)
        self.widget_85.setObjectName(u"widget_85")
        self.verticalLayout_49 = QVBoxLayout(self.widget_85)
        self.verticalLayout_49.setObjectName(u"verticalLayout_49")
        self.wb42 = QWidget(self.widget_85)
        self.wb42.setObjectName(u"wb42")
        sizePolicy2.setHeightForWidth(self.wb42.sizePolicy().hasHeightForWidth())
        self.wb42.setSizePolicy(sizePolicy2)
        self.wb42.setMinimumSize(QSize(220, 200))
        self.wb42.setMaximumSize(QSize(220, 200))
        self.wb42.setStyleSheet(u"background-color:transparent;")

        self.verticalLayout_49.addWidget(self.wb42, 0, Qt.AlignmentFlag.AlignHCenter)

        self.widget_86 = QWidget(self.widget_85)
        self.widget_86.setObjectName(u"widget_86")
        self.btnAdd42 = QPushButton(self.widget_86)
        self.btnAdd42.setObjectName(u"btnAdd42")
        self.btnAdd42.setGeometry(QRect(60, 100, 151, 51))
        sizePolicy3.setHeightForWidth(self.btnAdd42.sizePolicy().hasHeightForWidth())
        self.btnAdd42.setSizePolicy(sizePolicy3)
        self.btnAdd42.setFont(font3)
        self.btnAdd42.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btnAdd42.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(255, 255, 255);\n"
"border-radius: 8px;\n"
"	color: rgb(65, 66, 63);\n"
"t\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(239, 50, 104); \n"
"    color: white;\n"
"}\n"
"QPushButton:checked{\n"
" background-color: rgb(239, 50, 104);\n"
" color: white;\n"
"}")
        self.lblCost42 = QLabel(self.widget_86)
        self.lblCost42.setObjectName(u"lblCost42")
        self.lblCost42.setGeometry(QRect(30, 10, 211, 76))
        self.lblCost42.setFont(font4)
        self.lblCost42.setStyleSheet(u"color: white;   \n"
"text-align: center;\n"
"padding-left:10px;\n"
"font-size: 20px;")
        self.lblCost42.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_49.addWidget(self.widget_86)


        self.horizontalLayout_14.addWidget(self.widget_85)


        self.verticalLayout_6.addWidget(self.wg14)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_6.addItem(self.verticalSpacer_2)

        self.wg15 = QWidget(self.wdPicMenu)
        self.wg15.setObjectName(u"wg15")
        self.wg15.setMinimumSize(QSize(550, 400))
        self.horizontalLayout_15 = QHBoxLayout(self.wg15)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.widget_87 = QWidget(self.wg15)
        self.widget_87.setObjectName(u"widget_87")
        self.verticalLayout_50 = QVBoxLayout(self.widget_87)
        self.verticalLayout_50.setObjectName(u"verticalLayout_50")
        self.wb45 = QWidget(self.widget_87)
        self.wb45.setObjectName(u"wb45")
        sizePolicy2.setHeightForWidth(self.wb45.sizePolicy().hasHeightForWidth())
        self.wb45.setSizePolicy(sizePolicy2)
        self.wb45.setMinimumSize(QSize(220, 200))
        self.wb45.setMaximumSize(QSize(220, 200))
        self.wb45.setStyleSheet(u"background-color:transparent;")

        self.verticalLayout_50.addWidget(self.wb45, 0, Qt.AlignmentFlag.AlignHCenter)

        self.widget_88 = QWidget(self.widget_87)
        self.widget_88.setObjectName(u"widget_88")
        self.btnAdd45 = QPushButton(self.widget_88)
        self.btnAdd45.setObjectName(u"btnAdd45")
        self.btnAdd45.setGeometry(QRect(60, 100, 151, 51))
        sizePolicy3.setHeightForWidth(self.btnAdd45.sizePolicy().hasHeightForWidth())
        self.btnAdd45.setSizePolicy(sizePolicy3)
        self.btnAdd45.setFont(font3)
        self.btnAdd45.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btnAdd45.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(255, 255, 255);\n"
"border-radius: 8px;\n"
"	color: rgb(65, 66, 63);\n"
"t\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(239, 50, 104); \n"
"    color: white;\n"
"}\n"
"QPushButton:checked{\n"
" background-color: rgb(239, 50, 104);\n"
" color: white;\n"
"}")
        self.lblCost45 = QLabel(self.widget_88)
        self.lblCost45.setObjectName(u"lblCost45")
        self.lblCost45.setGeometry(QRect(30, 10, 211, 76))
        self.lblCost45.setFont(font4)
        self.lblCost45.setStyleSheet(u"color: white;\n"
"text-align: center;\n"
"padding-left:10px;\n"
"font-size: 20px;")
        self.lblCost45.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_50.addWidget(self.widget_88)


        self.horizontalLayout_15.addWidget(self.widget_87)

        self.widget_89 = QWidget(self.wg15)
        self.widget_89.setObjectName(u"widget_89")
        self.verticalLayout_51 = QVBoxLayout(self.widget_89)
        self.verticalLayout_51.setObjectName(u"verticalLayout_51")
        self.wb46 = QWidget(self.widget_89)
        self.wb46.setObjectName(u"wb46")
        sizePolicy2.setHeightForWidth(self.wb46.sizePolicy().hasHeightForWidth())
        self.wb46.setSizePolicy(sizePolicy2)
        self.wb46.setMinimumSize(QSize(220, 200))
        self.wb46.setMaximumSize(QSize(220, 200))
        self.wb46.setStyleSheet(u"background-color:transparent;")

        self.verticalLayout_51.addWidget(self.wb46, 0, Qt.AlignmentFlag.AlignHCenter)

        self.widget_90 = QWidget(self.widget_89)
        self.widget_90.setObjectName(u"widget_90")
        self.btnAdd47 = QPushButton(self.widget_90)
        self.btnAdd47.setObjectName(u"btnAdd47")
        self.btnAdd47.setGeometry(QRect(60, 100, 151, 51))
        sizePolicy3.setHeightForWidth(self.btnAdd47.sizePolicy().hasHeightForWidth())
        self.btnAdd47.setSizePolicy(sizePolicy3)
        self.btnAdd47.setFont(font3)
        self.btnAdd47.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btnAdd47.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(255, 255, 255);\n"
"border-radius: 8px;\n"
"	color: rgb(65, 66, 63);\n"
"t\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(239, 50, 104); \n"
"    color: white;\n"
"}\n"
"QPushButton:checked{\n"
" background-color: rgb(239, 50, 104);\n"
" color: white;\n"
"}")
        self.lblCost48 = QLabel(self.widget_90)
        self.lblCost48.setObjectName(u"lblCost48")
        self.lblCost48.setGeometry(QRect(30, 10, 211, 76))
        self.lblCost48.setFont(font4)
        self.lblCost48.setStyleSheet(u"color: white;\n"
"text-align: center;\n"
"padding-left:10px;\n"
"font-size: 20px;")
        self.lblCost48.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_51.addWidget(self.widget_90)


        self.horizontalLayout_15.addWidget(self.widget_89)

        self.widget_91 = QWidget(self.wg15)
        self.widget_91.setObjectName(u"widget_91")
        self.verticalLayout_52 = QVBoxLayout(self.widget_91)
        self.verticalLayout_52.setObjectName(u"verticalLayout_52")
        self.wb49 = QWidget(self.widget_91)
        self.wb49.setObjectName(u"wb49")
        sizePolicy2.setHeightForWidth(self.wb49.sizePolicy().hasHeightForWidth())
        self.wb49.setSizePolicy(sizePolicy2)
        self.wb49.setMinimumSize(QSize(220, 200))
        self.wb49.setMaximumSize(QSize(220, 200))
        self.wb49.setStyleSheet(u"background-color:transparent;")

        self.verticalLayout_52.addWidget(self.wb49, 0, Qt.AlignmentFlag.AlignHCenter)

        self.widget_92 = QWidget(self.widget_91)
        self.widget_92.setObjectName(u"widget_92")
        self.btnAdd49 = QPushButton(self.widget_92)
        self.btnAdd49.setObjectName(u"btnAdd49")
        self.btnAdd49.setGeometry(QRect(60, 100, 151, 51))
        sizePolicy3.setHeightForWidth(self.btnAdd49.sizePolicy().hasHeightForWidth())
        self.btnAdd49.setSizePolicy(sizePolicy3)
        self.btnAdd49.setFont(font3)
        self.btnAdd49.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btnAdd49.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(255, 255, 255);\n"
"border-radius: 8px;\n"
"	color: rgb(65, 66, 63);\n"
"t\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(239, 50, 104); \n"
"    color: white;\n"
"}\n"
"QPushButton:checked{\n"
" background-color: rgb(239, 50, 104);\n"
" color: white;\n"
"}")
        self.lblCost49 = QLabel(self.widget_92)
        self.lblCost49.setObjectName(u"lblCost49")
        self.lblCost49.setGeometry(QRect(30, 10, 211, 76))
        self.lblCost49.setFont(font4)
        self.lblCost49.setStyleSheet(u"color: white;\n"
"text-align: center;\n"
"padding-left:10px;\n"
"font-size: 20px;")
        self.lblCost49.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_52.addWidget(self.widget_92)


        self.horizontalLayout_15.addWidget(self.widget_91)


        self.verticalLayout_6.addWidget(self.wg15)


        self.verticalLayout_3.addWidget(self.wdPicMenu, 0, Qt.AlignmentFlag.AlignHCenter)

        self.scrollMenu.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout.addWidget(self.scrollMenu)


        self.verticalLayout_4.addWidget(self.widget)

        self.stackedWidget.addWidget(self.pageMenu)
        self.pageLogin = QWidget()
        self.pageLogin.setObjectName(u"pageLogin")
        self.verticalLayout_60 = QVBoxLayout(self.pageLogin)
        self.verticalLayout_60.setObjectName(u"verticalLayout_60")
        self.stackedWidget.addWidget(self.pageLogin)
        self.pageOrder = QWidget()
        self.pageOrder.setObjectName(u"pageOrder")
        self.verticalLayout_2 = QVBoxLayout(self.pageOrder)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 50)
        self.widget_48 = QWidget(self.pageOrder)
        self.widget_48.setObjectName(u"widget_48")
        self.widget_48.setMinimumSize(QSize(900, 70))
        self.widget_48.setMaximumSize(QSize(16777215, 70))
        self.widget_48.setStyleSheet(u"border-bottom: 2px solid \n"
" rgb(65, 66, 63);")
        self.lblCoffee_9 = QLabel(self.widget_48)
        self.lblCoffee_9.setObjectName(u"lblCoffee_9")
        self.lblCoffee_9.setGeometry(QRect(100, -10, 341, 41))
        font5 = QFont()
        font5.setFamilies([u"8-bit Arcade In"])
        font5.setPointSize(36)
        font5.setWeight(QFont.Medium)
        font5.setItalic(False)
        font5.setUnderline(False)
        font5.setStrikeOut(False)
        font5.setKerning(True)
        font5.setStyleStrategy(QFont.PreferAntialias)
        font5.setHintingPreference(QFont.PreferDefaultHinting)
        self.lblCoffee_9.setFont(font5)
        self.lblCoffee_9.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"border: none;\n"
"font: 500 36pt \"8-bit Arcade In\";")
        self.lblCoffee_9.setTextFormat(Qt.TextFormat.PlainText)
        self.lblCoffee_9.setScaledContents(False)
        self.lblCoffee_9.setWordWrap(False)
        self.lblCoffee_9.setOpenExternalLinks(False)
        self.lblCoffee_10 = QLabel(self.widget_48)
        self.lblCoffee_10.setObjectName(u"lblCoffee_10")
        self.lblCoffee_10.setGeometry(QRect(100, 40, 261, 16))
        self.lblCoffee_10.setFont(font2)
        self.lblCoffee_10.setStyleSheet(u"border: none;\n"
"color: rgb(255, 255, 255);")
        self.lblCoffee_10.setTextFormat(Qt.TextFormat.PlainText)
        self.lblCoffee_10.setScaledContents(False)
        self.lblCoffee_10.setWordWrap(False)
        self.lblCoffee_10.setOpenExternalLinks(False)

        self.verticalLayout_2.addWidget(self.widget_48, 0, Qt.AlignmentFlag.AlignTop)

        self.widget_64 = QWidget(self.pageOrder)
        self.widget_64.setObjectName(u"widget_64")
        sizePolicy.setHeightForWidth(self.widget_64.sizePolicy().hasHeightForWidth())
        self.widget_64.setSizePolicy(sizePolicy)
        self.widget_64.setMinimumSize(QSize(1200, 600))
        self.widget_64.setMaximumSize(QSize(16777215, 16777215))
        self.widget_64.setStyleSheet(u"")
        self.verticalLayout_28 = QVBoxLayout(self.widget_64)
        self.verticalLayout_28.setSpacing(0)
        self.verticalLayout_28.setObjectName(u"verticalLayout_28")
        self.verticalLayout_28.setContentsMargins(-1, 0, -1, 0)
        self.WgPWG = QWidget(self.widget_64)
        self.WgPWG.setObjectName(u"WgPWG")
        sizePolicy1.setHeightForWidth(self.WgPWG.sizePolicy().hasHeightForWidth())
        self.WgPWG.setSizePolicy(sizePolicy1)
        self.WgPWG.setMinimumSize(QSize(1200, 600))
        self.WgPWG.setMaximumSize(QSize(1200, 600))
        self.WgPWG.setStyleSheet(u"QWidget#WgPWG{\n"
"border:none\n"
"border-radius:30px;\n"
"}")
        self.scrollArea_2 = QScrollArea(self.WgPWG)
        self.scrollArea_2.setObjectName(u"scrollArea_2")
        self.scrollArea_2.setGeometry(QRect(40, 10, 1100, 560))
        self.scrollArea_2.setMinimumSize(QSize(1100, 560))
        self.scrollArea_2.setMaximumSize(QSize(1100, 560))
        self.scrollArea_2.setStyleSheet(u"border:none;")
        self.scrollArea_2.setFrameShape(QFrame.Shape.Panel)
        self.scrollArea_2.setFrameShadow(QFrame.Shadow.Plain)
        self.scrollArea_2.setLineWidth(1)
        self.scrollArea_2.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.scrollArea_2.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollAreaWidgetContents_4 = QWidget()
        self.scrollAreaWidgetContents_4.setObjectName(u"scrollAreaWidgetContents_4")
        self.scrollAreaWidgetContents_4.setGeometry(QRect(0, 0, 1150, 842))
        self.verticalLayout_63 = QVBoxLayout(self.scrollAreaWidgetContents_4)
        self.verticalLayout_63.setObjectName(u"verticalLayout_63")
        self.verticalLayout_63.setContentsMargins(0, -1, 0, -1)
        self.P2wglb1 = QWidget(self.scrollAreaWidgetContents_4)
        self.P2wglb1.setObjectName(u"P2wglb1")
        sizePolicy1.setHeightForWidth(self.P2wglb1.sizePolicy().hasHeightForWidth())
        self.P2wglb1.setSizePolicy(sizePolicy1)
        self.P2wglb1.setMinimumSize(QSize(1150, 160))
        self.P2wglb1.setStyleSheet(u"")
        self.pwg1 = QWidget(self.P2wglb1)
        self.pwg1.setObjectName(u"pwg1")
        self.pwg1.setGeometry(QRect(10, 20, 120, 120))
        self.pwg1.setStyleSheet(u"border-radius:60px;\n"
"background-color: transparent;")
        self.pwg2 = QWidget(self.P2wglb1)
        self.pwg2.setObjectName(u"pwg2")
        self.pwg2.setGeometry(QRect(380, 20, 120, 120))
        self.pwg2.setStyleSheet(u"border-radius:60px;\n"
"background-color: transparent;")
        self.pwg3 = QWidget(self.P2wglb1)
        self.pwg3.setObjectName(u"pwg3")
        self.pwg3.setGeometry(QRect(750, 20, 120, 120))
        self.pwg3.setStyleSheet(u"border-radius:60px;\n"
"background-color: transparent;")
        self.lbname1 = QLabel(self.P2wglb1)
        self.lbname1.setObjectName(u"lbname1")
        self.lbname1.setGeometry(QRect(140, 20, 191, 21))
        font6 = QFont()
        font6.setPointSize(12)
        font6.setBold(True)
        font6.setItalic(False)
        self.lbname1.setFont(font6)
        self.lbname1.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.lbgia1 = QLabel(self.P2wglb1)
        self.lbgia1.setObjectName(u"lbgia1")
        self.lbgia1.setGeometry(QRect(140, 50, 191, 21))
        self.lbgia1.setFont(font6)
        self.lbgia1.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.lbgia3 = QLabel(self.P2wglb1)
        self.lbgia3.setObjectName(u"lbgia3")
        self.lbgia3.setGeometry(QRect(880, 50, 191, 21))
        self.lbgia3.setFont(font6)
        self.lbgia3.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.lbname3 = QLabel(self.P2wglb1)
        self.lbname3.setObjectName(u"lbname3")
        self.lbname3.setGeometry(QRect(880, 20, 191, 21))
        self.lbname3.setFont(font6)
        self.lbname3.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.lbgia2 = QLabel(self.P2wglb1)
        self.lbgia2.setObjectName(u"lbgia2")
        self.lbgia2.setGeometry(QRect(510, 50, 191, 21))
        self.lbgia2.setFont(font6)
        self.lbgia2.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.lbname2 = QLabel(self.P2wglb1)
        self.lbname2.setObjectName(u"lbname2")
        self.lbname2.setGeometry(QRect(510, 20, 191, 21))
        self.lbname2.setFont(font6)
        self.lbname2.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.spinBox1 = QSpinBox(self.P2wglb1)
        self.spinBox1.setObjectName(u"spinBox1")
        self.spinBox1.setGeometry(QRect(140, 100, 71, 31))
        self.spinBox1.setStyleSheet(u"QSpinBox {\n"
"    background: rgb(65, 66, 63);\n"
"    color: white;\n"
"    border: 2px solid #ccc;\n"
"    border-radius: 4px;\n"
"    padding: 5px 10px;\n"
"    font-size: 16px;\n"
"}\n"
"\n"
"QSpinBox::up-button, QSpinBox::down-button {\n"
"	background-color: rgb(107, 109, 104);\n"
"    border: none;\n"
"    width: 16px;\n"
"}\n"
"\n"
"QSpinBox::up-button:hover, QSpinBox::down-button:hover {\n"
"    background: rgba(255, 255, 255, 0.2);\n"
"}\n"
"\n"
"QSpinBox::up-arrow {\n"
"    image: url(:/icons/up-arrow.png);\n"
"}\n"
"\n"
"QSpinBox::down-arrow {\n"
"    image: url(:/icons/down-arrow.png);\n"
"}\n"
"")
        self.spinBox2 = QSpinBox(self.P2wglb1)
        self.spinBox2.setObjectName(u"spinBox2")
        self.spinBox2.setGeometry(QRect(510, 100, 71, 31))
        self.spinBox2.setStyleSheet(u"QSpinBox {\n"
"    background: rgb(65, 66, 63);\n"
"    color: white;\n"
"    border: 2px solid #ccc;\n"
"    border-radius: 4px;\n"
"    padding: 5px 10px;\n"
"    font-size: 16px;\n"
"}\n"
"\n"
"QSpinBox::up-button, QSpinBox::down-button {\n"
"	background-color: rgb(107, 109, 104);\n"
"    border: none;\n"
"    width: 16px;\n"
"}\n"
"\n"
"QSpinBox::up-button:hover, QSpinBox::down-button:hover {\n"
"    background: rgba(255, 255, 255, 0.2);\n"
"}\n"
"\n"
"QSpinBox::up-arrow {\n"
"    image: url(:/icons/up-arrow.png);\n"
"}\n"
"\n"
"QSpinBox::down-arrow {\n"
"    image: url(:/icons/down-arrow.png);\n"
"}\n"
"")
        self.spinBox3 = QSpinBox(self.P2wglb1)
        self.spinBox3.setObjectName(u"spinBox3")
        self.spinBox3.setGeometry(QRect(880, 100, 71, 31))
        self.spinBox3.setStyleSheet(u"QSpinBox {\n"
"    background: rgb(65, 66, 63);\n"
"    color: white;\n"
"    border: 2px solid #ccc;\n"
"    border-radius: 4px;\n"
"    padding: 5px 10px;\n"
"    font-size: 16px;\n"
"}\n"
"\n"
"QSpinBox::up-button, QSpinBox::down-button {\n"
"	background-color: rgb(107, 109, 104);\n"
"    border: none;\n"
"    width: 16px;\n"
"}\n"
"\n"
"QSpinBox::up-button:hover, QSpinBox::down-button:hover {\n"
"    background: rgba(255, 255, 255, 0.2);\n"
"}\n"
"\n"
"QSpinBox::up-arrow {\n"
"    image: url(:/icons/up-arrow.png);\n"
"}\n"
"\n"
"QSpinBox::down-arrow {\n"
"    image: url(:/icons/down-arrow.png);\n"
"}\n"
"")

        self.verticalLayout_63.addWidget(self.P2wglb1)

        self.P2wglb2 = QWidget(self.scrollAreaWidgetContents_4)
        self.P2wglb2.setObjectName(u"P2wglb2")
        sizePolicy1.setHeightForWidth(self.P2wglb2.sizePolicy().hasHeightForWidth())
        self.P2wglb2.setSizePolicy(sizePolicy1)
        self.P2wglb2.setMinimumSize(QSize(1150, 160))
        self.P2wglb2.setStyleSheet(u"")
        self.pwg4 = QWidget(self.P2wglb2)
        self.pwg4.setObjectName(u"pwg4")
        self.pwg4.setGeometry(QRect(10, 20, 120, 120))
        self.pwg4.setStyleSheet(u"border-radius:60px;\n"
"background-color: transparent;")
        self.pwg5 = QWidget(self.P2wglb2)
        self.pwg5.setObjectName(u"pwg5")
        self.pwg5.setGeometry(QRect(380, 20, 120, 120))
        self.pwg5.setStyleSheet(u"border-radius:60px;\n"
"background-color: transparent;")
        self.pwg6 = QWidget(self.P2wglb2)
        self.pwg6.setObjectName(u"pwg6")
        self.pwg6.setGeometry(QRect(750, 20, 120, 120))
        self.pwg6.setStyleSheet(u"border-radius:60px;\n"
"background-color: transparent;")
        self.lbname4 = QLabel(self.P2wglb2)
        self.lbname4.setObjectName(u"lbname4")
        self.lbname4.setGeometry(QRect(140, 20, 191, 21))
        self.lbname4.setFont(font6)
        self.lbname4.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.lbgia4 = QLabel(self.P2wglb2)
        self.lbgia4.setObjectName(u"lbgia4")
        self.lbgia4.setGeometry(QRect(140, 50, 191, 21))
        self.lbgia4.setFont(font6)
        self.lbgia4.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.lbgia5 = QLabel(self.P2wglb2)
        self.lbgia5.setObjectName(u"lbgia5")
        self.lbgia5.setGeometry(QRect(510, 50, 191, 21))
        self.lbgia5.setFont(font6)
        self.lbgia5.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.lbname5 = QLabel(self.P2wglb2)
        self.lbname5.setObjectName(u"lbname5")
        self.lbname5.setGeometry(QRect(510, 20, 191, 21))
        self.lbname5.setFont(font6)
        self.lbname5.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.lbgia6 = QLabel(self.P2wglb2)
        self.lbgia6.setObjectName(u"lbgia6")
        self.lbgia6.setGeometry(QRect(880, 50, 191, 21))
        self.lbgia6.setFont(font6)
        self.lbgia6.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.lbname6 = QLabel(self.P2wglb2)
        self.lbname6.setObjectName(u"lbname6")
        self.lbname6.setGeometry(QRect(880, 20, 191, 21))
        self.lbname6.setFont(font6)
        self.lbname6.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.spinBox4 = QSpinBox(self.P2wglb2)
        self.spinBox4.setObjectName(u"spinBox4")
        self.spinBox4.setGeometry(QRect(140, 100, 71, 31))
        self.spinBox4.setStyleSheet(u"QSpinBox {\n"
"    background: rgb(65, 66, 63);\n"
"    color: white;\n"
"    border: 2px solid #ccc;\n"
"    border-radius: 4px;\n"
"    padding: 5px 10px;\n"
"    font-size: 16px;\n"
"}\n"
"\n"
"QSpinBox::up-button, QSpinBox::down-button {\n"
"	background-color: rgb(107, 109, 104);\n"
"    border: none;\n"
"    width: 16px;\n"
"}\n"
"\n"
"QSpinBox::up-button:hover, QSpinBox::down-button:hover {\n"
"    background: rgba(255, 255, 255, 0.2);\n"
"}\n"
"\n"
"QSpinBox::up-arrow {\n"
"    image: url(:/icons/up-arrow.png);\n"
"}\n"
"\n"
"QSpinBox::down-arrow {\n"
"    image: url(:/icons/down-arrow.png);\n"
"}\n"
"")
        self.spinBox6 = QSpinBox(self.P2wglb2)
        self.spinBox6.setObjectName(u"spinBox6")
        self.spinBox6.setGeometry(QRect(880, 100, 71, 31))
        self.spinBox6.setStyleSheet(u"QSpinBox {\n"
"    background: rgb(65, 66, 63);\n"
"    color: white;\n"
"    border: 2px solid #ccc;\n"
"    border-radius: 4px;\n"
"    padding: 5px 10px;\n"
"    font-size: 16px;\n"
"}\n"
"\n"
"QSpinBox::up-button, QSpinBox::down-button {\n"
"	background-color: rgb(107, 109, 104);\n"
"    border: none;\n"
"    width: 16px;\n"
"}\n"
"\n"
"QSpinBox::up-button:hover, QSpinBox::down-button:hover {\n"
"    background: rgba(255, 255, 255, 0.2);\n"
"}\n"
"\n"
"QSpinBox::up-arrow {\n"
"    image: url(:/icons/up-arrow.png);\n"
"}\n"
"\n"
"QSpinBox::down-arrow {\n"
"    image: url(:/icons/down-arrow.png);\n"
"}\n"
"")
        self.spinBox5 = QSpinBox(self.P2wglb2)
        self.spinBox5.setObjectName(u"spinBox5")
        self.spinBox5.setGeometry(QRect(510, 100, 71, 31))
        self.spinBox5.setStyleSheet(u"QSpinBox {\n"
"    background: rgb(65, 66, 63);\n"
"    color: white;\n"
"    border: 2px solid #ccc;\n"
"    border-radius: 4px;\n"
"    padding: 5px 10px;\n"
"    font-size: 16px;\n"
"}\n"
"\n"
"QSpinBox::up-button, QSpinBox::down-button {\n"
"	background-color: rgb(107, 109, 104);\n"
"    border: none;\n"
"    width: 16px;\n"
"}\n"
"\n"
"QSpinBox::up-button:hover, QSpinBox::down-button:hover {\n"
"    background: rgba(255, 255, 255, 0.2);\n"
"}\n"
"\n"
"QSpinBox::up-arrow {\n"
"    image: url(:/icons/up-arrow.png);\n"
"}\n"
"\n"
"QSpinBox::down-arrow {\n"
"    image: url(:/icons/down-arrow.png);\n"
"}\n"
"")

        self.verticalLayout_63.addWidget(self.P2wglb2)

        self.P2wglb3 = QWidget(self.scrollAreaWidgetContents_4)
        self.P2wglb3.setObjectName(u"P2wglb3")
        sizePolicy1.setHeightForWidth(self.P2wglb3.sizePolicy().hasHeightForWidth())
        self.P2wglb3.setSizePolicy(sizePolicy1)
        self.P2wglb3.setMinimumSize(QSize(1150, 160))
        self.P2wglb3.setStyleSheet(u"")
        self.pwg7 = QWidget(self.P2wglb3)
        self.pwg7.setObjectName(u"pwg7")
        self.pwg7.setGeometry(QRect(10, 20, 120, 120))
        self.pwg7.setStyleSheet(u"border-radius:60px;\n"
"background-color: transparent;")
        self.pwg8 = QWidget(self.P2wglb3)
        self.pwg8.setObjectName(u"pwg8")
        self.pwg8.setGeometry(QRect(380, 20, 120, 120))
        self.pwg8.setStyleSheet(u"border-radius:60px;\n"
"background-color: transparent;")
        self.pwg9 = QWidget(self.P2wglb3)
        self.pwg9.setObjectName(u"pwg9")
        self.pwg9.setGeometry(QRect(750, 20, 120, 120))
        self.pwg9.setStyleSheet(u"border-radius:60px;\n"
"background-color: transparent;")
        self.lbgia7 = QLabel(self.P2wglb3)
        self.lbgia7.setObjectName(u"lbgia7")
        self.lbgia7.setGeometry(QRect(140, 50, 191, 21))
        self.lbgia7.setFont(font6)
        self.lbgia7.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.lbname7 = QLabel(self.P2wglb3)
        self.lbname7.setObjectName(u"lbname7")
        self.lbname7.setGeometry(QRect(140, 20, 191, 21))
        self.lbname7.setFont(font6)
        self.lbname7.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.lbgia8 = QLabel(self.P2wglb3)
        self.lbgia8.setObjectName(u"lbgia8")
        self.lbgia8.setGeometry(QRect(510, 50, 191, 21))
        self.lbgia8.setFont(font6)
        self.lbgia8.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.lbname8 = QLabel(self.P2wglb3)
        self.lbname8.setObjectName(u"lbname8")
        self.lbname8.setGeometry(QRect(510, 20, 191, 21))
        self.lbname8.setFont(font6)
        self.lbname8.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.lbgia9 = QLabel(self.P2wglb3)
        self.lbgia9.setObjectName(u"lbgia9")
        self.lbgia9.setGeometry(QRect(880, 50, 191, 21))
        self.lbgia9.setFont(font6)
        self.lbgia9.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.lbname9 = QLabel(self.P2wglb3)
        self.lbname9.setObjectName(u"lbname9")
        self.lbname9.setGeometry(QRect(880, 20, 191, 21))
        self.lbname9.setFont(font6)
        self.lbname9.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.spinBox7 = QSpinBox(self.P2wglb3)
        self.spinBox7.setObjectName(u"spinBox7")
        self.spinBox7.setGeometry(QRect(140, 100, 71, 31))
        self.spinBox7.setStyleSheet(u"QSpinBox {\n"
"    background: rgb(65, 66, 63);\n"
"    color: white;\n"
"    border: 2px solid #ccc;\n"
"    border-radius: 4px;\n"
"    padding: 5px 10px;\n"
"    font-size: 16px;\n"
"}\n"
"\n"
"QSpinBox::up-button, QSpinBox::down-button {\n"
"	background-color: rgb(107, 109, 104);\n"
"    border: none;\n"
"    width: 16px;\n"
"}\n"
"\n"
"QSpinBox::up-button:hover, QSpinBox::down-button:hover {\n"
"    background: rgba(255, 255, 255, 0.2);\n"
"}\n"
"\n"
"QSpinBox::up-arrow {\n"
"    image: url(:/icons/up-arrow.png);\n"
"}\n"
"\n"
"QSpinBox::down-arrow {\n"
"    image: url(:/icons/down-arrow.png);\n"
"}\n"
"")
        self.spinBox8 = QSpinBox(self.P2wglb3)
        self.spinBox8.setObjectName(u"spinBox8")
        self.spinBox8.setGeometry(QRect(510, 100, 71, 31))
        self.spinBox8.setStyleSheet(u"QSpinBox {\n"
"    background: rgb(65, 66, 63);\n"
"    color: white;\n"
"    border: 2px solid #ccc;\n"
"    border-radius: 4px;\n"
"    padding: 5px 10px;\n"
"    font-size: 16px;\n"
"}\n"
"\n"
"QSpinBox::up-button, QSpinBox::down-button {\n"
"	background-color: rgb(107, 109, 104);\n"
"    border: none;\n"
"    width: 16px;\n"
"}\n"
"\n"
"QSpinBox::up-button:hover, QSpinBox::down-button:hover {\n"
"    background: rgba(255, 255, 255, 0.2);\n"
"}\n"
"\n"
"QSpinBox::up-arrow {\n"
"    image: url(:/icons/up-arrow.png);\n"
"}\n"
"\n"
"QSpinBox::down-arrow {\n"
"    image: url(:/icons/down-arrow.png);\n"
"}\n"
"")
        self.spinBox9 = QSpinBox(self.P2wglb3)
        self.spinBox9.setObjectName(u"spinBox9")
        self.spinBox9.setGeometry(QRect(880, 100, 71, 31))
        self.spinBox9.setStyleSheet(u"QSpinBox {\n"
"    background: rgb(65, 66, 63);\n"
"    color: white;\n"
"    border: 2px solid #ccc;\n"
"    border-radius: 4px;\n"
"    padding: 5px 10px;\n"
"    font-size: 16px;\n"
"}\n"
"\n"
"QSpinBox::up-button, QSpinBox::down-button {\n"
"	background-color: rgb(107, 109, 104);\n"
"    border: none;\n"
"    width: 16px;\n"
"}\n"
"\n"
"QSpinBox::up-button:hover, QSpinBox::down-button:hover {\n"
"    background: rgba(255, 255, 255, 0.2);\n"
"}\n"
"\n"
"QSpinBox::up-arrow {\n"
"    image: url(:/icons/up-arrow.png);\n"
"}\n"
"\n"
"QSpinBox::down-arrow {\n"
"    image: url(:/icons/down-arrow.png);\n"
"}\n"
"")

        self.verticalLayout_63.addWidget(self.P2wglb3)

        self.P2wglb4 = QWidget(self.scrollAreaWidgetContents_4)
        self.P2wglb4.setObjectName(u"P2wglb4")
        sizePolicy1.setHeightForWidth(self.P2wglb4.sizePolicy().hasHeightForWidth())
        self.P2wglb4.setSizePolicy(sizePolicy1)
        self.P2wglb4.setMinimumSize(QSize(1150, 160))
        self.P2wglb4.setStyleSheet(u"")
        self.pwg10 = QWidget(self.P2wglb4)
        self.pwg10.setObjectName(u"pwg10")
        self.pwg10.setGeometry(QRect(10, 20, 120, 120))
        self.pwg10.setStyleSheet(u"border-radius:60px;\n"
"background-color: transparent;")
        self.pwg11 = QWidget(self.P2wglb4)
        self.pwg11.setObjectName(u"pwg11")
        self.pwg11.setGeometry(QRect(380, 20, 120, 120))
        self.pwg11.setStyleSheet(u"border-radius:60px;\n"
"background-color: transparent;")
        self.pwg12 = QWidget(self.P2wglb4)
        self.pwg12.setObjectName(u"pwg12")
        self.pwg12.setGeometry(QRect(750, 20, 120, 120))
        self.pwg12.setStyleSheet(u"border-radius:60px;\n"
"background-color: transparent;")
        self.lbname10 = QLabel(self.P2wglb4)
        self.lbname10.setObjectName(u"lbname10")
        self.lbname10.setGeometry(QRect(140, 20, 191, 21))
        self.lbname10.setFont(font6)
        self.lbname10.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.lbgia10 = QLabel(self.P2wglb4)
        self.lbgia10.setObjectName(u"lbgia10")
        self.lbgia10.setGeometry(QRect(140, 50, 191, 21))
        self.lbgia10.setFont(font6)
        self.lbgia10.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.lbgia12 = QLabel(self.P2wglb4)
        self.lbgia12.setObjectName(u"lbgia12")
        self.lbgia12.setGeometry(QRect(880, 50, 191, 21))
        self.lbgia12.setFont(font6)
        self.lbgia12.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.lbname12 = QLabel(self.P2wglb4)
        self.lbname12.setObjectName(u"lbname12")
        self.lbname12.setGeometry(QRect(880, 20, 191, 21))
        self.lbname12.setFont(font6)
        self.lbname12.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.lbgia11 = QLabel(self.P2wglb4)
        self.lbgia11.setObjectName(u"lbgia11")
        self.lbgia11.setGeometry(QRect(510, 50, 191, 21))
        self.lbgia11.setFont(font6)
        self.lbgia11.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.lbname11 = QLabel(self.P2wglb4)
        self.lbname11.setObjectName(u"lbname11")
        self.lbname11.setGeometry(QRect(510, 20, 191, 21))
        self.lbname11.setFont(font6)
        self.lbname11.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.spinBox10 = QSpinBox(self.P2wglb4)
        self.spinBox10.setObjectName(u"spinBox10")
        self.spinBox10.setGeometry(QRect(140, 100, 71, 31))
        self.spinBox10.setStyleSheet(u"QSpinBox {\n"
"    background: rgb(65, 66, 63);\n"
"    color: white;\n"
"    border: 2px solid #ccc;\n"
"    border-radius: 4px;\n"
"    padding: 5px 10px;\n"
"    font-size: 16px;\n"
"}\n"
"\n"
"QSpinBox::up-button, QSpinBox::down-button {\n"
"	background-color: rgb(107, 109, 104);\n"
"    border: none;\n"
"    width: 16px;\n"
"}\n"
"\n"
"QSpinBox::up-button:hover, QSpinBox::down-button:hover {\n"
"    background: rgba(255, 255, 255, 0.2);\n"
"}\n"
"\n"
"QSpinBox::up-arrow {\n"
"    image: url(:/icons/up-arrow.png);\n"
"}\n"
"\n"
"QSpinBox::down-arrow {\n"
"    image: url(:/icons/down-arrow.png);\n"
"}\n"
"")
        self.spinBox12 = QSpinBox(self.P2wglb4)
        self.spinBox12.setObjectName(u"spinBox12")
        self.spinBox12.setGeometry(QRect(880, 100, 71, 31))
        self.spinBox12.setStyleSheet(u"QSpinBox {\n"
"    background: rgb(65, 66, 63);\n"
"    color: white;\n"
"    border: 2px solid #ccc;\n"
"    border-radius: 4px;\n"
"    padding: 5px 10px;\n"
"    font-size: 16px;\n"
"}\n"
"\n"
"QSpinBox::up-button, QSpinBox::down-button {\n"
"	background-color: rgb(107, 109, 104);\n"
"    border: none;\n"
"    width: 16px;\n"
"}\n"
"\n"
"QSpinBox::up-button:hover, QSpinBox::down-button:hover {\n"
"    background: rgba(255, 255, 255, 0.2);\n"
"}\n"
"\n"
"QSpinBox::up-arrow {\n"
"    image: url(:/icons/up-arrow.png);\n"
"}\n"
"\n"
"QSpinBox::down-arrow {\n"
"    image: url(:/icons/down-arrow.png);\n"
"}\n"
"")
        self.spinBox11 = QSpinBox(self.P2wglb4)
        self.spinBox11.setObjectName(u"spinBox11")
        self.spinBox11.setGeometry(QRect(510, 100, 71, 31))
        self.spinBox11.setStyleSheet(u"QSpinBox {\n"
"    background: rgb(65, 66, 63);\n"
"    color: white;\n"
"    border: 2px solid #ccc;\n"
"    border-radius: 4px;\n"
"    padding: 5px 10px;\n"
"    font-size: 16px;\n"
"}\n"
"\n"
"QSpinBox::up-button, QSpinBox::down-button {\n"
"	background-color: rgb(107, 109, 104);\n"
"    border: none;\n"
"    width: 16px;\n"
"}\n"
"\n"
"QSpinBox::up-button:hover, QSpinBox::down-button:hover {\n"
"    background: rgba(255, 255, 255, 0.2);\n"
"}\n"
"\n"
"QSpinBox::up-arrow {\n"
"    image: url(:/icons/up-arrow.png);\n"
"}\n"
"\n"
"QSpinBox::down-arrow {\n"
"    image: url(:/icons/down-arrow.png);\n"
"}\n"
"")

        self.verticalLayout_63.addWidget(self.P2wglb4)

        self.P2wglb5 = QWidget(self.scrollAreaWidgetContents_4)
        self.P2wglb5.setObjectName(u"P2wglb5")
        sizePolicy1.setHeightForWidth(self.P2wglb5.sizePolicy().hasHeightForWidth())
        self.P2wglb5.setSizePolicy(sizePolicy1)
        self.P2wglb5.setMinimumSize(QSize(1150, 160))
        self.P2wglb5.setStyleSheet(u"")
        self.pwg13 = QWidget(self.P2wglb5)
        self.pwg13.setObjectName(u"pwg13")
        self.pwg13.setGeometry(QRect(10, 20, 120, 120))
        self.pwg13.setStyleSheet(u"border-radius:60px;\n"
"background-color: transparent;")
        self.pwg14 = QWidget(self.P2wglb5)
        self.pwg14.setObjectName(u"pwg14")
        self.pwg14.setGeometry(QRect(380, 20, 120, 120))
        self.pwg14.setStyleSheet(u"border-radius:60px;\n"
"background-color: transparent;")
        self.pwg15 = QWidget(self.P2wglb5)
        self.pwg15.setObjectName(u"pwg15")
        self.pwg15.setGeometry(QRect(750, 20, 120, 120))
        self.pwg15.setStyleSheet(u"border-radius:60px;\n"
"background-color: transparent;")
        self.lbname13 = QLabel(self.P2wglb5)
        self.lbname13.setObjectName(u"lbname13")
        self.lbname13.setGeometry(QRect(140, 20, 191, 21))
        self.lbname13.setFont(font6)
        self.lbname13.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.lbgia13 = QLabel(self.P2wglb5)
        self.lbgia13.setObjectName(u"lbgia13")
        self.lbgia13.setGeometry(QRect(140, 50, 191, 21))
        self.lbgia13.setFont(font6)
        self.lbgia13.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.lbname14 = QLabel(self.P2wglb5)
        self.lbname14.setObjectName(u"lbname14")
        self.lbname14.setGeometry(QRect(510, 20, 191, 21))
        self.lbname14.setFont(font6)
        self.lbname14.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.lbgia14 = QLabel(self.P2wglb5)
        self.lbgia14.setObjectName(u"lbgia14")
        self.lbgia14.setGeometry(QRect(510, 50, 191, 21))
        self.lbgia14.setFont(font6)
        self.lbgia14.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.lbgia15 = QLabel(self.P2wglb5)
        self.lbgia15.setObjectName(u"lbgia15")
        self.lbgia15.setGeometry(QRect(880, 50, 191, 21))
        self.lbgia15.setFont(font6)
        self.lbgia15.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.lbname15 = QLabel(self.P2wglb5)
        self.lbname15.setObjectName(u"lbname15")
        self.lbname15.setGeometry(QRect(880, 20, 191, 21))
        self.lbname15.setFont(font6)
        self.lbname15.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.spinBox13 = QSpinBox(self.P2wglb5)
        self.spinBox13.setObjectName(u"spinBox13")
        self.spinBox13.setGeometry(QRect(140, 120, 71, 31))
        self.spinBox13.setStyleSheet(u"QSpinBox {\n"
"    background: rgb(65, 66, 63);\n"
"    color: white;\n"
"    border: 2px solid #ccc;\n"
"    border-radius: 4px;\n"
"    padding: 5px 10px;\n"
"    font-size: 16px;\n"
"}\n"
"\n"
"QSpinBox::up-button, QSpinBox::down-button {\n"
"	background-color: rgb(107, 109, 104);\n"
"    border: none;\n"
"    width: 16px;\n"
"}\n"
"\n"
"QSpinBox::up-button:hover, QSpinBox::down-button:hover {\n"
"    background: rgba(255, 255, 255, 0.2);\n"
"}\n"
"\n"
"QSpinBox::up-arrow {\n"
"    image: url(:/icons/up-arrow.png);\n"
"}\n"
"\n"
"QSpinBox::down-arrow {\n"
"    image: url(:/icons/down-arrow.png);\n"
"}\n"
"")
        self.spinBox14 = QSpinBox(self.P2wglb5)
        self.spinBox14.setObjectName(u"spinBox14")
        self.spinBox14.setGeometry(QRect(510, 120, 71, 31))
        self.spinBox14.setStyleSheet(u"QSpinBox {\n"
"    background: rgb(65, 66, 63);\n"
"    color: white;\n"
"    border: 2px solid #ccc;\n"
"    border-radius: 4px;\n"
"    padding: 5px 10px;\n"
"    font-size: 16px;\n"
"}\n"
"\n"
"QSpinBox::up-button, QSpinBox::down-button {\n"
"	background-color: rgb(107, 109, 104);\n"
"    border: none;\n"
"    width: 16px;\n"
"}\n"
"\n"
"QSpinBox::up-button:hover, QSpinBox::down-button:hover {\n"
"    background: rgba(255, 255, 255, 0.2);\n"
"}\n"
"\n"
"QSpinBox::up-arrow {\n"
"    image: url(:/icons/up-arrow.png);\n"
"}\n"
"\n"
"QSpinBox::down-arrow {\n"
"    image: url(:/icons/down-arrow.png);\n"
"}\n"
"")
        self.spinBox15 = QSpinBox(self.P2wglb5)
        self.spinBox15.setObjectName(u"spinBox15")
        self.spinBox15.setGeometry(QRect(880, 120, 71, 31))
        self.spinBox15.setStyleSheet(u"QSpinBox {\n"
"    background: rgb(65, 66, 63);\n"
"    color: white;\n"
"    border: 2px solid #ccc;\n"
"    border-radius: 4px;\n"
"    padding: 5px 10px;\n"
"    font-size: 16px;\n"
"}\n"
"\n"
"QSpinBox::up-button, QSpinBox::down-button {\n"
"	background-color: rgb(107, 109, 104);\n"
"    border: none;\n"
"    width: 16px;\n"
"}\n"
"\n"
"QSpinBox::up-button:hover, QSpinBox::down-button:hover {\n"
"    background: rgba(255, 255, 255, 0.2);\n"
"}\n"
"\n"
"QSpinBox::up-arrow {\n"
"    image: url(:/icons/up-arrow.png);\n"
"}\n"
"\n"
"QSpinBox::down-arrow {\n"
"    image: url(:/icons/down-arrow.png);\n"
"}\n"
"")

        self.verticalLayout_63.addWidget(self.P2wglb5)

        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_4)

        self.verticalLayout_28.addWidget(self.WgPWG, 0, Qt.AlignmentFlag.AlignHCenter)


        self.verticalLayout_2.addWidget(self.widget_64, 0, Qt.AlignmentFlag.AlignHCenter)

        self.wgThanhToan = QWidget(self.pageOrder)
        self.wgThanhToan.setObjectName(u"wgThanhToan")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.wgThanhToan.sizePolicy().hasHeightForWidth())
        self.wgThanhToan.setSizePolicy(sizePolicy4)
        self.wgThanhToan.setMinimumSize(QSize(1100, 70))
        self.wgThanhToan.setMaximumSize(QSize(1100, 70))
        self.wgThanhToan.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.wgThanhToan.setStyleSheet(u"background-color: rgb(65, 66, 63);\n"
"border-radius: 8px;")
        self.btnXGH = QPushButton(self.wgThanhToan)
        self.btnXGH.setObjectName(u"btnXGH")
        self.btnXGH.setGeometry(QRect(920, 10, 151, 51))
        sizePolicy3.setHeightForWidth(self.btnXGH.sizePolicy().hasHeightForWidth())
        self.btnXGH.setSizePolicy(sizePolicy3)
        self.btnXGH.setFont(font3)
        self.btnXGH.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btnXGH.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(65, 66, 63);\n"
"border-radius: 8px;\n"
"border: 1px solid rgb(255,255,255);\n"
"	\n"
"	color: rgb(255, 255, 255);\n"
"\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(239, 50, 104); \n"
"    color: white;\n"
"}\n"
"QPushButton:checked{\n"
" background-color: rgb(239, 50, 104);\n"
" color: white;\n"
"}")
        self.btnMua = QPushButton(self.wgThanhToan)
        self.btnMua.setObjectName(u"btnMua")
        self.btnMua.setGeometry(QRect(750, 10, 151, 51))
        sizePolicy3.setHeightForWidth(self.btnMua.sizePolicy().hasHeightForWidth())
        self.btnMua.setSizePolicy(sizePolicy3)
        self.btnMua.setFont(font3)
        self.btnMua.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btnMua.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(255, 255, 255);\n"
"border-radius: 8px;\n"
"border: none;\n"
"	color: rgb(65, 66, 63);\n"
"\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(239, 50, 104); \n"
"    color: white;\n"
"}\n"
"QPushButton:checked{\n"
" background-color: rgb(239, 50, 104);\n"
" color: white;\n"
"}")
        self.label_4 = QLabel(self.wgThanhToan)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(50, 20, 131, 31))
        self.label_4.setFont(font3)
        self.label_4.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"")
        self.lbThanhtien_3 = QLabel(self.wgThanhToan)
        self.lbThanhtien_3.setObjectName(u"lbThanhtien_3")
        self.lbThanhtien_3.setGeometry(QRect(200, 20, 171, 31))
        self.lbThanhtien_3.setFont(font3)
        self.lbThanhtien_3.setStyleSheet(u"color: rgb(255, 38, 107);")

        self.verticalLayout_2.addWidget(self.wgThanhToan, 0, Qt.AlignmentFlag.AlignHCenter)

        self.stackedWidget.addWidget(self.pageOrder)
        self.pageAI = QWidget()
        self.pageAI.setObjectName(u"pageAI")
        self.verticalLayout_57 = QVBoxLayout(self.pageAI)
        self.verticalLayout_57.setObjectName(u"verticalLayout_57")
        self.widget_96 = QWidget(self.pageAI)
        self.widget_96.setObjectName(u"widget_96")
        self.widget_96.setMinimumSize(QSize(900, 70))
        self.widget_96.setMaximumSize(QSize(16777215, 70))
        self.widget_96.setStyleSheet(u"")
        self.lblCoffee_17 = QLabel(self.widget_96)
        self.lblCoffee_17.setObjectName(u"lblCoffee_17")
        self.lblCoffee_17.setGeometry(QRect(80, -10, 551, 61))
        self.lblCoffee_17.setFont(font5)
        self.lblCoffee_17.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"border: none;\n"
"font: 500 36pt \"8-bit Arcade In\";")
        self.lblCoffee_17.setTextFormat(Qt.TextFormat.PlainText)
        self.lblCoffee_17.setScaledContents(False)
        self.lblCoffee_17.setWordWrap(False)
        self.lblCoffee_17.setOpenExternalLinks(False)
        self.lblCoffee_18 = QLabel(self.widget_96)
        self.lblCoffee_18.setObjectName(u"lblCoffee_18")
        self.lblCoffee_18.setGeometry(QRect(80, 50, 261, 16))
        self.lblCoffee_18.setFont(font2)
        self.lblCoffee_18.setStyleSheet(u"border: none;\n"
"color: white")
        self.lblCoffee_18.setTextFormat(Qt.TextFormat.PlainText)
        self.lblCoffee_18.setScaledContents(False)
        self.lblCoffee_18.setWordWrap(False)
        self.lblCoffee_18.setOpenExternalLinks(False)

        self.verticalLayout_57.addWidget(self.widget_96, 0, Qt.AlignmentFlag.AlignTop)

        self.widget_106 = QWidget(self.pageAI)
        self.widget_106.setObjectName(u"widget_106")
        self.widget_106.setStyleSheet(u"border-bottom: 1px solid rgb(65, 66, 63)")

        self.verticalLayout_57.addWidget(self.widget_106)

        self.widget_97 = QWidget(self.pageAI)
        self.widget_97.setObjectName(u"widget_97")
        self.verticalLayout_61 = QVBoxLayout(self.widget_97)
        self.verticalLayout_61.setObjectName(u"verticalLayout_61")
        self.WgPWG_2 = QWidget(self.widget_97)
        self.WgPWG_2.setObjectName(u"WgPWG_2")
        self.WgPWG_2.setMinimumSize(QSize(1000, 600))
        self.WgPWG_2.setMaximumSize(QSize(16777215, 16777215))
        self.WgPWG_2.setStyleSheet(u"")
        self.verticalLayout_65 = QVBoxLayout(self.WgPWG_2)
        self.verticalLayout_65.setSpacing(0)
        self.verticalLayout_65.setObjectName(u"verticalLayout_65")
        self.verticalLayout_65.setContentsMargins(-1, 0, 0, 0)
        self.textBrowser = QTextBrowser(self.WgPWG_2)
        self.textBrowser.setObjectName(u"textBrowser")
        font7 = QFont()
        font7.setFamilies([u"Tahoma"])
        font7.setPointSize(12)
        font7.setBold(False)
        self.textBrowser.setFont(font7)
        self.textBrowser.setStyleSheet(u"\n"
"background-color: rgb(0, 0, 0);\n"
"color: rgb(197, 197, 197);\n"
"padding:10px;\n"
"border-radius: 30px;")
        self.textBrowser.setLocale(QLocale(QLocale.Vietnamese, QLocale.Vietnam))

        self.verticalLayout_65.addWidget(self.textBrowser)

        self.widget_112 = QWidget(self.WgPWG_2)
        self.widget_112.setObjectName(u"widget_112")
        self.widget_112.setMinimumSize(QSize(0, 150))
        self.lineEdit = QLineEdit(self.widget_112)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(250, 10, 700, 130))
        sizePolicy.setHeightForWidth(self.lineEdit.sizePolicy().hasHeightForWidth())
        self.lineEdit.setSizePolicy(sizePolicy)
        self.lineEdit.setMinimumSize(QSize(700, 130))
        self.lineEdit.setMaximumSize(QSize(16777215, 16777215))
        font8 = QFont()
        font8.setPointSize(12)
        self.lineEdit.setFont(font8)
        self.lineEdit.setStyleSheet(u"QLineEdit {\n"
"    background-color: #2E2E2E;\n"
"    color: white; \n"
"\n"
"    border-radius: 30px;\n"
"    padding: 20px; \n"
"    selection-background-color: #555555;\n"
"    selection-color: white;\n"
"	\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border: 2px solid rgb(104, 34, 255)\n"
"    background-color: #3E3E3E;\n"
"}\n"
"")
        self.lineEdit.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)
        self.pushButton1 = QPushButton(self.widget_112)
        self.pushButton1.setObjectName(u"pushButton1")
        self.pushButton1.setGeometry(QRect(890, 90, 40, 40))
        self.pushButton1.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.pushButton1.setStyleSheet(u"color: rgb(255, 161, 238);\n"
"border-radius:20px")
        icon4 = QIcon()
        icon4.addFile(u":/src/ass/icon/top.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton1.setIcon(icon4)
        self.pushButton1.setIconSize(QSize(18, 18))

        self.verticalLayout_65.addWidget(self.widget_112)


        self.verticalLayout_61.addWidget(self.WgPWG_2)


        self.verticalLayout_57.addWidget(self.widget_97)

        self.stackedWidget.addWidget(self.pageAI)
        self.pageInfo = QWidget()
        self.pageInfo.setObjectName(u"pageInfo")
        self.verticalLayout_53 = QVBoxLayout(self.pageInfo)
        self.verticalLayout_53.setObjectName(u"verticalLayout_53")
        self.widget_93 = QWidget(self.pageInfo)
        self.widget_93.setObjectName(u"widget_93")
        self.widget_93.setMinimumSize(QSize(900, 70))
        self.widget_93.setMaximumSize(QSize(16777215, 70))
        self.widget_93.setStyleSheet(u"border-bottom: 2px solid \n"
" rgb(65, 66, 63);")
        self.lblCoffee_15 = QLabel(self.widget_93)
        self.lblCoffee_15.setObjectName(u"lblCoffee_15")
        self.lblCoffee_15.setGeometry(QRect(100, -10, 331, 41))
        font9 = QFont()
        font9.setFamilies([u"8-bit Arcade Out"])
        font9.setPointSize(40)
        font9.setWeight(QFont.Medium)
        font9.setItalic(False)
        font9.setUnderline(False)
        font9.setStrikeOut(False)
        font9.setKerning(True)
        font9.setStyleStrategy(QFont.PreferAntialias)
        font9.setHintingPreference(QFont.PreferDefaultHinting)
        self.lblCoffee_15.setFont(font9)
        self.lblCoffee_15.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"border: none;\n"
"font: 500 40pt \"8-bit Arcade Out\";")
        self.lblCoffee_15.setTextFormat(Qt.TextFormat.PlainText)
        self.lblCoffee_15.setScaledContents(False)
        self.lblCoffee_15.setWordWrap(False)
        self.lblCoffee_15.setOpenExternalLinks(False)
        self.lblCoffee_16 = QLabel(self.widget_93)
        self.lblCoffee_16.setObjectName(u"lblCoffee_16")
        self.lblCoffee_16.setGeometry(QRect(100, 40, 261, 16))
        self.lblCoffee_16.setFont(font2)
        self.lblCoffee_16.setStyleSheet(u"border: none;\n"
"color: rgb(65, 66, 63);")
        self.lblCoffee_16.setTextFormat(Qt.TextFormat.PlainText)
        self.lblCoffee_16.setScaledContents(False)
        self.lblCoffee_16.setWordWrap(False)
        self.lblCoffee_16.setOpenExternalLinks(False)

        self.verticalLayout_53.addWidget(self.widget_93, 0, Qt.AlignmentFlag.AlignTop)

        self.widget_3 = QWidget(self.pageInfo)
        self.widget_3.setObjectName(u"widget_3")
        self.widget_3.setMinimumSize(QSize(1100, 0))
        self.verticalLayout_54 = QVBoxLayout(self.widget_3)
        self.verticalLayout_54.setObjectName(u"verticalLayout_54")
        self.scrollArea = QScrollArea(self.widget_3)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents_3 = QWidget()
        self.scrollAreaWidgetContents_3.setObjectName(u"scrollAreaWidgetContents_3")
        self.scrollAreaWidgetContents_3.setGeometry(QRect(0, 0, 1070, 584))
        self.verticalLayout_55 = QVBoxLayout(self.scrollAreaWidgetContents_3)
        self.verticalLayout_55.setObjectName(u"verticalLayout_55")
        self.widget_94 = QWidget(self.scrollAreaWidgetContents_3)
        self.widget_94.setObjectName(u"widget_94")
        self.widget_94.setMinimumSize(QSize(0, 550))
        self.widget_94.setMaximumSize(QSize(16777215, 900))
        self.widget_94.setStyleSheet(u"")
        self.verticalLayout_56 = QVBoxLayout(self.widget_94)
        self.verticalLayout_56.setObjectName(u"verticalLayout_56")

        self.verticalLayout_55.addWidget(self.widget_94)

        self.widget_95 = QWidget(self.scrollAreaWidgetContents_3)
        self.widget_95.setObjectName(u"widget_95")

        self.verticalLayout_55.addWidget(self.widget_95)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents_3)

        self.verticalLayout_54.addWidget(self.scrollArea)


        self.verticalLayout_53.addWidget(self.widget_3, 0, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignVCenter)

        self.stackedWidget.addWidget(self.pageInfo)
        self.pageAdmin = QWidget()
        self.pageAdmin.setObjectName(u"pageAdmin")
        self.verticalLayout_58 = QVBoxLayout(self.pageAdmin)
        self.verticalLayout_58.setObjectName(u"verticalLayout_58")
        self.widget_98 = QWidget(self.pageAdmin)
        self.widget_98.setObjectName(u"widget_98")
        self.widget_98.setMinimumSize(QSize(900, 70))
        self.widget_98.setMaximumSize(QSize(1500, 70))
        self.widget_98.setStyleSheet(u"")
        self.lblCoffee_6 = QLabel(self.widget_98)
        self.lblCoffee_6.setObjectName(u"lblCoffee_6")
        self.lblCoffee_6.setGeometry(QRect(70, -10, 231, 31))
        self.lblCoffee_6.setFont(font5)
        self.lblCoffee_6.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"border: none;\n"
"font: 500 36pt \"8-bit Arcade In\";")
        self.lblCoffee_6.setTextFormat(Qt.TextFormat.PlainText)
        self.lblCoffee_6.setScaledContents(False)
        self.lblCoffee_6.setWordWrap(False)
        self.lblCoffee_6.setOpenExternalLinks(False)
        self.lblCoffee_7 = QLabel(self.widget_98)
        self.lblCoffee_7.setObjectName(u"lblCoffee_7")
        self.lblCoffee_7.setGeometry(QRect(70, 30, 261, 31))
        self.lblCoffee_7.setFont(font2)
        self.lblCoffee_7.setStyleSheet(u"border: none;\n"
"color: white")
        self.lblCoffee_7.setTextFormat(Qt.TextFormat.PlainText)
        self.lblCoffee_7.setScaledContents(False)
        self.lblCoffee_7.setWordWrap(False)
        self.lblCoffee_7.setOpenExternalLinks(False)

        self.verticalLayout_58.addWidget(self.widget_98, 0, Qt.AlignmentFlag.AlignTop)

        self.widget_101 = QWidget(self.pageAdmin)
        self.widget_101.setObjectName(u"widget_101")
        self.widget_101.setMinimumSize(QSize(0, 550))
        self.widget_101.setMaximumSize(QSize(16777215, 900))
        self.widget_101.setStyleSheet(u"")
        self.verticalLayout_59 = QVBoxLayout(self.widget_101)
        self.verticalLayout_59.setObjectName(u"verticalLayout_59")
        self.widget_99 = QWidget(self.widget_101)
        self.widget_99.setObjectName(u"widget_99")
        self.widget_99.setMinimumSize(QSize(0, 60))
        self.widget_99.setMaximumSize(QSize(16777215, 150))
        self.horizontalLayout_17 = QHBoxLayout(self.widget_99)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.widget_104 = QWidget(self.widget_99)
        self.widget_104.setObjectName(u"widget_104")
        sizePolicy1.setHeightForWidth(self.widget_104.sizePolicy().hasHeightForWidth())
        self.widget_104.setSizePolicy(sizePolicy1)
        self.widget_104.setMinimumSize(QSize(300, 70))
        self.widget_104.setStyleSheet(u"")
        self.comboBoxDB = QComboBox(self.widget_104)
        self.comboBoxDB.setObjectName(u"comboBoxDB")
        self.comboBoxDB.setGeometry(QRect(10, 10, 281, 24))
        self.comboBoxDB.setStyleSheet(u"QComboBox {\n"
"    background-color: rgb(65, 66, 63);\n"
"    color: white;\n"
"    border: 2px solid #ccc;\n"
"    border-radius: 6px;\n"
"    padding: 4px;\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"    background: #ccc;\n"
"    border: none;\n"
"    width: 20px;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView {\n"
"    background: rgb(65, 66, 63);\n"
"    color: white;\n"
"    border: 1px solid #ccc;\n"
"}\n"
"")

        self.horizontalLayout_17.addWidget(self.widget_104)

        self.widget_103 = QWidget(self.widget_99)
        self.widget_103.setObjectName(u"widget_103")
        self.widget_103.setStyleSheet(u"")

        self.horizontalLayout_17.addWidget(self.widget_103)


        self.verticalLayout_59.addWidget(self.widget_99)

        self.widget_100 = QWidget(self.widget_101)
        self.widget_100.setObjectName(u"widget_100")
        self.horizontalLayout_16 = QHBoxLayout(self.widget_100)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.tblDB = QTableView(self.widget_100)
        self.tblDB.setObjectName(u"tblDB")
        sizePolicy1.setHeightForWidth(self.tblDB.sizePolicy().hasHeightForWidth())
        self.tblDB.setSizePolicy(sizePolicy1)
        self.tblDB.setMinimumSize(QSize(900, 600))
        self.tblDB.setMaximumSize(QSize(800, 16777215))
        self.tblDB.setStyleSheet(u"QTableView {\n"
"    background-color: rgb(50, 50, 50);  \n"
"    color: white;\n"
"    border: px solid #aaa;  \n"
"    font-size: 14px;\n"
"    gridline-color: #666;  \n"
"    selection-background-color: white; \n"
"    selection-color: black;\n"
"\n"
"}\n"
"\n"
"QHeaderView::section {\n"
"    background-color: rgb(65, 66, 63);  \n"
"    color:black ;\n"
"\n"
"    border: 1px solid #555;\n"
"    font-weight: bold;\n"
"    text-transform: uppercase; \n"
"}\n"
"QTableView::item {\n"
" background-color: rgb(50, 50, 50);\n"
"    color: white;\n"
"}\n"
"QTableView::item:selected {\n"
"    background-color: rgb(65, 66, 63);  \n"
"    color: black;\n"
"    border-radius: 2px;\n"
"}\n"
"\n"
"QTableView::item:hover {\n"
"    background-color: #666;\n"
"    color: black;\n"
"}\n"
"QTableView QLineEdit {\n"
"    background-color: rgb(80, 80, 80);\n"
"    color: white;\n"
"}")
        self.tblDB.setFrameShadow(QFrame.Shadow.Plain)
        self.tblDB.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.tblDB.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.tblDB.setDragEnabled(False)
        self.tblDB.setVerticalScrollMode(QAbstractItemView.ScrollMode.ScrollPerPixel)
        self.tblDB.setHorizontalScrollMode(QAbstractItemView.ScrollMode.ScrollPerPixel)

        self.horizontalLayout_16.addWidget(self.tblDB)

        self.widget_102 = QWidget(self.widget_100)
        self.widget_102.setObjectName(u"widget_102")
        self.btnXoaDB = QPushButton(self.widget_102)
        self.btnXoaDB.setObjectName(u"btnXoaDB")
        self.btnXoaDB.setGeometry(QRect(40, 100, 151, 51))
        sizePolicy3.setHeightForWidth(self.btnXoaDB.sizePolicy().hasHeightForWidth())
        self.btnXoaDB.setSizePolicy(sizePolicy3)
        self.btnXoaDB.setFont(font3)
        self.btnXoaDB.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btnXoaDB.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(255, 255, 255);\n"
"border-radius: 8px;\n"
"	color: rgb(65, 66, 63);\n"
"t\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(239, 50, 104); \n"
"    color: white;\n"
"}\n"
"QPushButton:checked{\n"
" background-color: rgb(239, 50, 104);\n"
" color: white;\n"
"}")
        self.btnAddDB = QPushButton(self.widget_102)
        self.btnAddDB.setObjectName(u"btnAddDB")
        self.btnAddDB.setGeometry(QRect(40, 30, 151, 51))
        sizePolicy3.setHeightForWidth(self.btnAddDB.sizePolicy().hasHeightForWidth())
        self.btnAddDB.setSizePolicy(sizePolicy3)
        self.btnAddDB.setFont(font3)
        self.btnAddDB.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btnAddDB.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(255, 255, 255);\n"
"border-radius: 8px;\n"
"	color: rgb(65, 66, 63);\n"
"t\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(239, 50, 104); \n"
"    color: white;\n"
"}\n"
"QPushButton:checked{\n"
" background-color: rgb(239, 50, 104);\n"
" color: white;\n"
"}")
        self.btnUpdateDB = QPushButton(self.widget_102)
        self.btnUpdateDB.setObjectName(u"btnUpdateDB")
        self.btnUpdateDB.setGeometry(QRect(40, 170, 151, 51))
        sizePolicy3.setHeightForWidth(self.btnUpdateDB.sizePolicy().hasHeightForWidth())
        self.btnUpdateDB.setSizePolicy(sizePolicy3)
        self.btnUpdateDB.setFont(font3)
        self.btnUpdateDB.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btnUpdateDB.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(255, 255, 255);\n"
"border-radius: 8px;\n"
"	color: rgb(65, 66, 63);\n"
"t\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(239, 50, 104); \n"
"    color: white;\n"
"}\n"
"QPushButton:checked{\n"
" background-color: rgb(239, 50, 104);\n"
" color: white;\n"
"}")
        self.btnXem = QPushButton(self.widget_102)
        self.btnXem.setObjectName(u"btnXem")
        self.btnXem.setGeometry(QRect(40, 500, 151, 51))
        sizePolicy3.setHeightForWidth(self.btnXem.sizePolicy().hasHeightForWidth())
        self.btnXem.setSizePolicy(sizePolicy3)
        self.btnXem.setFont(font3)
        self.btnXem.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btnXem.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(255, 255, 255);\n"
"border-radius: 8px;\n"
"	color: rgb(65, 66, 63);\n"
"t\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(239, 50, 104); \n"
"    color: white;\n"
"}\n"
"QPushButton:checked{\n"
" background-color: rgb(239, 50, 104);\n"
" color: white;\n"
"}")

        self.horizontalLayout_16.addWidget(self.widget_102)


        self.verticalLayout_59.addWidget(self.widget_100)

        self.widget_105 = QWidget(self.widget_101)
        self.widget_105.setObjectName(u"widget_105")
        sizePolicy.setHeightForWidth(self.widget_105.sizePolicy().hasHeightForWidth())
        self.widget_105.setSizePolicy(sizePolicy)
        self.widget_105.setStyleSheet(u"")

        self.verticalLayout_59.addWidget(self.widget_105)


        self.verticalLayout_58.addWidget(self.widget_101)

        self.stackedWidget.addWidget(self.pageAdmin)

        self.horizontalLayout_18.addWidget(self.stackedWidget)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"CoffeeMTU", None))
        self.btnMenu.setText(QCoreApplication.translate("MainWindow", u"  Home", None))
        self.btnOrder.setText(QCoreApplication.translate("MainWindow", u"  Order", None))
        self.btnAI.setText(QCoreApplication.translate("MainWindow", u"    AI", None))
        self.btnAdmin.setText(QCoreApplication.translate("MainWindow", u"    Admin", None))
        self.label_2.setText("")
        self.label_5.setText("")
        self.label_6.setText("")
        self.label_7.setText("")
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Pinterest", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"VS Code", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Pinterest", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Github", None))
        self.lblWelcome.setText(QCoreApplication.translate("MainWindow", u"MENU", None))
        self.lbWelCome.setText(QCoreApplication.translate("MainWindow", u"MIEN TAY CONSTRUCTION UNIVERSITY", None))
        self.btnAdd1.setText(QCoreApplication.translate("MainWindow", u"Add To Cart", None))
        self.lblCost1.setText("")
        self.btnAdd2.setText(QCoreApplication.translate("MainWindow", u"Add To Cart", None))
        self.btnAdd3.setText(QCoreApplication.translate("MainWindow", u"Add To Cart", None))
        self.lblCost3.setText("")
        self.btnAdd4.setText(QCoreApplication.translate("MainWindow", u"Add To Cart", None))
        self.btnAdd5.setText(QCoreApplication.translate("MainWindow", u"Add To Cart", None))
        self.lblCost5.setText("")
        self.btnAdd6.setText(QCoreApplication.translate("MainWindow", u"Add To Cart", None))
        self.btnAdd8.setText(QCoreApplication.translate("MainWindow", u"Add To Cart", None))
        self.btnAdd7.setText(QCoreApplication.translate("MainWindow", u"Add To Cart", None))
        self.btnAdd9.setText(QCoreApplication.translate("MainWindow", u"Add To Cart", None))
        self.btnAdd10.setText(QCoreApplication.translate("MainWindow", u"Add To Cart", None))
        self.btnAdd11.setText(QCoreApplication.translate("MainWindow", u"Add To Cart", None))
        self.btnAdd12.setText(QCoreApplication.translate("MainWindow", u"Add To Cart", None))
        self.btnAdd13.setText(QCoreApplication.translate("MainWindow", u"Add To Cart", None))
        self.btnAdd14.setText(QCoreApplication.translate("MainWindow", u"Add To Cart", None))
        self.lblCost14.setText("")
        self.btnAdd15.setText(QCoreApplication.translate("MainWindow", u"Add To Cart", None))
        self.lblCost15.setText("")
        self.btnAdd16.setText(QCoreApplication.translate("MainWindow", u"Add To Cart", None))
        self.btnAdd17.setText(QCoreApplication.translate("MainWindow", u"Add To Cart", None))
        self.btnAdd18.setText(QCoreApplication.translate("MainWindow", u"Add To Cart", None))
        self.btnAdd19.setText(QCoreApplication.translate("MainWindow", u"Add To Cart", None))
        self.btnAdd20.setText(QCoreApplication.translate("MainWindow", u"Add To Cart", None))
        self.btnAdd21.setText(QCoreApplication.translate("MainWindow", u"Add To Cart", None))
        self.btnAdd22.setText(QCoreApplication.translate("MainWindow", u"Add To Cart", None))
        self.btnAdd23.setText(QCoreApplication.translate("MainWindow", u"Add To Cart", None))
        self.btnAdd24.setText(QCoreApplication.translate("MainWindow", u"Add To Cart", None))
        self.btnAdd27.setText(QCoreApplication.translate("MainWindow", u"Add To Cart", None))
        self.btnAdd26.setText(QCoreApplication.translate("MainWindow", u"Add To Cart", None))
        self.btnAdd25.setText(QCoreApplication.translate("MainWindow", u"Add To Cart", None))
        self.btnAdd28.setText(QCoreApplication.translate("MainWindow", u"Add To Cart", None))
        self.btnAdd29.setText(QCoreApplication.translate("MainWindow", u"Add To Cart", None))
        self.btnAdd30.setText(QCoreApplication.translate("MainWindow", u"Add To Cart", None))
        self.btnAdd31.setText(QCoreApplication.translate("MainWindow", u"Add To Cart", None))
        self.btnAdd32.setText(QCoreApplication.translate("MainWindow", u"Add To Cart", None))
        self.btnAdd33.setText(QCoreApplication.translate("MainWindow", u"Add To Cart", None))
        self.btnAdd34.setText(QCoreApplication.translate("MainWindow", u"Add To Cart", None))
        self.btnAdd35.setText(QCoreApplication.translate("MainWindow", u"Add To Cart", None))
        self.btnAdd36.setText(QCoreApplication.translate("MainWindow", u"Add To Cart", None))
        self.btnAdd37.setText(QCoreApplication.translate("MainWindow", u"Add To Cart", None))
        self.btnAdd38.setText(QCoreApplication.translate("MainWindow", u"Add To Cart", None))
        self.btnAdd39.setText(QCoreApplication.translate("MainWindow", u"Add To Cart", None))
        self.btnAdd40.setText(QCoreApplication.translate("MainWindow", u"Add To Cart", None))
        self.btnAdd41.setText(QCoreApplication.translate("MainWindow", u"Add To Cart", None))
        self.btnAdd42.setText(QCoreApplication.translate("MainWindow", u"Add To Cart", None))
        self.btnAdd45.setText(QCoreApplication.translate("MainWindow", u"Add To Cart", None))
        self.btnAdd47.setText(QCoreApplication.translate("MainWindow", u"Add To Cart", None))
        self.btnAdd49.setText(QCoreApplication.translate("MainWindow", u"Add To Cart", None))
        self.lblCoffee_9.setText(QCoreApplication.translate("MainWindow", u"Order Details", None))
        self.lblCoffee_10.setText(QCoreApplication.translate("MainWindow", u"MIEN TAY CONSTRUCTION UNIVERSITY", None))
        self.lbname1.setText("")
        self.lbgia1.setText("")
        self.lbgia3.setText("")
        self.lbname3.setText("")
        self.lbgia2.setText("")
        self.lbname2.setText("")
        self.lbname4.setText("")
        self.lbgia4.setText("")
        self.lbgia5.setText("")
        self.lbname5.setText("")
        self.lbgia6.setText("")
        self.lbname6.setText("")
        self.lbgia7.setText("")
        self.lbname7.setText("")
        self.lbgia8.setText("")
        self.lbname8.setText("")
        self.lbgia9.setText("")
        self.lbname9.setText("")
        self.lbname10.setText("")
        self.lbgia10.setText("")
        self.lbgia12.setText("")
        self.lbname12.setText("")
        self.lbgia11.setText("")
        self.lbname11.setText("")
        self.lbname13.setText("")
        self.lbgia13.setText("")
        self.lbname14.setText("")
        self.lbgia14.setText("")
        self.lbgia15.setText("")
        self.lbname15.setText("")
        self.btnXGH.setText(QCoreApplication.translate("MainWindow", u"X\u00f3a gi\u1ecf h\u00e0ng", None))
        self.btnMua.setText(QCoreApplication.translate("MainWindow", u"Mua", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"TH\u00c0NH TI\u1ec0N: ", None))
        self.lbThanhtien_3.setText("")
        self.lblCoffee_17.setText(QCoreApplication.translate("MainWindow", u"GEMINI MODEL 2.0-pro-exp", None))
        self.lblCoffee_18.setText(QCoreApplication.translate("MainWindow", u"MIEN TAY CONSTRUCTION UNIVERSITY", None))
        self.textBrowser.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Tahoma'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Times New Roman'; font-size:18pt;\"><br /></p></body></html>", None))
        self.lineEdit.setText("")
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"AI MTU...", None))
        self.pushButton1.setText("")
        self.lblCoffee_15.setText(QCoreApplication.translate("MainWindow", u"Order Details", None))
        self.lblCoffee_16.setText(QCoreApplication.translate("MainWindow", u"MIEN TAY CONSTRUCTION UNIVERSITY", None))
        self.lblCoffee_6.setText(QCoreApplication.translate("MainWindow", u"DATABASE", None))
        self.lblCoffee_7.setText(QCoreApplication.translate("MainWindow", u"MIEN TAY CONSTRUCTION UNIVERSITY", None))
        self.btnXoaDB.setText(QCoreApplication.translate("MainWindow", u"X\u00d3A", None))
        self.btnAddDB.setText(QCoreApplication.translate("MainWindow", u"TH\u00caM", None))
        self.btnUpdateDB.setText(QCoreApplication.translate("MainWindow", u"UPDATE", None))
        self.btnXem.setText(QCoreApplication.translate("MainWindow", u"XEM", None))
    # retranslateUi

