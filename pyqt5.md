## pyqt5

###  pyqt5总体使用步骤

1. 用designer_qt5.exe设计师设计页面
2. 用**pyuic -o test.py test.ui**转换为python代码
3. 在相应的目录新建一个新的py(main.py)文件,增添一下代码

```python
"""生成的py文件"""
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(688, 533)
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(200, 200, 75, 23))
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton.setText(_translate("Form", "PushButton"))
        
"""自己新建的main.py文件"""
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow

import test

if __name__ == '__main__':
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = test.Ui_Form()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

        
```



### 控件用法

- Buttons

  1. **Push Button**(点击触发时间)

     ```python
     """示例代码"""
     
     
     
     
     
     
     ```

     

