import sys
from PySide2.QtWidgets import QWidget, QApplication, QLabel, QLineEdit, QHBoxLayout, QFormLayout, QPushButton, QGroupBox
from PySide2.QtWidgets import QVBoxLayout, QTableView
from PySide2.QtCore import Qt
from PySide2.QtGui import QPixmap, QStandardItemModel, QStandardItem
from PySide2.QtSql import QSqlQueryModel, QSqlQuery
##from database.wwdb import WorkWithLiteDB, WorkWithODBC, WorkWithOCI
from database.dbfw import connect_to_base_and_execute
##import sqlparse
import cx_Oracle
import winsound
import hashlib
import getpass
import keyring
import k10


class Main(QWidget):

    def __init__(self):
        super().__init__()

        self.user_entry = QLineEdit("user5301")
        # self.user_entry.setStyleSheet("font: corbel; font-size: 12px;")
        self.pass_entry = QLineEdit("e", self)
        self.odbc = ""
        self.bars = ""
        self.table_query = ""
        self.pass_entry.setEchoMode(QLineEdit.PasswordEchoOnEdit)
        self.ru_entry = QLineEdit("328845", self)
        # self.ru_entry.setStyleSheet("font: corbel; font-size: 12px;")
        self.cur_entry = QLineEdit("840")
        # self.cur_entry.setStyleSheet("font: corbel; font-size: 12px;")
        self.balance_entry = QLineEdit("213000001")
        # self.balance_entry.setStyleSheet("font: corbel; font-size: 12px;")
        self.ok_button = QPushButton("Запрос (Пользователь и пароль должны быть правильными.)")
        self.ok_button.setStyleSheet("font: corbel; font-size: 12px; color: rgb(0, 0, 255)")
        # self.ok_button.setStyleSheet("color: rgb(160, 70, 70)")
        self.error_label = QLabel("Количество строк или ошибки будут тут")
        self.error_label.setStyleSheet("color: rgb(255, 0, 0)")

        self.start_button1 = QPushButton("Старт")
        self.stop_button1 = QPushButton("Стоп")
        self.start_button1.setEnabled(True)
        self.stop_button1.setEnabled(False)
        self.start_button1.setStyleSheet("background-color: rgb(81,142,144)")
        self.interval_l = QLabel("Интервал")
        # self.interval_l.setStyleSheet("font: corbel; font-size: 12px; color: rgb(0, 0, 255)")
        self.interval_e = QLineEdit()
        self.timer_id = 0
        self.table = QTableView()
        # Create model
        # self.sqm = QSqlQueryModel(parent=self.table)
        self.standart_item_model = QStandardItemModel()

        self.init_ui()

    def on_start(self):
        password = self.pass_entry.text()
        if password == "e":
            self.print_and_label("Вы не ввели пароль!")
        else:
            self.timer_id = self.startTimer(int(self.interval_e.text()))
            self.start_button1.setEnabled(False)
            self.stop_button1.setEnabled(True)

    def on_stop(self):
        print("Таймер остановлен.", self.timer_id)
        if self.timer_id:
            self.killTimer(self.timer_id)
            self.timer_id = 0
            self.start_button1.setEnabled(True)
            self.stop_button1.setEnabled(False)

    def print_and_label(self, text):
        print(text)
        self.error_label.setText(text)
    
    def run(self):
        
        rows = connect_to_base_and_execute(self.table_query.format(self.ru_entry.text().strip(), self.cur_entry.text().strip(), int(self.balance_entry.text().strip())), self.error_label, self.user_entry.text(), keyring.get_password(getpass.getuser(), self.user_entry.text()),
                                                                   self.ok_button, "''")
        self.standart_item_model.clear()
        self.table.clearSpans()
        item_list = []
        if rows:
            #print("rows", rows)
            for values in rows:
                item_list = []
                for value in values:
                    if type(value) == int:
                        item = QStandardItem(str(value))
                    else:
                        item = QStandardItem(value)
                    item_list.append(item)
                self.standart_item_model.appendRow(item_list)
            self.standart_item_model.setHorizontalHeaderLabels(["Счет", "РУ", "Валюта",
                                                            "Остаток"])
            self.table.setModel(self.standart_item_model)
            self.table.setColumnWidth(0, 150)
            self.table.setColumnWidth(1, 60)
            self.table.setColumnWidth(2, 80)
            self.table.setColumnWidth(3, 150)
            if self.standart_item_model.rowCount() > 0:
                frequency = 2500
                duration = 2000
                winsound.Beep(frequency, duration)
        
    
    def timerEvent(self, event):
        # self.error_label.setText("Сработал таймер" + str(event.timerId()))

        print("Сработал таймер", str(event.timerId()))
        self.run()
    
    def init_ui(self):
        file_name = 'ini_balance'
        with open(file_name) as f:
            lines = f.readlines()
            try:
                self.interval_e.setText(lines[0])
            except:
                self.error_label.setText(' Возможно в первой строке файла ini_balance нет времени таймера!')
            try:
                self.bars = lines[1]
            except:
                self.error_label.setText(' Возможно во второй строке файла ini_balance нет запроса!')
            try:
                self.table_query = lines[2]
            except:
                self.error_label.setText(' Возможно в третьей строке файла ini_balance нет запроса!')
            

        label = QLabel(self)
        label.setAlignment(Qt.AlignRight)
        label.resize(30,30)
        image = QPixmap("b.jfif", format="JPG").scaled(label.width(), label.height())
        #image = QPixmap("mon.png", format="PNG")
        
        label.setPixmap(image)
        self.group = QGroupBox("Таймер остатка")
        self.group.setStyleSheet("font: corbel; font-size: 14px;")
        v_group = QVBoxLayout()  # Контейнер для группы
        v_group.addWidget(self.start_button1)
        v_group.addWidget(self.stop_button1)
        v_group.addWidget(self.interval_l)
        v_group.addWidget(self.interval_e)
        self.group.setLayout(v_group)
        
        form = QFormLayout()
        form.addRow("", label)
        form.addRow("По&льзователь", self.user_entry)
        form.addRow("&Пароль", self.pass_entry)
        form.addRow("&МФО области", self.ru_entry)
        form.addRow("&Валюта", self.cur_entry)
        form.addRow("&Необходимый остаток", self.balance_entry)
        form.addRow("", self.ok_button)
        form.addRow("", self.group)
        form.addRow("&Результат", self.table)
        form.addRow("&Ошибки", self.error_label)

        self.setLayout(form)
        # k10 - work with password
        # is_right in - hash, return - T/F; set_p in - pass return - hash
        hash_pass = hashlib.md5(self.pass_entry.text().encode('utf-8'))
        # print("hash", hash_pass)
        # keyring.set_password(getpass.getuser(), self.user_entry.text(), self.pass_entry.text())
        self.pass_entry.editingFinished.connect(
            lambda: k10.keyring_pass(getpass.getuser(), self.user_entry.text(), self.pass_entry, hash_pass, self.ru_entry))
        self.ok_button.clicked.connect(
            lambda: self.run())
        self.start_button1.clicked.connect(self.on_start)
        self.stop_button1.clicked.connect(self.on_stop)
        self.setGeometry(300, 100, 650, 550)
        self.setWindowTitle('Ждем деньги')

        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = Main()
    main.setStyleSheet("QLabel {font: corbel; font-size: 12px; color: rgb(0, 0, 255)} QLineEdit {font: corbel; font-size: 12px;}")
    sys.exit(app.exec_())
