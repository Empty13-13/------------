from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import (QMainWindow, QTextEdit,
                             QAction, QFileDialog, QApplication)
import sys
import os
import functions
import math
import numpy as np
from ui import Ui_MainWindow
from PIL import Image


# Create application
app = QtWidgets.QApplication(sys.argv)

# Create form and init UI
MainWindow = QtWidgets.QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(MainWindow)
MainWindow.show()

# Hook logic
mainArr = []
keyArr = []
wbmArr = []


# Основное изображение
def upload_main_image():
    global mainArr
    pathImg = ShowPath(ui)
    img = Image.open(pathImg)
    mainArr = np.asarray(img, dtype='uint8')
    # print(mainArr)

    # k = np.array([[[0.2989, 0.587, 0.114]]])
    # sums = np.round(arr/1.1111).astype(np.uint8)
    # ui.label.setPixmap(QtGui.QPixmap(os.getcwd()+"\\1.jpg"))

    ui.mainPic.setPixmap(QtGui.QPixmap(pathImg))


def startGenerateResult():
    global mainArr, keyArr, wbmArr
    q = np.array([[[1.1, 1.1, 1.1]]])
    functions.generateWithDWM(mainArr, wbmArr, keyArr, q)


# Ключ
def upload_key_image(pathImg=""):
    global keyArr
    if not pathImg:
        pathImg = ShowPath(ui)
    img = Image.open(pathImg)
    keyArr = np.asarray(img, dtype='uint8')

    ui.keyPic.setPixmap(QtGui.QPixmap(pathImg))


def generateAndUpload():
    Image.fromarray(np.array(functions.generateKey())).save(
        'keyImg.jpg')

    upload_key_image(os.getcwd()+"\\keyImg.jpg")


# ЦВЗ
def upload_dwm_image():
    global wbmArr
    pathImg = ShowPath(ui)
    img = Image.open(pathImg)
    wbmArr = np.asarray(img, dtype='uint8')

    ui.dwmPic.setPixmap(QtGui.QPixmap(pathImg))


# Доп функции
def ShowPath(self):
    return QFileDialog.getOpenFileName(ui.centralwidget, "Выбор изображения", "", "*.png *.jpg *.bmp", "")[0]


ui.chooseButton.clicked.connect(upload_main_image)
ui.chooseButton_2.clicked.connect(upload_key_image)
ui.chooseButton_3.clicked.connect(upload_dwm_image)
ui.generateButton.clicked.connect(generateAndUpload)
ui.startBut.clicked.connect(startGenerateResult)


# Run main loop
sys.exit(app.exec_())
