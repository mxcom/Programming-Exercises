# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'WndMain.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QMainWindow,
    QPushButton, QSizePolicy, QStackedWidget, QVBoxLayout,
    QWidget)

class Ui_WndMain(object):
    def setupUi(self, WndMain):
        if not WndMain.objectName():
            WndMain.setObjectName(u"WndMain")
        WndMain.resize(1000, 560)
        self.centralwidget = QWidget(WndMain)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.topBar = QFrame(self.centralwidget)
        self.topBar.setObjectName(u"topBar")
        self.topBar.setMaximumSize(QSize(16777215, 40))
        self.topBar.setStyleSheet(u"background-color: rgb(83, 56, 224);\n"
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
        self.toggle.setStyleSheet(u"background-color: rgb(75, 75, 75);")
        self.toggle.setFrameShape(QFrame.StyledPanel)
        self.toggle.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.toggle)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.BtnToggle = QPushButton(self.toggle)
        self.BtnToggle.setObjectName(u"BtnToggle")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.BtnToggle.sizePolicy().hasHeightForWidth())
        self.BtnToggle.setSizePolicy(sizePolicy)
        self.BtnToggle.setStyleSheet(u"border: none;\n"
"background-color: rgb(65, 43, 173);")

        self.horizontalLayout_3.addWidget(self.BtnToggle)


        self.horizontalLayout.addWidget(self.toggle)

        self.frame_2 = QFrame(self.topBar)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setStyleSheet(u"border:none;\n"
"")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)

        self.horizontalLayout.addWidget(self.frame_2)


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
        self.leftMenu.setStyleSheet(u"background-color: rgb(83, 56, 224);\n"
"border:none\n"
"")
        self.leftMenu.setFrameShape(QFrame.StyledPanel)
        self.leftMenu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.leftMenu)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.topMenus = QFrame(self.leftMenu)
        self.topMenus.setObjectName(u"topMenus")
        self.topMenus.setFrameShape(QFrame.StyledPanel)
        self.topMenus.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.topMenus)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.btnHome = QPushButton(self.topMenus)
        self.btnHome.setObjectName(u"btnHome")
        self.btnHome.setMinimumSize(QSize(0, 40))
        self.btnHome.setStyleSheet(u"QPushButton{\n"
"color: rgb(255, 255, 255);\n"
"border: 0px solid;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(65, 43, 173);\n"
"}")

        self.verticalLayout_3.addWidget(self.btnHome)

        self.btnFood = QPushButton(self.topMenus)
        self.btnFood.setObjectName(u"btnFood")
        self.btnFood.setMinimumSize(QSize(0, 40))
        self.btnFood.setStyleSheet(u"QPushButton{\n"
"color: rgb(255, 255, 255);\n"
"border: 0px solid;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(65, 43, 173);\n"
"}")

        self.verticalLayout_3.addWidget(self.btnFood)

        self.btnStatistic = QPushButton(self.topMenus)
        self.btnStatistic.setObjectName(u"btnStatistic")
        self.btnStatistic.setMinimumSize(QSize(0, 40))
        self.btnStatistic.setStyleSheet(u"QPushButton{\n"
"color: rgb(255, 255, 255);\n"
"border: 0px solid;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(65, 43, 173);\n"
"}")

        self.verticalLayout_3.addWidget(self.btnStatistic)

        self.btnSettings = QPushButton(self.topMenus)
        self.btnSettings.setObjectName(u"btnSettings")
        self.btnSettings.setMinimumSize(QSize(0, 40))
        self.btnSettings.setStyleSheet(u"QPushButton{\n"
"color: rgb(255, 255, 255);\n"
"border: 0px solid;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(65, 43, 173);\n"
"}")

        self.verticalLayout_3.addWidget(self.btnSettings)


        self.verticalLayout_2.addWidget(self.topMenus, 0, Qt.AlignTop)

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
        self.btnLogout.setStyleSheet(u"QPushButton{\n"
"color: rgb(255, 255, 255);\n"
"border: 0px solid;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(65, 43, 173);\n"
"}")

        self.verticalLayout_6.addWidget(self.btnLogout)


        self.verticalLayout_2.addWidget(self.bottonMenus, 0, Qt.AlignBottom)


        self.horizontalLayout_2.addWidget(self.leftMenu)

        self.content = QFrame(self.mainWidget)
        self.content.setObjectName(u"content")
        self.content.setStyleSheet(u"background-color: rgb(143, 126, 230);\n"
"border-color: rgb(143, 126, 230);\n"
"border:none;\n"
"")
        self.content.setFrameShape(QFrame.StyledPanel)
        self.content.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.content)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.pages = QStackedWidget(self.content)
        self.pages.setObjectName(u"pages")
        self.pages.setStyleSheet(u"background-color: rgb(143, 126, 230);\n"
"border-color: rgb(143, 126, 230);\n"
"border:none;\n"
"")
        self.page_1 = QWidget()
        self.page_1.setObjectName(u"page_1")
        self.page_1.setStyleSheet(u"background-color: rgb(143, 126, 230);\n"
"border-color: rgb(143, 126, 230);\n"
"border:none;\n"
"")
        self.verticalLayout_5 = QVBoxLayout(self.page_1)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.prrogressBar = QFrame(self.page_1)
        self.prrogressBar.setObjectName(u"prrogressBar")
        self.prrogressBar.setFrameShape(QFrame.StyledPanel)
        self.prrogressBar.setFrameShadow(QFrame.Raised)

        self.verticalLayout_5.addWidget(self.prrogressBar)

        self.frame = QFrame(self.page_1)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.frame_4 = QFrame(self.frame)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_4.addWidget(self.frame_4)

        self.frame_5 = QFrame(self.frame)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_4.addWidget(self.frame_5)


        self.verticalLayout_5.addWidget(self.frame)

        self.pages.addWidget(self.page_1)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.pages.addWidget(self.page_2)

        self.verticalLayout_4.addWidget(self.pages)


        self.horizontalLayout_2.addWidget(self.content)


        self.verticalLayout.addWidget(self.mainWidget)

        WndMain.setCentralWidget(self.centralwidget)

        self.retranslateUi(WndMain)

        QMetaObject.connectSlotsByName(WndMain)
    # setupUi

    def retranslateUi(self, WndMain):
        WndMain.setWindowTitle(QCoreApplication.translate("WndMain", u"MainWindow", None))
        self.BtnToggle.setText(QCoreApplication.translate("WndMain", u"PushButton", None))
        self.btnHome.setText(QCoreApplication.translate("WndMain", u"Home", None))
        self.btnFood.setText(QCoreApplication.translate("WndMain", u"Food", None))
        self.btnStatistic.setText(QCoreApplication.translate("WndMain", u"Statistic", None))
        self.btnSettings.setText(QCoreApplication.translate("WndMain", u"Settings", None))
        self.btnLogout.setText(QCoreApplication.translate("WndMain", u"Logout", None))
    # retranslateUi

