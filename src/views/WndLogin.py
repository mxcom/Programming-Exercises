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
    QPushButton, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)

class Ui_WndLogin(object):
    def setupUi(self, WndLogin):
        if not WndLogin.objectName():
            WndLogin.setObjectName(u"WndLogin")
        WndLogin.resize(275, 350)
        WndLogin.setMinimumSize(QSize(275, 350))
        WndLogin.setMaximumSize(QSize(275, 350))
        self.verticalLayoutWidget_2 = QWidget(WndLogin)
        self.verticalLayoutWidget_2.setObjectName(u"verticalLayoutWidget_2")
        self.verticalLayoutWidget_2.setGeometry(QRect(0, 220, 281, 56))
        self.loBtn = QVBoxLayout(self.verticalLayoutWidget_2)
        self.loBtn.setObjectName(u"loBtn")
        self.loBtn.setContentsMargins(85, 0, 85, 0)
        self.btnLogin = QPushButton(self.verticalLayoutWidget_2)
        self.btnLogin.setObjectName(u"btnLogin")

        self.loBtn.addWidget(self.btnLogin)

        self.btnSignup = QPushButton(self.verticalLayoutWidget_2)
        self.btnSignup.setObjectName(u"btnSignup")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnSignup.sizePolicy().hasHeightForWidth())
        self.btnSignup.setSizePolicy(sizePolicy)
        self.btnSignup.setStyleSheet(u"border-color: transparent;\n"
"background-color: transparent;")

        self.loBtn.addWidget(self.btnSignup)

        self.horizontalLayoutWidget = QWidget(WndLogin)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(0, 110, 281, 24))
        self.loEmail = QHBoxLayout(self.horizontalLayoutWidget)
        self.loEmail.setSpacing(0)
        self.loEmail.setObjectName(u"loEmail")
        self.loEmail.setContentsMargins(0, 0, 0, 0)
        self.hsLeft = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.loEmail.addItem(self.hsLeft)

        self.ipEmial = QLineEdit(self.horizontalLayoutWidget)
        self.ipEmial.setObjectName(u"ipEmial")

        self.loEmail.addWidget(self.ipEmial)

        self.hsRight = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.loEmail.addItem(self.hsRight)

        self.lbEmail = QLabel(WndLogin)
        self.lbEmail.setObjectName(u"lbEmail")
        self.lbEmail.setGeometry(QRect(0, 79, 275, 27))
        font = QFont()
        font.setPointSize(15)
        self.lbEmail.setFont(font)
        self.lbEmail.setAlignment(Qt.AlignCenter)
        self.lbTitle = QLabel(WndLogin)
        self.lbTitle.setObjectName(u"lbTitle")
        self.lbTitle.setGeometry(QRect(0, 0, 275, 36))
        font1 = QFont()
        font1.setPointSize(20)
        self.lbTitle.setFont(font1)
        self.lbTitle.setAlignment(Qt.AlignCenter)
        self.lbPassword = QLabel(WndLogin)
        self.lbPassword.setObjectName(u"lbPassword")
        self.lbPassword.setGeometry(QRect(0, 149, 275, 27))
        self.lbPassword.setFont(font)
        self.lbPassword.setAlignment(Qt.AlignCenter)
        self.horizontalLayoutWidget_2 = QWidget(WndLogin)
        self.horizontalLayoutWidget_2.setObjectName(u"horizontalLayoutWidget_2")
        self.horizontalLayoutWidget_2.setGeometry(QRect(0, 180, 281, 24))
        self.loPassword = QHBoxLayout(self.horizontalLayoutWidget_2)
        self.loPassword.setSpacing(0)
        self.loPassword.setObjectName(u"loPassword")
        self.loPassword.setContentsMargins(0, 0, 0, 0)
        self.hsLeft_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.loPassword.addItem(self.hsLeft_2)

        self.ipEmial_2 = QLineEdit(self.horizontalLayoutWidget_2)
        self.ipEmial_2.setObjectName(u"ipEmial_2")

        self.loPassword.addWidget(self.ipEmial_2)

        self.hsRight_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.loPassword.addItem(self.hsRight_2)


        self.retranslateUi(WndLogin)

        QMetaObject.connectSlotsByName(WndLogin)
    # setupUi

    def retranslateUi(self, WndLogin):
        WndLogin.setWindowTitle(QCoreApplication.translate("WndLogin", u"Form", None))
        self.btnLogin.setText(QCoreApplication.translate("WndLogin", u"Login", None))
        self.btnSignup.setText(QCoreApplication.translate("WndLogin", u"Sign Up", None))
        self.lbEmail.setText(QCoreApplication.translate("WndLogin", u"Email", None))
        self.lbTitle.setText(QCoreApplication.translate("WndLogin", u"Login", None))
        self.lbPassword.setText(QCoreApplication.translate("WndLogin", u"Password", None))
    # retranslateUi

