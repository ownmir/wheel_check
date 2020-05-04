from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, qApp
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap, QPalette, QBrush
import sys


def paint(pic):
    pixmap = QPixmap(pic)
    # pixmap = QPixmap("sunflower1096.png")
    palette = window.palette()
    palette.setBrush(QPalette.Normal, QPalette.Window, QBrush(pixmap))
    palette.setBrush(QPalette.Inactive, QPalette.Window, QBrush(pixmap))
    window.setPalette(palette)
    window.setMask(pixmap.mask())
    # pic_b.clicked.connect(lambda: paint(pic))
    set_b.clicked.connect(lambda: set_pic(pic))
    print("Push paint; pic:", pic)
    #window.repaint()


def set_pic(pic):
    # 'bank720.png' 'sunflower1096.png' 'rf.png'
    if pic == 'bank720.png':
        pic = 'rf.png'
    elif pic == 'rf.png':
        pic = 'sunflower1096.png'
    elif pic == 'sunflower1096.png':
        pic = 'bank720.png'
    else:
        pic = 'bank720.png'
    # pic_b.clicked.emit(pic)
    pic_b.clicked.connect(lambda: paint(pic))

    print("Push set_pic; pic:", pic)


print("Begin")
app = QApplication(sys.argv)
window = QWidget()
window.setWindowFlags(Qt.Window | Qt.FramelessWindowHint)
# window.setAttribute(Qt.WA_TranslucentBackground)
window.resize(1096, 1096)
# window.resize(1920, 1080)
# pixmap = QPixmap("cloud.png")
pic = 'bank720.png'
pic_b = QPushButton("Paint picture", window)
pic_b.setFixedSize(100, 30)
pic_b.move(400, 435)
pic_b.clicked.connect(lambda : paint(pic))
set_b = QPushButton("Set picture", window)
set_b.setFixedSize(100, 30)
set_b.move(500, 435)
set_b.clicked.connect(lambda : set_pic(pic))

b = QPushButton("Close", window)
b.setFixedSize(100, 30)
b.move(280, 435)
# paint(pic)
b.clicked.connect(qApp.quit)
print("End")
window.show()
sys.exit(app.exec_())
