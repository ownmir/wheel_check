import sys
from PyQt5.QtWidgets import QWidget, QApplication, QMainWindow, QGridLayout, QAction, QVBoxLayout, QHBoxLayout
from PyQt5.QtWidgets import QTabWidget, QPushButton, QSplitter, QTableWidget, QTableWidgetItem, QTextEdit, QLabel
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt
from database.dbfw import connect_to_base_and_execute

    
class Main(QMainWindow):

    def __init__(self):
        super().__init__()
        
        self.init_ui()

    def top_on_current_change(self, index):
        print("Top index", index)

    def bottom_on_current_change(self, index):
        print("Bottom index", index)

    def init_ui(self):
        # textEdit = QTextEdit()
        
        central_widget = QWidget(self)                  # Создаём центральный виджет
        self.setCentralWidget(central_widget)
        okButton = QPushButton("OK")
        cancelButton = QPushButton("Cancel")
        error_label = QLabel("Errors will be here")
        vbox = QVBoxLayout(central_widget)

        top = QTabWidget(central_widget)
        text_edit1 = QTextEdit()
        tab1 = top.addTab(text_edit1, "Tab1")
        print('tab1', tab1, 'type(tab1)', type(tab1))
        text_edit2 = QTextEdit()
        tab2 = top.addTab(text_edit2, "Tab2")
        print('tab2', tab2, 'type(tab1)', type(tab2))
        top.currentChanged.connect(self.top_on_current_change)
        bottom = QTabWidget(central_widget)
        bottom.setTabPosition(QTabWidget.South)  # внизу

        # grid_layout = QGridLayout()             # Создаём QGridLayout
        # bottom.setLayout(grid_layout)
        table = QTableWidget(self)  # Создаём таблицу
        table.setColumnCount(3)  # Устанавливаем три колонки
        table.setRowCount(1)  # и одну строку в таблице

        # Устанавливаем заголовки таблицы
        table.setHorizontalHeaderLabels(["Header 1", "Header 2", "Header 3"])

        # Устанавливаем всплывающие подсказки на заголовки
        table.horizontalHeaderItem(0).setToolTip("Column 1 ")
        table.horizontalHeaderItem(1).setToolTip("Column 2 ")
        table.horizontalHeaderItem(2).setToolTip("Column 3 ")

        # Устанавливаем выравнивание на заголовки
        table.horizontalHeaderItem(0).setTextAlignment(Qt.AlignLeft)
        table.horizontalHeaderItem(1).setTextAlignment(Qt.AlignHCenter)
        table.horizontalHeaderItem(2).setTextAlignment(Qt.AlignRight)

        # заполняем первую строку
        table.setItem(0, 0, QTableWidgetItem("Text in column 1"))
        table.setItem(0, 1, QTableWidgetItem("Text in column 2"))
        table.setItem(0, 2, QTableWidgetItem("Text in column 3"))

        # делаем ресайз колонок по содержимому
        table.resizeColumnsToContents()
        bottom.addTab(table, "Result")
        messages_text_edit = QTextEdit()
        bottom.addTab(messages_text_edit, "Messages")
        bottom.currentChanged.connect(self.bottom_on_current_change)
        # grid_layout.addWidget(bottom, 0, 0)  # Добавляем таблицу в сетку

        splitter_vertical = QSplitter(Qt.Vertical)
        splitter_vertical.addWidget(top)
        splitter_vertical.addWidget(bottom)

        vbox.addWidget(splitter_vertical)
        hbox = QHBoxLayout(central_widget)
        hbox.addWidget(okButton)
        hbox.addWidget(cancelButton)
        hbox.addWidget(error_label)
        hbox.addStretch(1)
        vbox.addLayout(hbox)
        central_widget.setLayout(vbox)

        
        # QAction является абстракцией для действий, совершенных из меню, панели инструментов, или комбинаций клавиш. 
        exitAction = QAction(QIcon('exit.png'), '&Exit', self)  # В этих трех строках, мы создаем действие с соответствующей иконкой.
        exitAction.setShortcut('Ctrl+Q')  # Кроме того, для этого действия определяется комбинация клавиш.
        exitAction.setStatusTip('Exit application')  # создает подсказку, которая показывается в строке состояния, когда вы наведёте указатель мыши на пункт меню.
        # Когда мы выбираем именно это действие, срабатывает сигнал.
        exitAction.triggered.connect(self.close)  # Сигнал подключен к методу close(). Это завершает приложение.

        # Чтобы получить строку состояния, мы вызываем метод statusBar() класса QtGui.QMainWindow.
        # Первый вызов метода создает строку состояния.
        # Последующие вызовы возвращают объект статусбара.
        # showMessage() отображает сообщение в строке состояния.
        self.statusBar().showMessage('Ready')

        menubar = self.menuBar()  # Метод menuBar() создает строку меню.
        fileMenu = menubar.addMenu('&File')  # Мы создаем меню файла
        fileMenu.addAction(exitAction)  # и добавляем к нему действие выхода.

        toolbar = self.addToolBar('Exit')
        toolbar.addAction(exitAction)

        self.setGeometry(300, 100, 650, 550)
        self.setWindowTitle('Like silq')
##        self.setWindowIcon(QIcon('cfg.ico'))
        self.show()

        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = Main()
    sys.exit(app.exec_())
