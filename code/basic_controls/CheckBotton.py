# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'test.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


"""
setCheckanle():设置按钮是否已经被选中，可以改变单选按钮的选中状态，如果设置为True则表示单选按钮将保持以点击和释放状态
isChecked():返回单选按钮的状态，返回值True或False
setText():设置单选按钮显示的文本
text(): 返回单选按钮显示的文本
"""

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 300)
        self.checkBox = QtWidgets.QCheckBox(Form)
        self.checkBox.setGeometry(QtCore.QRect(140, 120, 71, 16))
        self.checkBox.setObjectName("checkBox")
        self.checkBox.setChecked(True)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.checkBox.setText(_translate("Form", "CheckBox"))
