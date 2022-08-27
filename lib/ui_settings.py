# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'settings.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_SettingsWindow(object):
    def setupUi(self, SettingsWindow):
        if not SettingsWindow.objectName():
            SettingsWindow.setObjectName(u"SettingsWindow")
        SettingsWindow.resize(318, 170)
        self.centralwidget = QWidget(SettingsWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 20, 301, 41))
        font = QFont()
        font.setFamily(u"Bahnschrift")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.langk = QComboBox(self.centralwidget)
        self.langk.setObjectName(u"langk")
        self.langk.setGeometry(QRect(170, 30, 131, 31))
        self.layoutWidget = QWidget(self.centralwidget)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(0, 120, 311, 41))
        self.horizontalLayout = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.cancel = QPushButton(self.layoutWidget)
        self.cancel.setObjectName(u"cancel")
        font1 = QFont()
        font1.setFamily(u"Bahnschrift")
        font1.setPointSize(11)
        self.cancel.setFont(font1)

        self.horizontalLayout.addWidget(self.cancel)

        self.Determine = QPushButton(self.layoutWidget)
        self.Determine.setObjectName(u"Determine")
        self.Determine.setFont(font1)

        self.horizontalLayout.addWidget(self.Determine)

        SettingsWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(SettingsWindow)

        QMetaObject.connectSlotsByName(SettingsWindow)
    # setupUi

    def retranslateUi(self, SettingsWindow):
        SettingsWindow.setWindowTitle(QCoreApplication.translate("SettingsWindow", u"Settings", None))
        self.label.setText(QCoreApplication.translate("SettingsWindow", u"Language:", None))
        self.cancel.setText(QCoreApplication.translate("SettingsWindow", u"Cancel", None))
        self.Determine.setText(QCoreApplication.translate("SettingsWindow", u"Determine", None))
    # retranslateUi

