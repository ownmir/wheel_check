import sys
from PySide2.QtWidgets import QWidget, QApplication
from PySide2.QtSql import QSqlQueryModel, QSqlQuery, QSqlDatabase

app = QApplication(sys.argv)
conn = QSqlDatabase.addDatabase("QOCI")
conn.setDatabaseName("MMFO")
conn.setHostName("localhost")
conn.setPort(1521)
conn.setUserName("user5301")
# sys.path.append(r"D:\Work\Py3proj\pyqt5\lisql")
# import ociaccess
from getpass import getpass
passw = getpass('Please enter your password ')
conn.setPassword(passw)
passw = "p@wfnnJHJN)njb^hb,^^GHGhg;bbvcdr"
reso = conn.open()
print("Result", reso, "E", conn.lastError().text())
conn.close()
