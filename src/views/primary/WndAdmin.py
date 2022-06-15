# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'WndAdmin.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QHBoxLayout,
    QHeaderView, QLabel, QLineEdit, QMainWindow,
    QPushButton, QScrollArea, QSizePolicy, QStackedWidget,
    QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget)
import src.views.icons.rc_icons

class Ui_WndAdmin(object):
    def setupUi(self, WndAdmin):
        if not WndAdmin.objectName():
            WndAdmin.setObjectName(u"WndAdmin")
        WndAdmin.resize(1000, 582)
        self.centralwidget = QWidget(WndAdmin)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.topBar = QFrame(self.centralwidget)
        self.topBar.setObjectName(u"topBar")
        self.topBar.setMinimumSize(QSize(0, 40))
        self.topBar.setMaximumSize(QSize(16777215, 40))
        self.topBar.setStyleSheet(u"background-color: rgb(155, 127, 240);\n"
"border:none;\n"
"")
        self.topBar.setFrameShape(QFrame.NoFrame)
        self.topBar.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.topBar)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.toggle = QFrame(self.topBar)
        self.toggle.setObjectName(u"toggle")
        self.toggle.setMaximumSize(QSize(60, 40))
        self.toggle.setStyleSheet(u"background-color: rgb(65, 43, 173);")
        self.toggle.setFrameShape(QFrame.StyledPanel)
        self.toggle.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.toggle)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.btnToggle = QPushButton(self.toggle)
        self.btnToggle.setObjectName(u"btnToggle")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnToggle.sizePolicy().hasHeightForWidth())
        self.btnToggle.setSizePolicy(sizePolicy)
        self.btnToggle.setStyleSheet(u"QPushButton{\n"
"border:none;\n"
"background-color: rgb(122, 100, 189);\n"
"background-image: url(:/icons/toggleIcon.png);\n"
"background-repeat:none;\n"
"background-position: center center;\n"
"}\n"
"\n"
"")

        self.horizontalLayout_3.addWidget(self.btnToggle)


        self.horizontalLayout.addWidget(self.toggle)

        self.description = QFrame(self.topBar)
        self.description.setObjectName(u"description")
        self.description.setStyleSheet(u"border:none;\n"
"")
        self.description.setFrameShape(QFrame.StyledPanel)
        self.description.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.description)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.frName = QFrame(self.description)
        self.frName.setObjectName(u"frName")
        self.frName.setFrameShape(QFrame.StyledPanel)
        self.frName.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frName)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.lbName = QLabel(self.frName)
        self.lbName.setObjectName(u"lbName")
        font = QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.lbName.setFont(font)

        self.horizontalLayout_6.addWidget(self.lbName)


        self.horizontalLayout_5.addWidget(self.frName)

        self.frDate = QFrame(self.description)
        self.frDate.setObjectName(u"frDate")
        self.frDate.setFrameShape(QFrame.StyledPanel)
        self.frDate.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frDate)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.lbDate = QLabel(self.frDate)
        self.lbDate.setObjectName(u"lbDate")
        self.lbDate.setFont(font)
        self.lbDate.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_7.addWidget(self.lbDate)


        self.horizontalLayout_5.addWidget(self.frDate)

        self.frPageDescription = QFrame(self.description)
        self.frPageDescription.setObjectName(u"frPageDescription")
        self.frPageDescription.setFrameShape(QFrame.StyledPanel)
        self.frPageDescription.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frPageDescription)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.lbPageDescription = QLabel(self.frPageDescription)
        self.lbPageDescription.setObjectName(u"lbPageDescription")
        self.lbPageDescription.setFont(font)
        self.lbPageDescription.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.lbPageDescription.setMargin(5)

        self.horizontalLayout_8.addWidget(self.lbPageDescription)


        self.horizontalLayout_5.addWidget(self.frPageDescription)


        self.horizontalLayout.addWidget(self.description)


        self.verticalLayout.addWidget(self.topBar)

        self.mainWidget = QFrame(self.centralwidget)
        self.mainWidget.setObjectName(u"mainWidget")
        self.mainWidget.setFrameShape(QFrame.NoFrame)
        self.mainWidget.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.mainWidget)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.leftMenu = QFrame(self.mainWidget)
        self.leftMenu.setObjectName(u"leftMenu")
        self.leftMenu.setMinimumSize(QSize(60, 0))
        self.leftMenu.setMaximumSize(QSize(60, 16777215))
        self.leftMenu.setStyleSheet(u"background-color: rgb(155, 127, 240);\n"
"border:none\n"
"")
        self.leftMenu.setFrameShape(QFrame.StyledPanel)
        self.leftMenu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.leftMenu)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.bottonMenus = QFrame(self.leftMenu)
        self.bottonMenus.setObjectName(u"bottonMenus")
        self.bottonMenus.setFrameShape(QFrame.StyledPanel)
        self.bottonMenus.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.bottonMenus)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.btnLogout = QPushButton(self.bottonMenus)
        self.btnLogout.setObjectName(u"btnLogout")
        self.btnLogout.setMinimumSize(QSize(0, 40))
        self.btnLogout.setFont(font)
        self.btnLogout.setStyleSheet(u"QPushButton{\n"
"background-image: url(:/icons/logoutIcon.png);\n"
"background-position: left center;\n"
"background-repeat: no-repeat;\n"
"border: none;\n"
"border-left: 14px solid rgb(155, 127, 240);\n"
"text-align: left;\n"
"padding-left: 45px;\n"
"background-color: rgb(155, 127, 240);\n"
"\n"
"\n"
"\n"
"}\n"
"QPushButton:hover{\n"
"	\n"
"	background-color: rgb(122, 100, 189);\n"
"	border-left: 14px solid rgb(122, 100, 189);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(211, 201, 242);\n"
"    border-left: 14px solid rgb(211, 201, 242);\n"
"}")
        self.btnLogout.setIconSize(QSize(25, 25))

        self.verticalLayout_6.addWidget(self.btnLogout)


        self.verticalLayout_2.addWidget(self.bottonMenus, 0, Qt.AlignBottom)


        self.horizontalLayout_2.addWidget(self.leftMenu)

        self.content = QFrame(self.mainWidget)
        self.content.setObjectName(u"content")
        self.content.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-color: rgb(143, 126, 230);\n"
"border:none;\n"
"")
        self.content.setFrameShape(QFrame.StyledPanel)
        self.content.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.content)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget = QStackedWidget(self.content)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.scrollArea = QScrollArea(self.page)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setGeometry(QRect(-1, -1, 941, 541))
        self.scrollArea.setStyleSheet(u"")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 941, 541))
        self.twUsers = QTableWidget(self.scrollAreaWidgetContents)
        if (self.twUsers.columnCount() < 8):
            self.twUsers.setColumnCount(8)
        __qtablewidgetitem = QTableWidgetItem()
        self.twUsers.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.twUsers.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.twUsers.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.twUsers.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.twUsers.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.twUsers.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.twUsers.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.twUsers.setHorizontalHeaderItem(7, __qtablewidgetitem7)
        self.twUsers.setObjectName(u"twUsers")
        self.twUsers.setGeometry(QRect(20, 50, 891, 481))
        self.twUsers.setStyleSheet(u"")
        self.lineEdit = QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(20, 20, 161, 22))
        font1 = QFont()
        font1.setUnderline(False)
        self.lineEdit.setFont(font1)
        self.lineEdit.setAutoFillBackground(False)
        self.lineEdit.setStyleSheet(u"border: 0.5px solid black")
        self.comboBox = QComboBox(self.scrollAreaWidgetContents)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setGeometry(QRect(190, 20, 161, 21))
        self.comboBox.setStyleSheet(u"border: 0.5px solid black")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.stackedWidget.addWidget(self.page)
        self.page2 = QWidget()
        self.page2.setObjectName(u"page2")
        self.stackedWidget.addWidget(self.page2)

        self.verticalLayout_4.addWidget(self.stackedWidget)


        self.horizontalLayout_2.addWidget(self.content)


        self.verticalLayout.addWidget(self.mainWidget)

        WndAdmin.setCentralWidget(self.centralwidget)

        self.retranslateUi(WndAdmin)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(WndAdmin)
    # setupUi

    def retranslateUi(self, WndAdmin):
        WndAdmin.setWindowTitle(QCoreApplication.translate("WndAdmin", u"MainWindow", None))
        self.btnToggle.setText("")
        self.lbName.setText(QCoreApplication.translate("WndAdmin", u" Max Mustermann", None))
        self.lbDate.setText(QCoreApplication.translate("WndAdmin", u"09.06.2022", None))
        self.lbPageDescription.setText(QCoreApplication.translate("WndAdmin", u"Home", None))
        self.btnLogout.setText(QCoreApplication.translate("WndAdmin", u"Logout", None))
        ___qtablewidgetitem = self.twUsers.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("WndAdmin", u"ID", None));
        ___qtablewidgetitem1 = self.twUsers.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("WndAdmin", u"Email", None));
        ___qtablewidgetitem2 = self.twUsers.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("WndAdmin", u"First Name", None));
        ___qtablewidgetitem3 = self.twUsers.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("WndAdmin", u"Last Name", None));
        ___qtablewidgetitem4 = self.twUsers.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("WndAdmin", u"Sex", None));
        ___qtablewidgetitem5 = self.twUsers.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("WndAdmin", u"Birthday", None));
        ___qtablewidgetitem6 = self.twUsers.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("WndAdmin", u"Height", None));
        ___qtablewidgetitem7 = self.twUsers.horizontalHeaderItem(7)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("WndAdmin", u"Password", None));
        self.lineEdit.setText(QCoreApplication.translate("WndAdmin", u"Search", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("WndAdmin", u"ID", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("WndAdmin", u"Email", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("WndAdmin", u"First Name", None))
        self.comboBox.setItemText(3, QCoreApplication.translate("WndAdmin", u"Last Name", None))
        self.comboBox.setItemText(4, QCoreApplication.translate("WndAdmin", u"Sex", None))
        self.comboBox.setItemText(5, QCoreApplication.translate("WndAdmin", u"Birthday", None))
        self.comboBox.setItemText(6, QCoreApplication.translate("WndAdmin", u"Height", None))
        self.comboBox.setItemText(7, QCoreApplication.translate("WndAdmin", u"Password", None))

    # retranslateUi

