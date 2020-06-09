from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, qApp, QLineEdit, QTextEdit, QHBoxLayout, QFormLayout
from PyQt5.QtWidgets import QComboBox
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap, QPalette, QBrush, QIcon
from PyQt5.QtSql import QSqlDatabase
import sys


def on_db(driver, tns, port, user, passw):
    # conn_oracle = QSqlDatabase.addDatabase("QOCI", connectionName=tns)
    conn = QSqlDatabase.addDatabase(driver, connectionName=tns)
    conn.setPort(int(port))
    conn.setUserName(user)
    conn.setPassword(passw)
    conn.setDatabaseName(tns)
    if conn.open():
        print("Database is opened.")
    else:
        conn.lastError().text()


print("Begin")
app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle('db QFormLayout')
window.resize(400, 75)
# window.resize(1920, 1080)
driverComboBox = QComboBox()
driverComboBox.addItem(QIcon("sqlite.svg"), "QSQLITE")
driverComboBox.addItem(QIcon("mysql.svg"), "QMYSQL")
driverComboBox.addItem(QIcon("oracle-6.svg"), "QOCI")
# driverLineEdit = QLineEdit("QSQLITE")
# driverLineEdit = QLineEdit("QMYSQL")
# tnsLineEdit = QLineEdit("XE")
# tnsLineEdit = QLineEdit("D:/Work/virte/pyqt5/Scripts/mytest.db")
tnsLineEdit = QLineEdit("world")
portLE = QLineEdit("3306")
# userLineEdit = QLineEdit("user5301")
userLineEdit = QLineEdit("root")
passLineEdit = QLineEdit("e")
passLineEdit.setEchoMode(QLineEdit.PasswordEchoOnEdit)
# textEdit = QTextEdit()
b1 = QPushButton("О&тправить")
b2 = QPushButton("О&чистить")
hbox = QHBoxLayout()
hbox.addWidget(b1)
hbox.addWidget(b2)
form = QFormLayout()
# form.addRow("&Драйвер:", driverLineEdit)
form.addRow("&Драйвер:", driverComboBox)
form.addRow("&Название:", tnsLineEdit)
form.addRow("P&ort:", portLE)
form.addRow("&Пользователь:", userLineEdit)
form.addRow("П&ароль:", passLineEdit)
form.addRow(hbox)
window.setLayout(form)

x = driverComboBox.currentText()
driverComboBox.activated.connect(on_active)
y = tnsLineEdit.text()
print("y", y, "type(y)", type(y))
b1.clicked.connect(lambda driver=x, tns=y, port=portLE.text(), user=userLineEdit.text(),
                          passw=passLineEdit.text(): on_db("QSQLITE", tns, port, user, passw))
print("End")
window.show()
sys.exit(app.exec_())
