from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import (QMainWindow, QTextEdit,
                             QAction, QFileDialog, QApplication)
import sys
import os
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


def upload_main_image():
    #img = Image.open(ShowPath(ui))
    #arr = np.asarray(img, dtype='uint8')

    #k = np.array([[[0.2989, 0.587, 0.114]]])
    #sums = np.round(arr/1.1111).astype(np.uint8)

    #print(Image.fromarray(sums).save('1.jpg'), os.getcwd()+"1.jpg")
    # ui.label.setPixmap(QtGui.QPixmap(os.getcwd()+"\\1.jpg"))

    ui.mainPic.setPixmap(QtGui.QPixmap(ShowPath(ui)))


def upload_image():
    ui.keyPic.setPixmap(QtGui.QPixmap(ShowPath(ui)))


def ShowPath(self):
    return QFileDialog.getOpenFileName()[0]


ui.chooseButton.clicked.connect(upload_main_image)
ui.chooseButton_2.clicked.connect(upload_image)


# Run main loop
sys.exit(app.exec_())
