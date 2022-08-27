# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'startwindow.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_StartWindow(object):
    def setupUi(self, StartWindow):
        if not StartWindow.objectName():
            StartWindow.setObjectName(u"StartWindow")
        StartWindow.resize(581, 537)
        self.centralwidget = QWidget(StartWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 10, 501, 51))
        font = QFont()
        font.setFamily(u"Bahnschrift")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.worldList = QListWidget(self.centralwidget)
        QListWidgetItem(self.worldList)
        self.worldList.setObjectName(u"worldList")
        self.worldList.setGeometry(QRect(10, 60, 561, 411))
        self.JoinWorld = QPushButton(self.centralwidget)
        self.JoinWorld.setObjectName(u"JoinWorld")
        self.JoinWorld.setEnabled(False)
        self.JoinWorld.setGeometry(QRect(10, 480, 271, 41))
        font1 = QFont()
        font1.setFamily(u"Bahnschrift")
        font1.setPointSize(13)
        self.JoinWorld.setFont(font1)
        self.setings = QPushButton(self.centralwidget)
        self.setings.setObjectName(u"setings")
        self.setings.setGeometry(QRect(520, 10, 51, 41))
        icon = QIcon()
        icon.addFile(u"settings_icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.setings.setIcon(icon)
        self.setings.setIconSize(QSize(32, 32))
        self.DelteWorld = QPushButton(self.centralwidget)
        self.DelteWorld.setObjectName(u"DelteWorld")
        self.DelteWorld.setEnabled(False)
        self.DelteWorld.setGeometry(QRect(290, 480, 281, 41))
        self.DelteWorld.setFont(font1)
        StartWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(StartWindow)

        QMetaObject.connectSlotsByName(StartWindow)
    # setupUi

    def retranslateUi(self, StartWindow):
        StartWindow.setWindowTitle(QCoreApplication.translate("StartWindow", u"2DBox", None))
        self.label.setText(QCoreApplication.translate("StartWindow", u"Select a world", None))

        __sortingEnabled = self.worldList.isSortingEnabled()
        self.worldList.setSortingEnabled(False)
        ___qlistwidgetitem = self.worldList.item(0)
        ___qlistwidgetitem.setText(QCoreApplication.translate("StartWindow", u"Create a new world", None));
        self.worldList.setSortingEnabled(__sortingEnabled)

        self.JoinWorld.setText(QCoreApplication.translate("StartWindow", u"Join the world", None))
#if QT_CONFIG(tooltip)
        self.setings.setToolTip(QCoreApplication.translate("StartWindow", u"Settings", None))
#endif // QT_CONFIG(tooltip)
        self.setings.setText("")
        self.DelteWorld.setText(QCoreApplication.translate("StartWindow", u"Delte the world", None))
    # retranslateUi

