# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mock_server.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(691, 498)
        Form.setToolTipDuration(1)
        Form.setStyleSheet("background-image: url(./6.png);")
        self.textEdit = QtWidgets.QTextEdit(Form)
        self.textEdit.setGeometry(QtCore.QRect(40, 100, 611, 281))
        self.textEdit.setStyleSheet("background-image: url(./2.png);")
        self.textEdit.setObjectName("textEdit")

        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(160, 30, 491, 20))
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")

        self.comboBox = QtWidgets.QComboBox(Form)
        self.comboBox.setGeometry(QtCore.QRect(40, 30, 91, 22))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("GET")
        self.comboBox.addItem("POST")
        self.comboBox.addItem("PULL")
        self.comboBox.addItem("DELETE")

        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(40, 400, 611, 81))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(20)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("background-image: url(./4.png);")
        self.pushButton.setObjectName("pushButton")

        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(250, 60, 251, 31))
        self.label.setObjectName("label")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "EasyMock"))
        self.textEdit.setToolTip(_translate("Form", "只支持json数据和html数据"))
        self.textEdit.setPlaceholderText(_translate("Form", "版本V1：只支持单接口访问\n支持：JSON_CONTENT OR HTML_CONTENT的返回信息\n默认IP：localhost\n默认端口：7777"))
        self.comboBox.setItemText(0, _translate("Form", "GET"))
        self.comboBox.setItemText(1, _translate("Form", "POST"))
        self.comboBox.setItemText(2, _translate("Form", "PULL"))
        self.comboBox.setItemText(3, _translate("Form", "DELETE"))
        self.pushButton.setText(_translate("Form", "启动Flask服务"))
        self.label.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:20pt; font-weight:600;\">ResponseContent</span></p></body></html>"))
