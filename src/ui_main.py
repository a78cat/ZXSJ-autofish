# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_main.ui'
##
## Created by: Qt User Interface Compiler version 6.6.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QMetaObject)
from PySide6.QtWidgets import (QGroupBox, QHBoxLayout, QLabel,
                               QLineEdit, QPushButton, QVBoxLayout)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(236, 136)
        self.verticalLayout_2 = QVBoxLayout(Form)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.groupBox = QGroupBox(Form)
        self.groupBox.setObjectName(u"groupBox")
        self.verticalLayout = QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_presstime = QLabel(self.groupBox)
        self.label_presstime.setObjectName(u"label_presstime")

        self.horizontalLayout.addWidget(self.label_presstime)

        self.lineEdit_presstime = QLineEdit(self.groupBox)
        self.lineEdit_presstime.setObjectName(u"lineEdit_presstime")

        self.horizontalLayout.addWidget(self.lineEdit_presstime)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_releasetime = QLabel(self.groupBox)
        self.label_releasetime.setObjectName(u"label_releasetime")

        self.horizontalLayout_2.addWidget(self.label_releasetime)

        self.lineEdit_releasetime = QLineEdit(self.groupBox)
        self.lineEdit_releasetime.setObjectName(u"lineEdit_releasetime")

        self.horizontalLayout_2.addWidget(self.lineEdit_releasetime)


        self.verticalLayout.addLayout(self.horizontalLayout_2)


        self.verticalLayout_2.addWidget(self.groupBox)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.pushButton_start = QPushButton(Form)
        self.pushButton_start.setObjectName(u"pushButton_start")

        self.horizontalLayout_3.addWidget(self.pushButton_start)

        self.pushButton_stop = QPushButton(Form)
        self.pushButton_stop.setObjectName(u"pushButton_stop")

        self.horizontalLayout_3.addWidget(self.pushButton_stop)


        self.verticalLayout_2.addLayout(self.horizontalLayout_3)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.groupBox.setTitle(QCoreApplication.translate("Form", u"\u65f6\u95f4\u8c03\u6574", None))
        self.label_presstime.setText(QCoreApplication.translate("Form", u"\u6309\u4e0b\u65f6\u95f4", None))
        self.lineEdit_presstime.setText(QCoreApplication.translate("Form", u"0.5", None))
        self.label_releasetime.setText(QCoreApplication.translate("Form", u"\u677e\u5f00\u65f6\u95f4", None))
        self.lineEdit_releasetime.setInputMask("")
        self.lineEdit_releasetime.setText(QCoreApplication.translate("Form", u"0.3", None))
        self.pushButton_start.setText(QCoreApplication.translate("Form", u"\u5f00\u59cb", None))
        self.pushButton_stop.setText(QCoreApplication.translate("Form", u"\u505c\u6b62", None))
    # retranslateUi

