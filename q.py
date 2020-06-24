import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QTableView
from PyQt5.QtSql import QSqlDatabase, QSqlQuery, QSqlQueryModel, QSqlTableModel


app = QApplication(sys.argv)
db = QSqlDatabase.addDatabase("QODBC3")
db.setHostName("localhost")
db.setDatabaseName("XE")
db.setUserName("user5301")
db.setPassword("xyz")
qry = QSqlQuery()
if db.open():
    #qry = db.exec("begin  bars.bars_login.login_user(sys_guid, 1, null, null); end;")
    #qry.finish()
    qry = db.exec("select dk, name from dk")
tabmodel = QSqlTableModel()
tabmodel.setQuery(qry)
tabmodel.setHeaderData(0, Qt.Horizontal, "ID")
tabmodel.setHeaderData(1, Qt.Horizontal, "Name")
tabview = QTableView()
tabview.setModel(tabmodel)
tabview.show()
db.close()
app.exec()
