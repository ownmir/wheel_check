from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, qApp
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap, QPalette, QBrush
import sys

app = QApplication(sys.argv)
window = QWidget()
window.setWindowFlags(Qt.Window | Qt.FramelessWindowHint)
window.resize(1920, 1080)
pixmap = QPixmap("cloud.png")
palette = window.palette()
palette.setBrush(QPalette.Normal, QPalette.Window, QBrush(pixmap))
# palette.setBrush(QPalette.Inactive, QPalette.Window, QBrush(pixmap))
window.setPalette(palette)
window.setMask(pixmap.mask())
b = QPushButton("Close", window)
b.setFixedSize(150, 30)
# b.move(80, 135)
b.clicked.connect(qApp.quit)
window.show()
sys.exit(app.exec_())
