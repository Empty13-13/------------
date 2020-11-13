# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.NonModal)
        MainWindow.resize(1054, 699)
        MainWindow.setFocusPolicy(QtCore.Qt.NoFocus)
        MainWindow.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        MainWindow.setAcceptDrops(True)
        MainWindow.setWindowOpacity(1.0)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet("QMainWindow{\n"
"background-color: white;\n"
"border-radius: 40px;\n"
"}\n"
"")
        MainWindow.setInputMethodHints(QtCore.Qt.ImhNone)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.chooseButton = QtWidgets.QPushButton(self.centralwidget)
        self.chooseButton.setGeometry(QtCore.QRect(460, 360, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.chooseButton.setFont(font)
        self.chooseButton.setMouseTracking(False)
        self.chooseButton.setTabletTracking(False)
        self.chooseButton.setAcceptDrops(True)
        self.chooseButton.setObjectName("chooseButton")
        self.mainPic = QtWidgets.QLabel(self.centralwidget)
        self.mainPic.setGeometry(QtCore.QRect(370, 0, 311, 311))
        self.mainPic.setText("")
        self.mainPic.setPixmap(QtGui.QPixmap("../../../../Download/Group 18 (1).jpg"))
        self.mainPic.setScaledContents(True)
        self.mainPic.setObjectName("mainPic")
        self.keyPic = QtWidgets.QLabel(self.centralwidget)
        self.keyPic.setGeometry(QtCore.QRect(10, 0, 311, 311))
        self.keyPic.setText("")
        self.keyPic.setPixmap(QtGui.QPixmap("key.png"))
        self.keyPic.setScaledContents(True)
        self.keyPic.setObjectName("keyPic")
        self.dwmPic = QtWidgets.QLabel(self.centralwidget)
        self.dwmPic.setGeometry(QtCore.QRect(730, 0, 311, 311))
        self.dwmPic.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.dwmPic.setAcceptDrops(False)
        self.dwmPic.setText("")
        self.dwmPic.setPixmap(QtGui.QPixmap("../../../../Download/Group 18 (1).jpg"))
        self.dwmPic.setScaledContents(True)
        self.dwmPic.setObjectName("dwmPic")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(400, 310, 261, 41))
        self.label_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_2.setAutoFillBackground(False)
        self.label_2.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";")
        self.label_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label_2.setLineWidth(1)
        self.label_2.setMidLineWidth(0)
        self.label_2.setScaledContents(False)
        self.label_2.setWordWrap(False)
        self.label_2.setOpenExternalLinks(False)
        self.label_2.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(870, 310, 51, 41))
        self.label_3.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_3.setAutoFillBackground(False)
        self.label_3.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";")
        self.label_3.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_3.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label_3.setLineWidth(1)
        self.label_3.setMidLineWidth(0)
        self.label_3.setScaledContents(False)
        self.label_3.setWordWrap(False)
        self.label_3.setOpenExternalLinks(False)
        self.label_3.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse)
        self.label_3.setObjectName("label_3")
        self.label_1 = QtWidgets.QLabel(self.centralwidget)
        self.label_1.setGeometry(QtCore.QRect(120, 310, 51, 41))
        self.label_1.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_1.setAutoFillBackground(False)
        self.label_1.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";")
        self.label_1.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_1.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label_1.setLineWidth(1)
        self.label_1.setMidLineWidth(0)
        self.label_1.setScaledContents(False)
        self.label_1.setWordWrap(False)
        self.label_1.setOpenExternalLinks(False)
        self.label_1.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse)
        self.label_1.setObjectName("label_1")
        self.chooseButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.chooseButton_2.setGeometry(QtCore.QRect(190, 360, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.chooseButton_2.setFont(font)
        self.chooseButton_2.setMouseTracking(False)
        self.chooseButton_2.setTabletTracking(False)
        self.chooseButton_2.setAcceptDrops(True)
        self.chooseButton_2.setObjectName("chooseButton_2")
        self.generateButton = QtWidgets.QPushButton(self.centralwidget)
        self.generateButton.setGeometry(QtCore.QRect(10, 360, 161, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.generateButton.setFont(font)
        self.generateButton.setMouseTracking(False)
        self.generateButton.setTabletTracking(False)
        self.generateButton.setAcceptDrops(True)
        self.generateButton.setObjectName("generateButton")
        self.chooseButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.chooseButton_3.setGeometry(QtCore.QRect(830, 360, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.chooseButton_3.setFont(font)
        self.chooseButton_3.setMouseTracking(False)
        self.chooseButton_3.setTabletTracking(False)
        self.chooseButton_3.setAcceptDrops(True)
        self.chooseButton_3.setObjectName("chooseButton_3")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(-20, 480, 1101, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(400, 490, 261, 41))
        self.label_4.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_4.setAutoFillBackground(False)
        self.label_4.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";")
        self.label_4.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_4.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label_4.setLineWidth(1)
        self.label_4.setMidLineWidth(0)
        self.label_4.setScaledContents(False)
        self.label_4.setWordWrap(False)
        self.label_4.setOpenExternalLinks(False)
        self.label_4.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse)
        self.label_4.setObjectName("label_4")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(10, 540, 291, 111))
        self.groupBox.setObjectName("groupBox")
        self.radioButton = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton.setGeometry(QtCore.QRect(10, 30, 95, 20))
        self.radioButton.setChecked(True)
        self.radioButton.setObjectName("radioButton")
        self.radioButton_2 = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton_2.setGeometry(QtCore.QRect(160, 30, 95, 20))
        self.radioButton_2.setObjectName("radioButton_2")
        self.radioButton_3 = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton_3.setGeometry(QtCore.QRect(10, 80, 101, 20))
        self.radioButton_3.setObjectName("radioButton_3")
        self.radioButton_4 = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton_4.setGeometry(QtCore.QRect(160, 80, 101, 20))
        self.radioButton_4.setObjectName("radioButton_4")
        self.startBut = QtWidgets.QPushButton(self.centralwidget)
        self.startBut.setGeometry(QtCore.QRect(410, 430, 221, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.startBut.setFont(font)
        self.startBut.setMouseTracking(False)
        self.startBut.setTabletTracking(False)
        self.startBut.setAcceptDrops(True)
        self.startBut.setStyleSheet("QPushButton{\n"
"background-color: black;\n"
"color: white;\n"
"}\n"
"\n"
"QPushButton::hover{\n"
"background-color: gray;\n"
"color: white;\n"
"}")
        self.startBut.setObjectName("startBut")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Главная"))
        self.chooseButton.setText(_translate("MainWindow", "Выбрать"))
        self.label_2.setText(_translate("MainWindow", "Оригинальное изображение"))
        self.label_3.setText(_translate("MainWindow", "ЦВЗ"))
        self.label_1.setText(_translate("MainWindow", "Ключ"))
        self.chooseButton_2.setText(_translate("MainWindow", "Выбрать"))
        self.generateButton.setText(_translate("MainWindow", "Сгенерировать"))
        self.chooseButton_3.setText(_translate("MainWindow", "Выбрать"))
        self.label_4.setText(_translate("MainWindow", "Функции вытаскивания ЦВЗ"))
        self.groupBox.setTitle(_translate("MainWindow", "Изображение повернуто (по часовой стрелке)"))
        self.radioButton.setText(_translate("MainWindow", "0 Градусов"))
        self.radioButton_2.setText(_translate("MainWindow", "90 Градусов"))
        self.radioButton_3.setText(_translate("MainWindow", "180 Градусов"))
        self.radioButton_4.setText(_translate("MainWindow", "270 градусов"))
        self.startBut.setText(_translate("MainWindow", "Сделать водяной знак"))
