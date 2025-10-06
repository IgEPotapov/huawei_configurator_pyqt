from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import QtCore, QtGui


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(351, 202)
        MainWindow.setContextMenuPolicy(QtCore.Qt)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("C:/Python Projects/HellowWorld/huawei.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.btn1_rtn905 = QtWidgets.QPushButton(self.centralwidget)
        self.btn1_rtn905.setGeometry(QtCore.QRect(100, 50, 151, 31))
        self.btn1_rtn905.setObjectName("btn1_rtn905")
        self.btn2_rtn380ax = QtWidgets.QPushButton(self.centralwidget)
        self.btn2_rtn380ax.setGeometry(QtCore.QRect(100, 90, 151, 31))
        self.btn2_rtn380ax.setObjectName("btn2_rtn380ax")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 160, 351, 31))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(0, 20, 351, 20))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(15)
        font.setItalic(False)
        font.setKerning(True)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setWordWrap(False)
        self.label_2.setObjectName("label_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Huawei RTN Configurator"))
        self.btn1_rtn905.setText(_translate("MainWindow", "RTN 905"))
        self.btn2_rtn380ax.setText(_translate("MainWindow", "RTN 380AX"))
        self.label.setText(_translate("MainWindow", "To exit the program, press ESC"))
        self.label_2.setText(_translate("MainWindow", "Select NE type"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
