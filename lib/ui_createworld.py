

# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'createworld.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_creaworldw(object):
    def setupUi(self, creaworldw):
        if not creaworldw.objectName():
            creaworldw.setObjectName(u"creaworldw")
        creaworldw.resize(391, 154)
        self.centralwidget = QWidget(creaworldw)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 10, 361, 41))
        font = QFont()
        font.setFamily(u"Bahnschrift")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.worldnamel = QLineEdit(self.centralwidget)
        self.worldnamel.setObjectName(u"worldnamel")
        self.worldnamel.setGeometry(QRect(10, 60, 371, 31))
        font1 = QFont()
        font1.setPointSize(10)
        self.worldnamel.setFont(font1)
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(290, 110, 91, 31))
        font2 = QFont()
        font2.setFamily(u"Bahnschrift")
        font2.setPointSize(10)
        self.pushButton.setFont(font2)
        self.pushButton_2 = QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(190, 110, 91, 31))
        self.pushButton_2.setFont(font2)
        creaworldw.setCentralWidget(self.centralwidget)

        self.retranslateUi(creaworldw)

        QMetaObject.connectSlotsByName(creaworldw)
    # setupUi

    def retranslateUi(self, creaworldw):
        creaworldw.setWindowTitle(QCoreApplication.translate("creaworldw", u"Create World", None))
        self.label.setText(QCoreApplication.translate("creaworldw", u"World name:", None))
        self.pushButton.setText(QCoreApplication.translate("creaworldw", u"Determine", None))
        self.pushButton_2.setText(QCoreApplication.translate("creaworldw", u"Cancel", None))
    # retranslateUi

class Test():
    def __init__(self) -> None:
        self._666 = "郑昊林"