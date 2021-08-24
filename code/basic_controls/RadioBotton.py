import sys
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QMessageBox, QRadioButton, QButtonGroup

app = QtWidgets.QApplication(sys.argv)
windows = QtWidgets.QWidget()
windows.setGeometry(QtCore.QRect(100, 100, 500, 500))

btn1 = QRadioButton("男", windows)
btn2 = QRadioButton("女", windows)
btn1.setChecked(True)  # 默认选中按钮
# 点击事件，信号与槽函数绑可以参考:https://www.jb51.net/article/181602.htm
btn1.toggled.connect(lambda isChecked: print(isChecked))
btn2.toggled.connect(lambda isChecked: print(isChecked))

btn3 = QRadioButton("是", windows)
btn4 = QRadioButton("否", windows)

btn1.move(250, 100)
btn2.move(250, 120)
btn3.move(200, 100)
btn4.move(200, 120)
# 创建按键组
QBG1 = QButtonGroup()
QBG2 = QButtonGroup()
# 给按键分组
QBG1.addButton(btn1, 1)
QBG1.addButton(btn2, 2)
QBG2.addButton(btn3, 1)
QBG2.addButton(btn4, 2)

windows.show()
sys.exit(app.exec_())