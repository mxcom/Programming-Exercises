# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'WndRegistration.ui'
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
from PySide6.QtWidgets import (QAbstractSpinBox, QApplication, QComboBox, QDateEdit,
    QDoubleSpinBox, QFormLayout, QFrame, QHBoxLayout,
    QLabel, QLineEdit, QMainWindow, QPushButton,
    QSizePolicy, QStackedWidget, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(408, 311)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.header = QFrame(self.centralwidget)
        self.header.setObjectName(u"header")
        self.header.setFrameShape(QFrame.StyledPanel)
        self.header.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.header)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.title = QLabel(self.header)
        self.title.setObjectName(u"title")
        font = QFont()
        font.setFamilies([u"Segoe UI"])
        font.setPointSize(30)
        font.setStyleStrategy(QFont.PreferAntialias)
        self.title.setFont(font)
        self.title.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.title)


        self.verticalLayout.addWidget(self.header)

        self.content = QFrame(self.centralwidget)
        self.content.setObjectName(u"content")
        self.content.setMinimumSize(QSize(0, 0))
        self.content.setFrameShape(QFrame.StyledPanel)
        self.content.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.content)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget = QStackedWidget(self.content)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.page1 = QWidget()
        self.page1.setObjectName(u"page1")
        self.verticalLayout_3 = QVBoxLayout(self.page1)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.formular = QFrame(self.page1)
        self.formular.setObjectName(u"formular")
        self.formular.setFrameShape(QFrame.StyledPanel)
        self.formular.setFrameShadow(QFrame.Raised)
        self.formLayout = QFormLayout(self.formular)
        self.formLayout.setObjectName(u"formLayout")
        self.lbEmail = QLabel(self.formular)
        self.lbEmail.setObjectName(u"lbEmail")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.lbEmail)

        self.leEmail = QLineEdit(self.formular)
        self.leEmail.setObjectName(u"leEmail")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.leEmail)

        self.lbPassword = QLabel(self.formular)
        self.lbPassword.setObjectName(u"lbPassword")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.lbPassword)

        self.lePassword = QLineEdit(self.formular)
        self.lePassword.setObjectName(u"lePassword")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.lePassword)

        self.lbConfirmPw = QLabel(self.formular)
        self.lbConfirmPw.setObjectName(u"lbConfirmPw")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.lbConfirmPw)

        self.leConfirmPw = QLineEdit(self.formular)
        self.leConfirmPw.setObjectName(u"leConfirmPw")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.leConfirmPw)


        self.verticalLayout_3.addWidget(self.formular)

        self.navigation = QFrame(self.page1)
        self.navigation.setObjectName(u"navigation")
        self.navigation.setMaximumSize(QSize(16777215, 40))
        self.navigation.setFrameShape(QFrame.StyledPanel)
        self.navigation.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.navigation)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.btnCancel = QPushButton(self.navigation)
        self.btnCancel.setObjectName(u"btnCancel")

        self.horizontalLayout_2.addWidget(self.btnCancel)

        self.btnNext = QPushButton(self.navigation)
        self.btnNext.setObjectName(u"btnNext")

        self.horizontalLayout_2.addWidget(self.btnNext)


        self.verticalLayout_3.addWidget(self.navigation)

        self.stackedWidget.addWidget(self.page1)
        self.page2 = QWidget()
        self.page2.setObjectName(u"page2")
        self.verticalLayout_4 = QVBoxLayout(self.page2)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.page2)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.formLayout_2 = QFormLayout(self.frame)
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.lbFirstName = QLabel(self.frame)
        self.lbFirstName.setObjectName(u"lbFirstName")

        self.formLayout_2.setWidget(0, QFormLayout.LabelRole, self.lbFirstName)

        self.leFirstName = QLineEdit(self.frame)
        self.leFirstName.setObjectName(u"leFirstName")

        self.formLayout_2.setWidget(0, QFormLayout.FieldRole, self.leFirstName)

        self.lbLastName = QLabel(self.frame)
        self.lbLastName.setObjectName(u"lbLastName")

        self.formLayout_2.setWidget(1, QFormLayout.LabelRole, self.lbLastName)

        self.leLastName = QLineEdit(self.frame)
        self.leLastName.setObjectName(u"leLastName")

        self.formLayout_2.setWidget(1, QFormLayout.FieldRole, self.leLastName)

        self.lbBirthdate = QLabel(self.frame)
        self.lbBirthdate.setObjectName(u"lbBirthdate")

        self.formLayout_2.setWidget(2, QFormLayout.LabelRole, self.lbBirthdate)

        self.dpBirthdate = QDateEdit(self.frame)
        self.dpBirthdate.setObjectName(u"dpBirthdate")

        self.formLayout_2.setWidget(2, QFormLayout.FieldRole, self.dpBirthdate)

        self.lbSex = QLabel(self.frame)
        self.lbSex.setObjectName(u"lbSex")

        self.formLayout_2.setWidget(3, QFormLayout.LabelRole, self.lbSex)

        self.cbSex = QComboBox(self.frame)
        self.cbSex.setObjectName(u"cbSex")

        self.formLayout_2.setWidget(3, QFormLayout.FieldRole, self.cbSex)

        self.lbWeight = QLabel(self.frame)
        self.lbWeight.setObjectName(u"lbWeight")

        self.formLayout_2.setWidget(4, QFormLayout.LabelRole, self.lbWeight)

        self.leWeight = QLineEdit(self.frame)
        self.leWeight.setObjectName(u"leWeight")

        self.formLayout_2.setWidget(4, QFormLayout.FieldRole, self.leWeight)

        self.lbHeight = QLabel(self.frame)
        self.lbHeight.setObjectName(u"lbHeight")

        self.formLayout_2.setWidget(5, QFormLayout.LabelRole, self.lbHeight)

        self.sbHeight = QDoubleSpinBox(self.frame)
        self.sbHeight.setObjectName(u"sbHeight")
        self.sbHeight.setDecimals(2)
        self.sbHeight.setMinimum(0.000000000000000)
        self.sbHeight.setMaximum(250.000000000000000)
        self.sbHeight.setStepType(QAbstractSpinBox.AdaptiveDecimalStepType)
        self.sbHeight.setValue(0.000000000000000)

        self.formLayout_2.setWidget(5, QFormLayout.FieldRole, self.sbHeight)


        self.verticalLayout_4.addWidget(self.frame)

        self.navigation2 = QFrame(self.page2)
        self.navigation2.setObjectName(u"navigation2")
        self.navigation2.setMaximumSize(QSize(16777215, 40))
        self.navigation2.setFrameShape(QFrame.StyledPanel)
        self.navigation2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.navigation2)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.btnCancel2 = QPushButton(self.navigation2)
        self.btnCancel2.setObjectName(u"btnCancel2")

        self.horizontalLayout_3.addWidget(self.btnCancel2)

        self.btnFinish = QPushButton(self.navigation2)
        self.btnFinish.setObjectName(u"btnFinish")

        self.horizontalLayout_3.addWidget(self.btnFinish)


        self.verticalLayout_4.addWidget(self.navigation2)

        self.stackedWidget.addWidget(self.page2)

        self.horizontalLayout.addWidget(self.stackedWidget)


        self.verticalLayout.addWidget(self.content)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.title.setText(QCoreApplication.translate("MainWindow", u"Registration", None))
        self.lbEmail.setText(QCoreApplication.translate("MainWindow", u"Email", None))
        self.lbPassword.setText(QCoreApplication.translate("MainWindow", u"Password", None))
        self.lbConfirmPw.setText(QCoreApplication.translate("MainWindow", u"Confirm Password", None))
        self.btnCancel.setText(QCoreApplication.translate("MainWindow", u"Cancel", None))
        self.btnNext.setText(QCoreApplication.translate("MainWindow", u"Next", None))
        self.lbFirstName.setText(QCoreApplication.translate("MainWindow", u"First Name", None))
        self.lbLastName.setText(QCoreApplication.translate("MainWindow", u"Last Name", None))
        self.lbBirthdate.setText(QCoreApplication.translate("MainWindow", u"Birthdate", None))
        self.lbSex.setText(QCoreApplication.translate("MainWindow", u"Sex", None))
        self.lbWeight.setText(QCoreApplication.translate("MainWindow", u"Weight", None))
        self.lbHeight.setText(QCoreApplication.translate("MainWindow", u"Height", None))
        self.sbHeight.setPrefix("")
        self.btnCancel2.setText(QCoreApplication.translate("MainWindow", u"Cancel", None))
        self.btnFinish.setText(QCoreApplication.translate("MainWindow", u"Finish", None))
    # retranslateUi

