# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'test.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(584, 383)
        self.comboBox = QtWidgets.QComboBox(Form)
        self.comboBox.setGeometry(QtCore.QRect(220, 110, 69, 22))
        self.comboBox.setObjectName("comboBox")
        # 添加一个下拉框选项addItem()
        self.comboBox.addItems(['Java', 'C#', 'PHP'])  # 从列表中添加下拉框选项
        self.comboBox.currentIndexChanged.connect(self.get_combox)  # 当下拉选项的索引发生改变时发射该信号

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))


    def get_combox(self):
        # 获取索引为i的item的选项文本 itemText(i) i:列表的下标
        str = self.comboBox.currentText()  # 返回下拉框选中的内容
        print(str)