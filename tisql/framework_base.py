import sys
from PyQt5.QtWidgets import QWidget, QApplication, QMainWindow, QGridLayout, QAction, QVBoxLayout, QHBoxLayout
from PyQt5.QtWidgets import QTabWidget, QPushButton, QSplitter, QTableWidget, QTableWidgetItem, QTextEdit, QLabel
from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt
from database.dbfw import connect_to_base_and_execute
import sqlparse

    
def run(index, text1, text2, error_label, user, password, parse_button, table):
    # print(error_label.text())
    if index == 0:
        query = text1.toPlainText()
    else:
        query = text2.toPlainText()
    try:
        parsed = sqlparse.parse(query)[0]
        if parsed.get_type() == 'SELECT':
            if password == "d":
                error_label.setText('Вы не ввели пароль!')
            else:
                error_label.setText('Пока все хорошо..')
                connect_to_base_and_execute(query, error_label, user, password, parse_button)
                table.clear()
                try:
                    id_list = list(parsed.tokens[2].get_identifiers())
                    table.setColumnCount(len(id_list))  # Устанавливаем количество колонок, равное к-ву полей в запросе
                    # table.setRowCount(1)  # и одну строку в таблице
                    # Устанавливаем заголовки таблицы
                    headers_list = [x.get_alias() for x in id_list]
                    table.setHorizontalHeaderLabels(headers_list)
                except AttributeError:
                    error_label.setText('Что-то не так(')

                    tokens = parsed.tokens

        else:
            error_label.setText('В качестве запросов вы можете использовать только выборки "SELECT"!')
    except IndexError:
        error_label.setText('Пустой запрос?')


class Main(QMainWindow):

    def __init__(self):
        super().__init__()
        
        self.init_ui()

    def top_on_current_change(self, index):
        print("Top index", index)
        if index == 0:
            # print(type(self.ok_button))
            pass
        elif index == 1:
            pass

    def bottom_on_current_change(self, index):
        print("Bottom index", index)

    def init_ui(self):
        # textEdit = QTextEdit()
        
        central_widget = QWidget(self)                  # Создаём центральный виджет
        self.setCentralWidget(central_widget)
        self.ok_button = QPushButton("OK")

        self.cancel_button = QPushButton("Результат смотри тут")

        self.error_label = QLabel("Errors will be here")

        self.user_entry = QLineEdit("user5301")
        self.pass_entry = QLineEdit("d")
        self.pass_entry.setEchoMode(QLineEdit.PasswordEchoOnEdit)
        vbox = QVBoxLayout(central_widget)

        top = QTabWidget(central_widget)
        q = """select a.fn "Файл", a.dat "dat", a.kv "Валюта", a.skr "Сума файла", a.n "К-во пл", a.otm "otm", a.k_er "Ошибка", b.nb "Банк отправителя", a.sign_key "Ключ" from bars.zag_b a, bars.banks$base b where  a.DAT >= trunc(sysdate) and a.kf = b.mfo and a.otm <= 3 and to_char(a.dat + INTERVAL '20' MINUTE,'DD.MM.YYYY HH24:MI') <= to_char(sysdate,'DD.MM.YYYY HH24:MI') group by  fn, a.dat, a.kv, a.skr, a.n, a.otm, a.k_er, b.nb, a.kf, a.sign_key order by a.kf, a.dat"""
        print("q", q, "end q")
        self.text_edit1 = QTextEdit()
        self.text_edit1.setPlainText(q)
        # ok_button.clicked.connect(lambda: run(q, error_label, user_entry.text(), pass_entry.text(), cancel_button))
        # self.ok_button.clicked.connect(lambda: run(self.text_edit1.toPlainText(), self.error_label, self.user_entry.text(), self.pass_entry.text(), self.cancel_button))
        top.addTab(self.text_edit1, "Файлы, не сквитованые более 20 мин")
        self.text_edit2 = QTextEdit()
        top.addTab(self.text_edit2, "Tab2")
        top.currentChanged.connect(self.top_on_current_change)

        bottom = QTabWidget(central_widget)
        bottom.setTabPosition(QTabWidget.South)  # внизу

        # grid_layout = QGridLayout()             # Создаём QGridLayout
        # bottom.setLayout(grid_layout)
        table = QTableWidget(self)  # Создаём таблицу
        self.ok_button.clicked.connect(
            lambda: run(top.currentIndex(), self.text_edit1, self.text_edit2, self.error_label, self.user_entry.text(),
                        self.pass_entry.text(), self.cancel_button, table))
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
        hbox.addWidget(self.ok_button)
        hbox.addWidget(self.cancel_button)
        hbox.addWidget(self.user_entry)
        hbox.addWidget(self.pass_entry)
        hbox.addWidget(self.error_label)
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
