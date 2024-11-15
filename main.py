#создай тут фоторедактор Easy Editor!
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QListWidget, QApplication,  QHBoxLayout, QWidget, QPushButton, QLabel, QVBoxLayout, QFileDialog
from PyQt5 import QtGui, QtCore
from PyQt5.QtGui import QPixmap
import os
from PIL import Image
from PIL import ImageFilter
from PIL import ImageEnhance



app = QApplication([])

workdir = ""


def chooseWorkdir():
    global workdir
    workdir = QFileDialog.getExistingDirectory()

def filter(files, extensions):
    result = []
    for file in files:
        for extension in extensions:
            if file.endswith(extension):
                result.append(file)
    return result

    
    

def showFilenamesList():
    chooseWorkdir()
    extensions = [".jpg", ".jpeg", ".png", ".gif", ".bmp"]
    files = os.listdir(workdir)
    res = filter(files, extensions)
    pictures.clear()
    for r in res:
        pictures.addItem(r)


class ImageProcessor():
    def __init__(self):
        self.image = None
        self.name = None
        self.save = "Img/"

    def LoadImage(self, filename):
        self.name = filename
        file_path = os.path.join(workdir, filename)
        self.image = Image.open(file_path)

    def showImage(self, path):
        text.hide()
        pixmapimage = QPixmap(path)
        w, h = text.width(), text.height()
        pixmapimage = pixmapimage.scaled(w, h, Qt.KeepAspectRatio)
        text.setPixmap(pixmapimage)
        text.show()

    def do_bw(self):
        self.image = self.image.convert("L")
        self.saveImage()
        image_path = os.path.join(workdir, self.save, self.name)
        self.showImage(image_path)
        
    def do_left(self):
        self.image = self.image.transpose(Image.ROTATE_90)
        self.saveImage()
        image_path = os.path.join(workdir, self.save, self.name)
        self.showImage(image_path)

    def do_flip(self):
        self.image = self.image.transpose(Image.FLIP_LEFT_RIGHT)
        self.saveImage()
        image_path = os.path.join(workdir, self.save, self.name)
        self.showImage(image_path)

    def do_countur(self):
        self.image = self.image.filter(ImageFilter.CONTOUR)
        self.saveImage()
        image_path = os.path.join(workdir, self.save, self.name)
        self.showImage(image_path)

    def do_emboss(self):
        self.image = self.image.filter(ImageFilter.EMBOSS)
        self.saveImage()
        image_path = os.path.join(workdir, self.save, self.name)
        self.showImage(image_path)

    def do_find_edges(self):
        self.image = self.image.filter(ImageFilter.FIND_EDGES)
        self.saveImage()
        image_path = os.path.join(workdir, self.save, self.name)
        self.showImage(image_path)

    def saveImage(self):
        path = os.path.join(workdir, self.save)
        if not(os.path.exists(path) or os.path.isdir(path)):
            os.mkdir(path)
        image_path = os.path.join(path, self.name)
        self.image.save(image_path)

workimage = ImageProcessor()

def showChosenImage():
    if pictures.currentRow() >= 0:
        filename = pictures.currentItem().text()
        workimage.LoadImage(filename)
        image_path = os.path.join(workdir, workimage.name)
        workimage.showImage(image_path)




    








main_win = QWidget()
main_win.show()

main_win.setWindowTitle("EasyEditor")
main_win.resize(700, 400)

btn1 = QPushButton("Папка")
pictures = QListWidget()

btnpc1 = QPushButton("Лево")
btnpc2 = QPushButton("Глина")
btnpc3 = QPushButton("Зеркало")
btnpc4 = QPushButton("Контур")
btnpc5 = QPushButton("Ч\Б")
btnpc6 = QPushButton("Края")

text = QLabel("Картинка")

v_line_left_column = QVBoxLayout()
v_line_right_column = QVBoxLayout()
h_line_buttons_layout = QHBoxLayout()
h_line_main = QHBoxLayout()

v_line_left_column.addWidget(btn1)
v_line_left_column.addWidget(pictures)

h_line_buttons_layout.addWidget(btnpc1)
h_line_buttons_layout.addWidget(btnpc2)
h_line_buttons_layout.addWidget(btnpc3)
h_line_buttons_layout.addWidget(btnpc4)
h_line_buttons_layout.addWidget(btnpc5)
h_line_buttons_layout.addWidget(btnpc6)

v_line_right_column.addWidget(text)
v_line_right_column.addLayout(h_line_buttons_layout)

h_line_main.addLayout(v_line_left_column, 20)
h_line_main.addLayout(v_line_right_column, 80)


main_win.setLayout(h_line_main)






btn1.clicked.connect(showFilenamesList)
btnpc5.clicked.connect(workimage.do_bw)
btnpc1.clicked.connect(workimage.do_left)
btnpc3.clicked.connect(workimage.do_flip)
btnpc4.clicked.connect(workimage.do_countur)
btnpc2.clicked.connect(workimage.do_emboss)
btnpc6.clicked.connect(workimage.do_find_edges)

pictures.currentRowChanged.connect(showChosenImage)









app.exec_()























