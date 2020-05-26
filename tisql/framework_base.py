import sys
from PyQt5.QtWidgets import QWidget, QApplication, QMainWindow, QAction, QVBoxLayout, QHBoxLayout, QGroupBox
from PyQt5.QtWidgets import QTabWidget, QPushButton, QSplitter, QTableWidget, QTableWidgetItem, QTextEdit, QLabel
from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtGui import QIcon, QColor
from PyQt5.QtCore import Qt
from database.dbfw import connect_to_base_and_execute
import sqlparse
import cx_Oracle
import winsound


def run(index, text1, text2, text3, error_label, user, password, parse_button, table):
    """
    Run query text1 (2,3)
    :param index: index of tab
    :param text1: query 1
    :param text2: query 2
    :param text3: query 3
    :param error_label: number of records is returned by query or errors
    :param user: user
    :param password: password
    :param parse_button: will be result
    :param table: TableWidget
    """
    # print(error_label.text())
    if index == 0:
        print("index", index)
        query = text1.toPlainText()
    elif index == 1:
        print("index", index)
        query = text2.toPlainText()
    elif index == 2:
        print("index", index)
        query = text3.toPlainText()
    else:
        print("Else index", index)
        query = ""
        # print("text2.toPlainText()", query)
    try:
        parsed = sqlparse.parse(query)[0]
        if parsed.get_type() == 'SELECT':
            if password == "d":
                error_label.setText('Вы не ввели пароль!')
            else:
                error_label.setText('Пока все хорошо..')
                # connect_to_base_and_execute(query, error_label, user, password, parse_button)
                rows = connect_to_base_and_execute(query, error_label, user, password, parse_button, "''")
                if rows:
                    table.clear()
                    try:
                        id_list = list(parsed.tokens[2].get_identifiers())
                        table.setColumnCount(
                            len(id_list))  # Устанавливаем количество колонок, равное к-ву полей в запросе
                        # table.setRowCount(1)  # и одну строку в таблице
                        table.setRowCount(min(30, len(rows)))  # и количество строк в таблице
                        # Устанавливаем заголовки таблицы
                        headers_list = [x.get_alias() or x.get_name() for x in id_list]
                        table.setHorizontalHeaderLabels(headers_list)
                        for line, row in enumerate(rows):
                            # print("line", line)
                            for i, header in enumerate(headers_list):
                                # Устанавливаем всплывающие подсказки на заголовки
                                table.horizontalHeaderItem(i).setToolTip(header)
                                # table.horizontalHeaderItem(1).setToolTip("Column 2 ")select dk, name from dk
                                # Устанавливаем выравнивание на заголовки
                                table.horizontalHeaderItem(i).setTextAlignment(Qt.AlignLeft)
                                # print("row", row)
                                # print("row[i]", row[i])
                                # print("QTableWidgetItem(str(row[i]))", QTableWidgetItem(str(row[i])))
                                # заполняем строку
                                table.setItem(line, i, QTableWidgetItem(str(row[i])))
                        # делаем ресайз колонок по содержимому
                        table.resizeColumnsToContents()
                    except AttributeError:
                        error_label.setText('Что-то не так(')
                        tokens = parsed.tokens
                        columns = []
                        tables = []
                        is_from = False
                        for token in tokens:
                            # print("token", token, "ttype", token.ttype)
                            if token.ttype is sqlparse.tokens.Wildcard:
                                print("В таблицу выведутся все поля..")
                                error_label.setText('Выводим все поля')
                                columns.append("*")
                            if isinstance(token, sqlparse.sql.IdentifierList):
                                # print("IdentifierList found")
                                if is_from:
                                    for identifier in token.get_identifiers():
                                        tables.append(str(identifier))
                                    continue
                                for identifier in token.get_identifiers():
                                    columns.append(str(identifier))
                            if isinstance(token, sqlparse.sql.Identifier):
                                # print("Identifier found")
                                if is_from:
                                    tables.append(str(token))
                                    continue
                                columns.append(str(token))
                            if token.ttype is sqlparse.tokens.Keyword:  # from
                                # print("token.ttype is sqlparse.tokens.Keyword (# from)")
                                # print(columns)
                                is_from = True
                                continue
                            if str(token).lstrip().upper().startswith("WHERE"):
                                # print("token.ttype is sqlparse.tokens.Keyword (# where) .. breaking")
                                # print(columns)
                                # print(tables)
                                break
                        # print(tables)
                        if '*' in columns:
                            columns_list = []
                            for column, selected_table in enumerate(tables):
                                # print("selected_table", selected_table, "type(selected_table)", type(selected_table))
                                query_fields_rows_base = """SELECT column_name \
                                    FROM ALL_TAB_COLUMNS \
                                    WHERE table_name = :table_name"""
                                table_name = selected_table.upper().replace("BARS.", "")  # отбрасываем bars., если есть
                                # print(table_name)
                                # Выполнение запроса для получения полей таблицы selected_table
                                fields_rows_base = connect_to_base_and_execute(query_fields_rows_base, error_label,
                                                                               user, password, parse_button, table_name)
                                if fields_rows_base:
                                    # print("fields_rows_base", fields_rows_base,
                                    #       "type(fields_rows_base)", type(fields_rows_base))
                                    for field in fields_rows_base:
                                        print('field[0]', field[0], 'type(field[0])', type(field[0]))
                                        columns_list.append(selected_table + '.' + field[0])

                            # Выполнение запроса select * from dk, second_table...
                            star_rows = connect_to_base_and_execute(query, error_label, user, password, parse_button,
                                                                    "''")
                            if star_rows:
                                table.clear()

                                table.setColumnCount(
                                    len(columns_list))  # Устанавливаем количество колонок, равное к-ву полей в запросе
                                # table.setRowCount(1)  # и одну строку в таблице
                                table.setRowCount(min(30, len(star_rows)))  # и количество строк в таблице
                                table.setHorizontalHeaderLabels(columns_list)
                                for line, star_row in enumerate(star_rows):
                                    # print("line", line)
                                    for i, star_header in enumerate(columns_list):
                                        # Устанавливаем всплывающие подсказки на заголовки
                                        table.horizontalHeaderItem(i).setToolTip(star_header)
                                        # table.horizontalHeaderItem(1).setToolTip("Column 2 ")
                                        # Устанавливаем выравнивание на заголовки
                                        table.horizontalHeaderItem(i).setTextAlignment(Qt.AlignLeft)
                                        # print("star_row", star_row)
                                        # print("star_row[i]", star_row[i])
                                        # print("QTableWidgetItem(str(star_row[i]))", QTableWidgetItem(str(star_row[i])))
                                        # заполняем строку
                                        table.setItem(line, i, QTableWidgetItem(str(star_row[i])))
                                # делаем ресайз колонок по содержимому
                                table.resizeColumnsToContents()
                    except cx_Oracle.InterfaceError as driver_interface_error:
                        print("Driver interface error", driver_interface_error, "rows", rows, "error_label.text()",
                              error_label.text())
                        # return rows
                else:
                    table.setColumnCount(0)  # Устанавливаем к-во колонок
                    table.setRowCount(0)  # и количество строк в таблице
                    table.clear()
        else:
            error_label.setText('В качестве запросов вы можете использовать только выборки "SELECT"!')
    except IndexError:
        error_label.setText('Пустой запрос?')


class Main(QMainWindow):

    def __init__(self):
        super().__init__()

        self.ok_button = QPushButton("Запустить")
        self.cancel_button = QPushButton("Результат смотри тут")
        self.error_label = QLabel("Количество строк или ошибки будут тут")
        self.user_entry = QLineEdit("user5301")
        self.pass_entry = QLineEdit("d")
        self.text_edit1 = QTextEdit()
        self.text_edit2 = QTextEdit()
        self.text_edit3 = QTextEdit()

        self.start_button1 = QPushButton("Старт")
        self.start_button2 = QPushButton("Старт")
        self.stop_button1 = QPushButton("Стоп")
        self.stop_button2 = QPushButton("Стоп")
        self.start_button1.setEnabled(True)
        self.stop_button1.setEnabled(False)
        self.start_button2.setEnabled(True)
        self.start_button1.setStyleSheet("background-color: rgb(81,142,144)")
        self.start_button2.setStyleSheet("background-color: rgb(81,142,144)")
        self.stop_button2.setEnabled(False)
        self.bad_interval_l = QLabel("Интервал")
        self.pts_interval_l = QLabel("Интервал")
        self.bad_interval_e = QLineEdit()
        self.pts_interval_e = QLineEdit()
        self.bad_timer_id = 0
        self.pts_timer_id = 0

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

    def bad_on_start(self):
        self.bad_timer_id = self.startTimer(int(self.bad_interval_e.text()))
        self.start_button1.setEnabled(False)
        self.stop_button1.setEnabled(True)

    def pts_on_start(self):
        self.pts_timer_id = self.startTimer(int(self.pts_interval_e.text()))
        self.start_button2.setEnabled(False)
        self.stop_button2.setEnabled(True)

    def bad_on_stop(self):
        if self.bad_timer_id:
            self.killTimer(self.bad_timer_id)
            self.bad_timer_id = 0
        self.start_button1.setEnabled(True)
        self.stop_button1.setEnabled(False)

    def pts_on_stop(self):
        if self.pts_timer_id:
            self.killTimer(self.pts_timer_id)
            self.pts_timer_id = 0
        self.start_button2.setEnabled(True)
        self.stop_button2.setEnabled(False)

    def timerEvent(self, event):
        self.error_label.setText("Сработал таймер" + str(event.timerId()))

        print("Сработал таймер", str(event.timerId()), "bad time", self.bad_timer_id, "pts time", self.pts_timer_id)
        query_index = 3  #
        if event.timerId() == self.bad_timer_id:
            query_index = 0
        elif event.timerId() == self.pts_timer_id:
            query_index = 1
        else:
            query_index = 3
        run(query_index, self.text_edit1, self.text_edit2, self.text_edit3, self.error_label,
            self.user_entry.text(),
            self.pass_entry.text(), self.cancel_button, self.table)
        print("rowCount", self.table.rowCount())
        if query_index == 0 and self.table.rowCount() != 0:
            frequency = 2500
            duration = 2000
            winsound.Beep(frequency, duration)
        elif query_index == 1 and self.table.rowCount() == 0:
            frequency = 1500
            duration = 3000
            winsound.Beep(frequency, duration)

    def init_ui(self):
        # textEdit = QTextEdit()

        self.central_widget = QWidget(self)  # Создаём центральный виджет
        self.setCentralWidget(self.central_widget)

        self.pass_entry.setEchoMode(QLineEdit.PasswordEchoOnEdit)
        vbox = QVBoxLayout(self.central_widget)

        self.top = QTabWidget(self.central_widget)
        q = """select a.fn "Файл", a.dat "dat", a.kv "Валюта", a.skr "Сума файла", a.n "К-во пл", a.otm "otm", \
        a.k_er "Ошибка", b.nb "Банк отправителя", a.sign_key "Ключ" from bars.zag_b a, bars.banks$base b \
        where a.DAT >= trunc(sysdate) and a.kf = b.mfo and a.otm <= 3 and \
        to_char(a.dat + INTERVAL '20' MINUTE,'DD.MM.YYYY HH24:MI') <= to_char(sysdate,'DD.MM.YYYY HH24:MI') \
        group by  fn, a.dat, a.kv, a.skr, a.n, a.otm, a.k_er, b.nb, a.kf, a.sign_key order by a.kf, a.dat"""
        # print("q", q, "end q")
        # self.text_edit1 = QTextEdit()
        self.text_edit1.setPlainText(q)
        # ok_button.clicked.connect(lambda: run(q, error_label, user_entry.text(), pass_entry.text(), cancel_button))
        # self.ok_button.clicked.connect(lambda: run(self.text_edit1.toPlainText(), self.error_label,
        # self.user_entry.text(), self.pass_entry.text(), self.cancel_button))
        self.top.addTab(self.text_edit1, "Файлы, не сквитованые более 20 мин")
        q2 = """select * from bars.SEC_AUDIT \
        where REC_DATE >= trunc(sysdate) \
        and to_char(REC_DATE,'DD.MM.YYYY HH24:MI') >= to_char(sysdate-interval '30' MINUTE, 'DD.MM.YYYY HH24:MI') \
        and REC_UNAME = 'TECH_BPK' \
        and REC_MODULE = 'Toss.Net'
        order by REC_DATE desc"""

        # self.text_edit2 = QTextEdit()
        self.top.addTab(self.text_edit2, "Контроль вертушки ПЦ")
        self.text_edit2.setPlainText(q2)
        self.top.addTab(self.text_edit3, "Произвольный запрос")
        q3 = """select * from dk"""
        self.text_edit3.setPlainText(q3)
        self.top.currentChanged.connect(self.top_on_current_change)

        self.bottom = QTabWidget(self.central_widget)
        self.bottom.setTabPosition(QTabWidget.South)  # внизу

        self.table = QTableWidget(self)  # Создаём таблицу
        # self.ok_button.clicked.connect(
        #    lambda: run(top.currentIndex(), self.text_edit1, self.text_edit2, self.error_label, self.user_entry.text(),
        #                 self.pass_entry.text(), self.cancel_button, table))
        self.ok_button.clicked.connect(
            lambda: run(self.top.currentIndex(), self.text_edit1, self.text_edit2, self.text_edit3, self.error_label, self.user_entry.text(),
                        self.pass_entry.text(), self.cancel_button, self.table))
        # self.table.setColumnCount(3)  # Устанавливаем три колонки
        # self.table.setRowCount(2)  # и две строки в таблице

        # Устанавливаем заголовки таблицы
        # self.table.setHorizontalHeaderLabels(["Header 1", "Header 2", "Header 3"])

        # Устанавливаем всплывающие подсказки на заголовки
        # self.table.horizontalHeaderItem(0).setToolTip("Column 1 ")
        # self.table.horizontalHeaderItem(1).setToolTip("Column 2 ")
        # self.table.horizontalHeaderItem(2).setToolTip("Column 3 ")

        # Устанавливаем выравнивание на заголовки
        # self.table.horizontalHeaderItem(0).setTextAlignment(Qt.AlignLeft)
        # self.table.horizontalHeaderItem(1).setTextAlignment(Qt.AlignHCenter)
        # self.table.horizontalHeaderItem(2).setTextAlignment(Qt.AlignRight)

        # заполняем первую строку
        # self.table.setItem(0, 0, QTableWidgetItem("Text0 in column 1"))
        # self.table.setItem(0, 1, QTableWidgetItem("Text0 in column 2"))
        # self.table.setItem(0, 2, QTableWidgetItem("Text0 in column 3"))

        # заполняем первую строку
        # self.table.setItem(1, 0, QTableWidgetItem("Text1 in column 1"))
        # self.table.setItem(1, 1, QTableWidgetItem("Text1 in column 2"))
        # self.table.setItem(1, 2, QTableWidgetItem("Text1 in column 3"))

        # делаем ресайз колонок по содержимому
        # self.table.resizeColumnsToContents()
        self.bottom.addTab(self.table, "Результат")
        messages_text_edit = QTextEdit()
        self.bottom.addTab(messages_text_edit, "Сообщения")
        self.bottom.currentChanged.connect(self.bottom_on_current_change)
        # grid_layout.addWidget(bottom, 0, 0)  # Добавляем таблицу в сетку

        splitter_vertical = QSplitter(Qt.Vertical)
        splitter_vertical.addWidget(self.top)
        splitter_vertical.addWidget(self.bottom)

        vbox.addWidget(splitter_vertical)
        hbox = QHBoxLayout(self.central_widget)
        hbox.addWidget(self.ok_button)
        hbox.addWidget(self.cancel_button)
        hbox.addWidget(self.user_entry)
        hbox.addWidget(self.pass_entry)
        self.bad_group = QGroupBox("Таймер несквитованных")
        self.bad_group.setStyleSheet("font: corbel; font-size: 14px;")
        h_bad_group = QHBoxLayout()  # Контейнер для группы
        h_bad_group.addWidget(self.start_button1)
        h_bad_group.addWidget(self.stop_button1)
        h_bad_group.addWidget(self.bad_interval_l)
        h_bad_group.addWidget(self.bad_interval_e)

        self.bad_group.setLayout(h_bad_group)
        hbox.addWidget(self.bad_group)
        self.pts_group = QGroupBox("Таймер вертушки ПЦ")  # ,
        self.pts_group.setStyleSheet("font: sitka; font-size: 14px;")
        h_pts_group = QHBoxLayout()  # Контейнер для группы
        h_pts_group.addWidget(self.start_button2)
        h_pts_group.addWidget(self.stop_button2)
        h_pts_group.addWidget(self.pts_interval_l)
        h_pts_group.addWidget(self.pts_interval_e)
        self.pts_group.setLayout(h_pts_group)
        hbox.addWidget(self.pts_group)

        hbox.addWidget(self.error_label)
        hbox.addStretch(1)
        vbox.addLayout(hbox)
        self.central_widget.setLayout(vbox)

        # QAction является абстракцией для действий, совершенных из меню, панели инструментов, или комбинаций клавиш.
        exitAction = QAction(QIcon('exit.png'), '&Выход',
                             self)  # В этих трех строках, мы создаем действие с соответствующей иконкой.
        exitAction.setShortcut('Ctrl+Q')  # Кроме того, для этого действия определяется комбинация клавиш.
        exitAction.setStatusTip(
            'Exit application')  # создает подсказку, которая показывается в строке состояния, когда вы наведёте указатель мыши на пункт меню.
        # Когда мы выбираем именно это действие, срабатывает сигнал.
        exitAction.triggered.connect(self.close)  # Сигнал подключен к методу close(). Это завершает приложение.

        # Чтобы получить строку состояния, мы вызываем метод statusBar() класса QtGui.QMainWindow.
        # Первый вызов метода создает строку состояния.
        # Последующие вызовы возвращают объект статусбара.
        # showMessage() отображает сообщение в строке состояния.
        self.statusBar().showMessage('Готово')

        menubar = self.menuBar()  # Метод menuBar() создает строку меню.
        fileMenu = menubar.addMenu('&Файл')  # Мы создаем меню файла
        fileMenu.addAction(exitAction)  # и добавляем к нему действие выхода.

        toolbar = self.addToolBar('Выход')
        toolbar.addAction(exitAction)

        file_name = 'ini_timers'
        with open(file_name) as f:
            lines = f.readlines()
            try:
                self.bad_interval_e.setText(lines[0])
            except:
                self.error_label.setText(' Возможно в первой строке файла ini_timers нет времени таймера несквитованых!')
            try:
                self.pts_interval_e.setText(lines[1])
            except:
                self.error_label.setText(' Возможно в первой строке файла ini_timers нет времени таймера вертушки ПЦ!')

        self.start_button1.clicked.connect(self.bad_on_start)
        self.start_button2.clicked.connect(self.pts_on_start)
        self.stop_button1.clicked.connect(self.bad_on_stop)
        self.stop_button2.clicked.connect(self.pts_on_stop)

        self.setGeometry(300, 100, 850, 550)
        self.setWindowTitle('Таймеры')
        ##        self.setWindowIcon(QIcon('cfg.ico'))
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = Main()
    sys.exit(app.exec_())
