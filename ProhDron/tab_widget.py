from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, qApp, QTabWidget, QLabel, QHBoxLayout, QVBoxLayout
from PyQt5.QtCore import Qt
import sys


def on_current_change(index):
    print("index", index)


print("Begin")
app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle('QTabWidget')
window.resize(400, 200)
tab = QTabWidget()
tab.addTab(QLabel("Content 1"), "Tab &1")
tab.addTab(QLabel("Content 2"), "Tab &2")
tab.addTab(QLabel("Content 3"), "Tab &3")
tab.setCurrentIndex(0)
vbox = QVBoxLayout()  #
vbox.addWidget(tab)  # Добавляем компоненты
tab1 = QTabWidget()
tab1.addTab(QLabel("1 Content 1"), "1 Tab &1")
tab1.addTab(QLabel("1 Content 2"), "1 Tab &2")
tab1.addTab(QLabel("1 Content 3"), "1 Tab &3")
tab1.setCurrentIndex(0)
tab1.setTabPosition(QTabWidget.South)  # внизу
tab1.setTabShape(QTabWidget.Triangular)
vbox.addWidget(tab1)
window.setLayout(vbox)  #
tab.currentChanged.connect(on_current_change)
print("tab.tabText(0)", tab.tabText(0))
print("tab.tabText(1)", tab.tabText(1))
print("tab.tabText(2)", tab.tabText(2), "\nbox.alignment()")
# print(box.alignment())
print("End")
window.show()
sys.exit(app.exec_())
