from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(439, 432)
        MainWindow.setAcceptDrops(True)
        MainWindow.setStyleSheet("QMainWindow{\n"
                                 "background-color: white;\n"
                                 "}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.chooseButton = QtWidgets.QPushButton(self.centralwidget)
        self.chooseButton.setGeometry(QtCore.QRect(10, 320, 151, 71))
        self.chooseButton.setObjectName("chooseButton")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 431, 291))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(
            "../../../../Download/Group 18 (1).jpg"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.secondButton = QtWidgets.QPushButton(self.centralwidget)
        self.secondButton.setGeometry(QtCore.QRect(180, 320, 231, 81))
        self.secondButton.setObjectName("secondButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.chooseButton.setText(_translate("MainWindow", "Выбрать файл"))
        self.secondButton.setText(_translate("MainWindow", "Второй"))
