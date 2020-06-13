from PySide2 import QtWidgets
import sys
from wwdb import WorkWithLiteDB, WorkWithMyDB

app = QtWidgets.QApplication(sys.argv)
# e = WorkWithLiteDB("D:/Work/Py3proj/duties/a.db")
# e = WorkWithLiteDB("D:/Work/Py3proj/a.db")
e = WorkWithMyDB("adb", "3306", "neo", "pp12")
print("Name of database:", e.name)
connn = e.open_db()
if connn:
    print(e.name, "database is opened")
    connn.close()
    
