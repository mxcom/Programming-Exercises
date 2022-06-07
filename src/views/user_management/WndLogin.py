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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QLineEdit,
    QMainWindow, QPushButton, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(275, 350)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayoutWidget = QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(0, 111, 281, 27))
        self.loEmail = QHBoxLayout(self.horizontalLayoutWidget)
        self.loEmail.setSpacing(0)
        self.loEmail.setObjectName(u"loEmail")
        self.loEmail.setContentsMargins(0, 0, 0, 0)
        self.hsLeft = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.loEmail.addItem(self.hsLeft)

        self.leEmail = QLineEdit(self.horizontalLayoutWidget)
        self.leEmail.setObjectName(u"leEmail")

        self.loEmail.addWidget(self.leEmail)

        self.hsRight = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.loEmail.addItem(self.hsRight)

        self.lbEmail = QLabel(self.centralwidget)
        self.lbEmail.setObjectName(u"lbEmail")
        self.lbEmail.setGeometry(QRect(0, 80, 275, 27))
        font = QFont()
        font.setPointSize(15)
        self.lbEmail.setFont(font)
        self.lbEmail.setAlignment(Qt.AlignCenter)
        self.lbTitle = QLabel(self.centralwidget)
        self.lbTitle.setObjectName(u"lbTitle")
        self.lbTitle.setGeometry(QRect(0, 1, 275, 36))
        font1 = QFont()
        font1.setPointSize(20)
        self.lbTitle.setFont(font1)
        self.lbTitle.setAlignment(Qt.AlignCenter)
        self.verticalLayoutWidget_2 = QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setObjectName(u"verticalLayoutWidget_2")
        self.verticalLayoutWidget_2.setGeometry(QRect(0, 221, 281, 58))
        self.loBtn = QVBoxLayout(self.verticalLayoutWidget_2)
        self.loBtn.setObjectName(u"loBtn")
        self.loBtn.setContentsMargins(85, 0, 85, 0)
        self.btnLogin = QPushButton(self.verticalLayoutWidget_2)
        self.btnLogin.setObjectName(u"btnLogin")

        self.loBtn.addWidget(self.btnLogin)

        self.btnSignup = QPushButton(self.verticalLayoutWidget_2)
        self.btnSignup.setObjectName(u"btnSignup")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.btnSignup.sizePolicy().hasHeightForWidth())
        self.btnSignup.setSizePolicy(sizePolicy1)
        self.btnSignup.setStyleSheet(u"border-color: transparent;\n"
"background-color: transparent;")

        self.loBtn.addWidget(self.btnSignup)

        self.horizontalLayoutWidget_2 = QWidget(self.centralwidget)
        self.horizontalLayoutWidget_2.setObjectName(u"horizontalLayoutWidget_2")
        self.horizontalLayoutWidget_2.setGeometry(QRect(0, 181, 281, 27))
        self.loPassword = QHBoxLayout(self.horizontalLayoutWidget_2)
        self.loPassword.setSpacing(0)
        self.loPassword.setObjectName(u"loPassword")
        self.loPassword.setContentsMargins(0, 0, 0, 0)
        self.hsLeft_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.loPassword.addItem(self.hsLeft_2)

        self.lePassword = QLineEdit(self.horizontalLayoutWidget_2)
        self.lePassword.setObjectName(u"lePassword")
        self.lePassword.setEchoMode(QLineEdit.Password)

        self.loPassword.addWidget(self.lePassword)

        self.hsRight_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.loPassword.addItem(self.hsRight_2)

        self.lbPassword = QLabel(self.centralwidget)
        self.lbPassword.setObjectName(u"lbPassword")
        self.lbPassword.setGeometry(QRect(0, 150, 275, 27))
        self.lbPassword.setFont(font)
        self.lbPassword.setAlignment(Qt.AlignCenter)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.lbEmail.setText(QCoreApplication.translate("MainWindow", u"Email", None))
        self.lbTitle.setText(QCoreApplication.translate("MainWindow", u"Login", None))
        self.btnLogin.setText(QCoreApplication.translate("MainWindow", u"Login", None))
        self.btnSignup.setText(QCoreApplication.translate("MainWindow", u"Sign Up", None))
        self.lbPassword.setText(QCoreApplication.translate("MainWindow", u"Password", None))
    # retranslateUi

