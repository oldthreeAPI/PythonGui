"""
version1:单接口版本
利用python的flask、pyqt5开发的简单服务器mock工具，可用于接口的简单的测试。
注意：不支持关联的接口测试
"""

import sys

import mock_server
from PyQt5.QtWidgets import QApplication, QMainWindow

if __name__ == '__main__':
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = mock_server.Ui_Form()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())



