import sys
from PySide2.QtWidgets import QWidget, QApplication, QLabel, QLineEdit, QHBoxLayout, QFormLayout, QPushButton, QGroupBox
from PySide2.QtWidgets import QVBoxLayout, QTableView
from PySide2.QtCore import Qt
from PySide2.QtSql import QSqlQueryModel
from wwdb import WorkWithLiteDB, WorkWithODBC


class Main(QWidget):

    def __init__(self):
        super().__init__()

        self.user_entry = QLineEdit("user5301")
        self.pass_entry = QLineEdit("e")
        self.pass_entry.setEchoMode(QLineEdit.PasswordEchoOnEdit)
        self.ru_entry = QLineEdit("300465")
        self.cur_entry = QLineEdit("840")
        self.balance_entry = QLineEdit()
        self.ok_button = QPushButton("Запустить")
        self.ok_button.setStyleSheet("color: rgb(160, 70, 70)")
        self.error_label = QLabel("Ошибки будут тут")
        self.error_label.setStyleSheet("color: rgb(255, 142, 144)")

        self.start_button1 = QPushButton("Старт")
        self.stop_button1 = QPushButton("Стоп")
        self.start_button1.setEnabled(True)
        self.stop_button1.setEnabled(False)
        self.start_button1.setStyleSheet("background-color: rgb(81,142,144)")
        self.interval_l = QLabel("Интервал")
        self.interval_e = QLineEdit()
        self.timer_id = 0
        self.table = QTableView()

        self.init_ui()

    def on_start(self):
        self.timer_id = self.startTimer(int(self.interval_e.text()))
        self.start_button1.setEnabled(False)
        self.stop_button1.setEnabled(True)

    def on_stop(self):
        if self.timer_id:
            self.killTimer(self.timer_id)
            self.timer_id = 0
        self.start_button1.setEnabled(True)
        self.stop_button1.setEnabled(False)

    def init_ui(self):
        file_name = 'ini_balance'
        with open(file_name) as f:
            lines = f.readlines()
            try:
                self.interval_e.setText(lines[0])
            except:
                self.error_label.setText(' Возможно в первой строке файла ini_balance нет времени таймера!')

        self.start_button1.clicked.connect(self.on_start)
        self.stop_button1.clicked.connect(self.on_stop)

        hbox = QHBoxLayout()
        hbox.addWidget(self.ok_button)
        self.group = QGroupBox("Таймер остатка")
        self.group.setStyleSheet("font: corbel; font-size: 14px;")
        v_group = QVBoxLayout()  # Контейнер для группы
        v_group.addWidget(self.start_button1)
        v_group.addWidget(self.stop_button1)
        v_group.addWidget(self.interval_l)
        v_group.addWidget(self.interval_e)

        self.group.setLayout(v_group)
        hbox.addWidget(self.group)
        form = QFormLayout()
        form.addRow("&User", self.user_entry)
        form.addRow("&Пароль", self.pass_entry)
        form.addRow("&МФО области", self.ru_entry)
        form.addRow("&Валюта", self.cur_entry)
        form.addRow("&Необходимый остаток", self.balance_entry)
        form.addRow(hbox)
        form.addRow("Результат", self.table)
        e = WorkWithLiteDB("D:/Work/Py3proj/pyqt5/lisql/testdb.db")
        print("Name of database:", e.name)
        conn = e.open_db()
        if conn:
            # Create model
            sqm = QSqlQueryModel(parent=self.table)
            good_select = "select * from good order by goodname"
            sqm.setQuery(good_select)
            # Задаем заголовки для столбцов модели
            sqm.setHeaderData(1, Qt.Horizontal, "Название")
            sqm.setHeaderData(2, Qt.Horizontal, "Количество")
            # Задаем для талицы только что созданную модель
            self.table.setModel(sqm)
            # Скрываем первый столбец, в котором выводится идентификатор
            self.table.hideColumn(0)
            self.table.setColumnWidth(1, 150)
            self.table.setColumnWidth(2, 60)
        self.setLayout(form)
        self.setGeometry(300, 100, 650, 450)
        self.setWindowTitle('Ждем деньги')

        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = Main()
    sys.exit(app.exec_())
