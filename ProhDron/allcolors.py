from PySide2.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout, QFormLayout, QGridLayout
# from PySide2.QtCore import Qt
from PySide2.QtGui import QPixmap, QPalette, QBrush, QColor
import sys

print("Begin")
app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle('Цвета')
# window.resize(300, 150)
window.resize(1920, 1080)
colors_list = QColor.colorNames()  # Список имен цветов
grid = QGridLayout()
window.setLayout(grid)
positions = [(i,j) for i in range(19) for j in range(8)]
# zip(*iters) - Итератор, возвращающий кортежи, состоящие из соответствующих элементов аргументов-последовательностей.
for position, name in zip(positions, colors_list):
    print("position", position, "name", name, "css", "background-color: {0}".format(name))
    button = QPushButton(name)
    button.setStyleSheet("background-color: {0}".format(name))
    # Если значения параметров, которые планируется передать в функцию, содержится в кортеже или списке, то перед
    # объектом следует указать символ * ( ПрохДрон стр 216 )
    grid.addWidget(button, *position)
print("End")
window.show()
sys.exit(app.exec_())
