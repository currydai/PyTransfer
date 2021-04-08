from PyQt5 import QtGui,QtWidgets,QtCore
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from modules.Login import Ui_Login_Form
from modules.main_window import Ui_main_window
import sys


###登录界面
class Login(QMainWindow, Ui_Login_Form):
    def __init__(self, parent=None):
        super(Login, self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle("Login")  # 设置标题
        self.changeStyle('Fusion')  # 启动时使用Fusion风格
        self.setWindowIcon(QtGui.QIcon(r'.\pictures\界面图标.png'))
        #self.setWindowFlag(QtCore.Qt.FramelessWindowHint)  # 隐藏边框
        self.pushButton_login.clicked.connect(self.mainwindow)
    def changeStyle(self, styleName):
        QApplication.setStyle(QStyleFactory.create(styleName))

    def mainwindow(self):
        username=self.lineEdit_username.text()
        password=self.lineEdit_password.text()

        if(username=="currydai" and password=="currydai"):
            self.main=MainWindow()
            self.main.show()
            self.close()
        else:
            self.label_login_error.setText("Username or Password is wrong!")

###主界面
class MainWindow(QMainWindow, Ui_main_window):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle("MainWindow")  # 设置标题
        self.changeStyle('Fusion')  # 启动时使用Fusion风格
        self.setWindowIcon(QtGui.QIcon(r'.\pictures\界面图标.png'))
        # self.setWindowFlag(QtCore.Qt.FramelessWindowHint)  # 隐藏边框

    def changeStyle(self, styleName):
        QApplication.setStyle(QStyleFactory.create(styleName))

if __name__=="__main__":
    # 固定的，PyQt5程序都需要QApplication对象。sys.argv是命令行参数列表，确保程序可以双击运行
    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)
    app = QApplication(sys.argv)
    # 初始化
    myWin = Login()
    # 将窗口控件显示在屏幕上
    myWin.show()
    # 程序运行，sys.exit方法确保程序完整退出。
    sys.exit(app.exec_())