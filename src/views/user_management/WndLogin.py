# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'WndLogin.ui'
##
## Created by: Qt User Interface Compiler version 6.3.0
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
    QVBoxLayout, QWidget)

class Ui_WndLogin(object):
    def setupUi(self, WndLogin):
        if not WndLogin.objectName():
            WndLogin.setObjectName(u"WndLogin")
        WndLogin.resize(275, 350)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(WndLogin.sizePolicy().hasHeightForWidth())
        WndLogin.setSizePolicy(sizePolicy)
        WndLogin.setMinimumSize(QSize(275, 350))
        WndLogin.setMaximumSize(QSize(275, 350))
        self.centralwidget = QWidget(WndLogin)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame_2)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(self.frame_2)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(16777215, 50))
        font = QFont()
        font.setPointSize(18)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setStyleSheet(u"background-color: rgb(211, 201, 242);\n"
"border-radius: 15px")
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label)

        self.frame_5 = QFrame(self.frame_2)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setStyleSheet(u"background-color: rgb(155, 127, 240);\n"
"border-radius: 15px;\n"
"")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_5)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.frame = QFrame(self.frame_5)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.lbEmail = QLabel(self.frame)
        self.lbEmail.setObjectName(u"lbEmail")
        font1 = QFont()
        font1.setPointSize(12)
        font1.setBold(True)
        self.lbEmail.setFont(font1)

        self.verticalLayout_3.addWidget(self.lbEmail)

        self.leEmail = QLineEdit(self.frame)
        self.leEmail.setObjectName(u"leEmail")
        self.leEmail.setStyleSheet(u"border-bottom: 2px solid rgb(211, 201, 242);\n"
"")

        self.verticalLayout_3.addWidget(self.leEmail)


        self.verticalLayout_2.addWidget(self.frame)

        self.frame_3 = QFrame(self.frame_5)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_3)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.lbPassword = QLabel(self.frame_3)
        self.lbPassword.setObjectName(u"lbPassword")
        self.lbPassword.setFont(font1)

        self.verticalLayout_4.addWidget(self.lbPassword)

        self.lePassword = QLineEdit(self.frame_3)
        self.lePassword.setObjectName(u"lePassword")
        self.lePassword.setStyleSheet(u"border-bottom: 2px solid rgb(211, 201, 242);\n"
"")
        self.lePassword.setEchoMode(QLineEdit.Password)

        self.verticalLayout_4.addWidget(self.lePassword)


        self.verticalLayout_2.addWidget(self.frame_3)

        self.frame_4 = QFrame(self.frame_5)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_4)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.frame_6 = QFrame(self.frame_4)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.btnLogin = QPushButton(self.frame_6)
        self.btnLogin.setObjectName(u"btnLogin")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.btnLogin.sizePolicy().hasHeightForWidth())
        self.btnLogin.setSizePolicy(sizePolicy1)
        self.btnLogin.setMinimumSize(QSize(0, 0))
        self.btnLogin.setMaximumSize(QSize(140, 40))
        self.btnLogin.setFont(font1)
        self.btnLogin.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(155, 127, 240);\n"
"	border-radius: 15px ;\n"
"	border: 3px solid rgb(122, 100, 189);\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(122, 100, 189);\n"
"	border-radius: 15px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(211, 201, 242);\n"
"	border-radius: 15px;\n"
"}\n"
"")

        self.horizontalLayout_2.addWidget(self.btnLogin)

        self.btnSignup = QPushButton(self.frame_6)
        self.btnSignup.setObjectName(u"btnSignup")
        sizePolicy1.setHeightForWidth(self.btnSignup.sizePolicy().hasHeightForWidth())
        self.btnSignup.setSizePolicy(sizePolicy1)
        self.btnSignup.setMinimumSize(QSize(0, 0))
        self.btnSignup.setMaximumSize(QSize(140, 40))
        self.btnSignup.setFont(font1)
        self.btnSignup.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(155, 127, 240);\n"
"	border-radius: 15px ;\n"
"	border: 3px solid rgb(122, 100, 189);\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(122, 100, 189);\n"
"	border-radius: 15px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(211, 201, 242);\n"
"	border-radius: 15px;\n"
"}\n"
"")

        self.horizontalLayout_2.addWidget(self.btnSignup)


        self.verticalLayout_5.addWidget(self.frame_6)

        self.label_2 = QLabel(self.frame_4)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setEnabled(True)
        self.label_2.setMaximumSize(QSize(16777215, 25))
        self.label_2.setStyleSheet(u"color: rgb(211, 201, 242)")
        self.label_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_5.addWidget(self.label_2)


        self.verticalLayout_2.addWidget(self.frame_4)


        self.verticalLayout.addWidget(self.frame_5)


        self.horizontalLayout.addWidget(self.frame_2)

        WndLogin.setCentralWidget(self.centralwidget)

        self.retranslateUi(WndLogin)

        QMetaObject.connectSlotsByName(WndLogin)
    # setupUi

    def retranslateUi(self, WndLogin):
        WndLogin.setWindowTitle(QCoreApplication.translate("WndLogin", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("WndLogin", u"Login", None))
        self.lbEmail.setText(QCoreApplication.translate("WndLogin", u"Email", None))
        self.lbPassword.setText(QCoreApplication.translate("WndLogin", u"Password", None))
        self.btnLogin.setText(QCoreApplication.translate("WndLogin", u"Login", None))
        self.btnSignup.setText(QCoreApplication.translate("WndLogin", u"Sign Up", None))
        self.label_2.setText(QCoreApplication.translate("WndLogin", u"Wrong Email or Password", None))
    # retranslateUi

