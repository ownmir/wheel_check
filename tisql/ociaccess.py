import sys
from PySide2.QtWidgets import QWidget, QApplication
from PySide2.QtSql import QSqlQueryModel, QSqlQuery, QSqlDatabase
from mani import mani


app = QApplication.instance()
if app is None: 
    app = QApplication([])
conn = QSqlDatabase.addDatabase("QOCI")
conn.setDatabaseName("XE")
conn.setHostName("localhost")
conn.setPort(1521)
conn.setUserName("user5301")
# sys.path.append(r"D:\Work\Py3proj\pyqt5\lisql")
# sys.path.append(r"D:\Work\Py3proj\tisql64")
# import ociaccess
#from getpass import getpass
#passw = getpass('Please enter your password ')
#conn.setPassword(passw)
#passw = "p@wfnnJHJN)njb^hb,^^GHGhg;bbvcdr"
mani(conn)
reso = conn.open()
print("Result", reso, "E", conn.lastError().text())
resc = conn.close()
app.deleteLater()
del conn
del app
input()
sys.exit(0)
