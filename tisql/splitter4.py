import sys
from PyQt5.QtWidgets import (QWidget, QHBoxLayout, QVBoxLayout, QFrame, QGridLayout,
    QSplitter, QStyleFactory, QApplication)
from PyQt5.QtCore import Qt
from PyQt5 import QtGui


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):

        # hbox = QHBoxLayout(self)
        grid = QGridLayout()

        topleft = QFrame(self)
        topleft.setFrameShape(QFrame.StyledPanel)

        topright = QFrame(self)
        topright.setFrameShape(QFrame.StyledPanel)

        bottom = QFrame(self)
        bottom.setFrameShape(QFrame.StyledPanel)

        # splitter1 = QSplitter(Qt.Horizontal)
        # splitter1.addWidget(topleft)
        # splitter1.addWidget(topright)
        #
        # splitter2 = QSplitter(Qt.Vertical)
        # splitter2.addWidget(splitter1)
        # splitter2.addWidget(bottom)

        grid.addWidget(topleft, 0, 0)
        # hbox.addWidget(topleft)
        grid.addWidget(topright, 0, 1)
        # hbox.addWidget(topright)
        grid.addWidget(bottom, 1, 0)
        # vbox = QVBoxLayout(self)
        #vbox.addWidget(bottom)
        # hbox.addLayout(vbox)

        self.setLayout(grid)

        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('QSplitter')
        self.show()


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
