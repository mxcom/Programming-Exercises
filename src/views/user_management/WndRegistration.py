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
from PySide6.QtWidgets import (QApplication, QComboBox, QDoubleSpinBox, QFormLayout,
    QFrame, QHBoxLayout, QLabel, QLineEdit,
    QMainWindow, QPushButton, QSizePolicy, QStackedWidget,
    QVBoxLayout, QWidget)

class Ui_WndRegistration(object):
    def setupUi(self, WndRegistration):
        if not WndRegistration.objectName():
            WndRegistration.setObjectName(u"WndRegistration")
        WndRegistration.resize(408, 311)
        self.centralwidget = QWidget(WndRegistration)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(0, 50))
        self.label.setMaximumSize(QSize(16777215, 50))
        font = QFont()
        font.setPointSize(15)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setStyleSheet(u"background-color: rgb(211, 201, 242);\n"
"border-radius: 15px")
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label)

        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.page1 = QWidget()
        self.page1.setObjectName(u"page1")
        self.verticalLayout_2 = QVBoxLayout(self.page1)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.page1)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"background-color: rgb(155, 127, 240);\n"
"border-radius: 15px;")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.formLayout = QFormLayout(self.frame)
        self.formLayout.setObjectName(u"formLayout")
        self.lbEmail = QLabel(self.frame)
        self.lbEmail.setObjectName(u"lbEmail")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.lbEmail)

        self.lineEdit = QLineEdit(self.frame)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setStyleSheet(u"border-bottom: 2px solid rgb(211, 201, 242);\n"
"")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.lineEdit)

        self.lbPassword = QLabel(self.frame)
        self.lbPassword.setObjectName(u"lbPassword")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.lbPassword)

        self.lineEdit_2 = QLineEdit(self.frame)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setStyleSheet(u"border-bottom: 2px solid rgb(211, 201, 242);\n"
"")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.lineEdit_2)

        self.lbConfirmPw = QLabel(self.frame)
        self.lbConfirmPw.setObjectName(u"lbConfirmPw")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.lbConfirmPw)

        self.lineEdit_3 = QLineEdit(self.frame)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setStyleSheet(u"border-bottom: 2px solid rgb(211, 201, 242);\n"
"")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.lineEdit_3)

        self.lbError = QLabel(self.frame)
        self.lbError.setObjectName(u"lbError")
        self.lbError.setAlignment(Qt.AlignCenter)

        self.formLayout.setWidget(3, QFormLayout.SpanningRole, self.lbError)


        self.verticalLayout_2.addWidget(self.frame)

        self.frame_2 = QFrame(self.page1)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMaximumSize(QSize(16777215, 50))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_2)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.btnCancel = QPushButton(self.frame_2)
        self.btnCancel.setObjectName(u"btnCancel")
        self.btnCancel.setMinimumSize(QSize(160, 40))
        self.btnCancel.setMaximumSize(QSize(160, 40))
        font1 = QFont()
        font1.setPointSize(12)
        font1.setBold(True)
        self.btnCancel.setFont(font1)
        self.btnCancel.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(155, 127, 240);\n"
"	border-radius: 15px;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(122, 100, 189);\n"
"	border-radius: 15px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(211, 201, 242);\n"
"	border-radius: 15px;\n"
"}")

        self.horizontalLayout.addWidget(self.btnCancel)

        self.btnNext = QPushButton(self.frame_2)
        self.btnNext.setObjectName(u"btnNext")
        self.btnNext.setMinimumSize(QSize(160, 40))
        self.btnNext.setMaximumSize(QSize(160, 40))
        self.btnNext.setFont(font1)
        self.btnNext.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(155, 127, 240);\n"
"	border-radius: 15px;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(122, 100, 189);\n"
"	border-radius: 15px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(211, 201, 242);\n"
"	border-radius: 15px;\n"
"}")

        self.horizontalLayout.addWidget(self.btnNext)


        self.verticalLayout_2.addWidget(self.frame_2)

        self.stackedWidget.addWidget(self.page1)
        self.page2 = QWidget()
        self.page2.setObjectName(u"page2")
        self.verticalLayout_3 = QVBoxLayout(self.page2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame_3 = QFrame(self.page2)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setStyleSheet(u"background-color: rgb(155, 127, 240);\n"
"border-radius: 15px;")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.formLayout_2 = QFormLayout(self.frame_3)
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.lbFirstName = QLabel(self.frame_3)
        self.lbFirstName.setObjectName(u"lbFirstName")

        self.formLayout_2.setWidget(0, QFormLayout.LabelRole, self.lbFirstName)

        self.leFirstName = QLineEdit(self.frame_3)
        self.leFirstName.setObjectName(u"leFirstName")
        self.leFirstName.setStyleSheet(u"border-bottom: 2px solid rgb(211, 201, 242);")

        self.formLayout_2.setWidget(0, QFormLayout.FieldRole, self.leFirstName)

        self.lbLastName = QLabel(self.frame_3)
        self.lbLastName.setObjectName(u"lbLastName")

        self.formLayout_2.setWidget(1, QFormLayout.LabelRole, self.lbLastName)

        self.leLastName = QLineEdit(self.frame_3)
        self.leLastName.setObjectName(u"leLastName")
        self.leLastName.setStyleSheet(u"border-bottom: 2px solid rgb(211, 201, 242);")

        self.formLayout_2.setWidget(1, QFormLayout.FieldRole, self.leLastName)

        self.lbBirthdate = QLabel(self.frame_3)
        self.lbBirthdate.setObjectName(u"lbBirthdate")

        self.formLayout_2.setWidget(2, QFormLayout.LabelRole, self.lbBirthdate)

        self.lbSex = QLabel(self.frame_3)
        self.lbSex.setObjectName(u"lbSex")

        self.formLayout_2.setWidget(3, QFormLayout.LabelRole, self.lbSex)

        self.cbSex = QComboBox(self.frame_3)
        self.cbSex.setObjectName(u"cbSex")
        self.cbSex.setStyleSheet(u"border-bottom: 2px solid rgb(211, 201, 242);")

        self.formLayout_2.setWidget(3, QFormLayout.FieldRole, self.cbSex)

        self.lbWeight = QLabel(self.frame_3)
        self.lbWeight.setObjectName(u"lbWeight")

        self.formLayout_2.setWidget(4, QFormLayout.LabelRole, self.lbWeight)

        self.frame_5 = QFrame(self.frame_3)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_3.setSpacing(10)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.cbDay = QComboBox(self.frame_5)
        self.cbDay.setObjectName(u"cbDay")
        self.cbDay.setStyleSheet(u"border-bottom: 2px solid rgb(211, 201, 242);")

        self.horizontalLayout_3.addWidget(self.cbDay)

        self.cbMonth = QComboBox(self.frame_5)
        self.cbMonth.setObjectName(u"cbMonth")
        self.cbMonth.setStyleSheet(u"border-bottom: 2px solid rgb(211, 201, 242);")

        self.horizontalLayout_3.addWidget(self.cbMonth)

        self.cbYear = QComboBox(self.frame_5)
        self.cbYear.setObjectName(u"cbYear")
        self.cbYear.setStyleSheet(u"border-bottom: 2px solid rgb(211, 201, 242);")

        self.horizontalLayout_3.addWidget(self.cbYear)


        self.formLayout_2.setWidget(2, QFormLayout.FieldRole, self.frame_5)

        self.frame_6 = QFrame(self.frame_3)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.leWeight = QLineEdit(self.frame_6)
        self.leWeight.setObjectName(u"leWeight")
        self.leWeight.setMaximumSize(QSize(120, 16777215))
        self.leWeight.setStyleSheet(u"border-bottom: 2px solid rgb(211, 201, 242);")

        self.horizontalLayout_4.addWidget(self.leWeight)

        self.frame_7 = QFrame(self.frame_6)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setMaximumSize(QSize(15, 16777215))
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_4.addWidget(self.frame_7)

        self.lbHeight = QLabel(self.frame_6)
        self.lbHeight.setObjectName(u"lbHeight")

        self.horizontalLayout_4.addWidget(self.lbHeight)

        self.sbHeight = QDoubleSpinBox(self.frame_6)
        self.sbHeight.setObjectName(u"sbHeight")

        self.horizontalLayout_4.addWidget(self.sbHeight)


        self.formLayout_2.setWidget(4, QFormLayout.FieldRole, self.frame_6)


        self.verticalLayout_3.addWidget(self.frame_3)

        self.frame_4 = QFrame(self.page2)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMaximumSize(QSize(16777215, 50))
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.btnBack = QPushButton(self.frame_4)
        self.btnBack.setObjectName(u"btnBack")
        self.btnBack.setMinimumSize(QSize(160, 40))
        self.btnBack.setMaximumSize(QSize(160, 40))
        self.btnBack.setFont(font1)
        self.btnBack.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(155, 127, 240);\n"
"	border-radius: 15px;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(122, 100, 189);\n"
"	border-radius: 15px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(211, 201, 242);\n"
"	border-radius: 15px;\n"
"}")

        self.horizontalLayout_2.addWidget(self.btnBack)

        self.btnFinish = QPushButton(self.frame_4)
        self.btnFinish.setObjectName(u"btnFinish")
        self.btnFinish.setMinimumSize(QSize(160, 40))
        self.btnFinish.setMaximumSize(QSize(160, 40))
        self.btnFinish.setFont(font1)
        self.btnFinish.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(155, 127, 240);\n"
"	border-radius: 15px;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(122, 100, 189);\n"
"	border-radius: 15px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(211, 201, 242);\n"
"	border-radius: 15px;\n"
"}")

        self.horizontalLayout_2.addWidget(self.btnFinish)


        self.verticalLayout_3.addWidget(self.frame_4)

        self.stackedWidget.addWidget(self.page2)

        self.verticalLayout.addWidget(self.stackedWidget)

        WndRegistration.setCentralWidget(self.centralwidget)

        self.retranslateUi(WndRegistration)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(WndRegistration)
    # setupUi

    def retranslateUi(self, WndRegistration):
        WndRegistration.setWindowTitle(QCoreApplication.translate("WndRegistration", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("WndRegistration", u"Registration", None))
        self.lbEmail.setText(QCoreApplication.translate("WndRegistration", u"Email:", None))
        self.lbPassword.setText(QCoreApplication.translate("WndRegistration", u"Password:", None))
        self.lbConfirmPw.setText(QCoreApplication.translate("WndRegistration", u"Confirm Password:", None))
        self.lbError.setText(QCoreApplication.translate("WndRegistration", u"TextLabel", None))
        self.btnCancel.setText(QCoreApplication.translate("WndRegistration", u"Cancel", None))
        self.btnNext.setText(QCoreApplication.translate("WndRegistration", u"Next", None))
        self.lbFirstName.setText(QCoreApplication.translate("WndRegistration", u"First Name:", None))
        self.lbLastName.setText(QCoreApplication.translate("WndRegistration", u"Last Name:", None))
        self.lbBirthdate.setText(QCoreApplication.translate("WndRegistration", u"Birthdate:", None))
        self.lbSex.setText(QCoreApplication.translate("WndRegistration", u"Sex:", None))
        self.lbWeight.setText(QCoreApplication.translate("WndRegistration", u"Weight:", None))
        self.lbHeight.setText(QCoreApplication.translate("WndRegistration", u"Height:", None))
        self.btnBack.setText(QCoreApplication.translate("WndRegistration", u"Back", None))
        self.btnFinish.setText(QCoreApplication.translate("WndRegistration", u"Finish", None))
    # retranslateUi

