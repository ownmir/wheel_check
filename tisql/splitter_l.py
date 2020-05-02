import sys
from PyQt5.QtWidgets import (QWidget, QVBoxLayout, QFrame, QSplitter, QStyleFactory, QApplication, QLabel)
from PyQt5.QtCore import Qt


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        splitter = QSplitter(Qt.Vertical)
        label1 = QLabel("Content of companent 1")
        label2 = QLabel("Content of companent 2")
        label3 = QLabel("Content of companent 3")
        label1.setFrameStyle(QFrame.Box | QFrame.Plain)
        label2.setFrameStyle(QFrame.Box | QFrame.Plain)
        label3.setFrameStyle(QFrame.Box | QFrame.Plain)

        splitter.addWidget(label1)
        # splitter.addWidget(label2)
        vbox = QVBoxLayout(self)


        splitter_h = QSplitter(Qt.Horizontal)

        splitter_h.addWidget(label2)
        splitter_h.addWidget(label3)
        splitter.addWidget(splitter_h)
        vbox.addWidget(splitter)

        self.setLayout(vbox)

        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('QSplitter')
        self.show()


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
