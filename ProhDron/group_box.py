from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, qApp, QRadioButton, QGroupBox, QHBoxLayout, QVBoxLayout
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap, QPalette, QBrush
import sys

print("Begin")
app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle('QGroupBox')
window.resize(200, 80)
main_box = QVBoxLayout()
radio1 = QRadioButton("&Да")
radio2 = QRadioButton("&Нет")
box = QGroupBox("&Вы знаете язык Python?")  # Объект группы
hbox = QHBoxLayout()  # Контейнер для группы
hbox.addWidget(radio1)  # Добавляем компоненты
hbox.addWidget(radio2)
box.setLayout(hbox)  # Передаем ссылку на контейнер
main_box.addWidget(box)  # Добавляем группу в главный контейнер
window.setLayout(main_box)  # Передаем ссылку на главный контейнер в окно
radio1.setChecked(True)  # Выбираем первый переключатель
print("box.title()", box.title(), "\nbox.alignment()")
print(box.alignment())
print("End")
window.show()
sys.exit(app.exec_())
