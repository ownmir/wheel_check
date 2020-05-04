from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, qApp, QLineEdit, QTextEdit, QHBoxLayout, QFormLayout
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap, QPalette, QBrush
import sys

print("Begin")
app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle('QFormLayout')
window.resize(300, 150)
# window.resize(1920, 1080)
lineEdit = QLineEdit()
textEdit = QTextEdit()
b1 = QPushButton("О&тправить")
b2 = QPushButton("О&чистить")
hbox = QHBoxLayout()
hbox.addWidget(b1)
hbox.addWidget(b2)
form = QFormLayout()
form.addRow("&Название:", lineEdit)
form.addRow("&Описание:", textEdit)
form.addRow(hbox)
window.setLayout(form)
print("End")
window.show()
sys.exit(app.exec_())
