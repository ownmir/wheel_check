from PySide2 import QtWidgets
import sys
from wwdb import WorkWithLiteDB, WorkWithMyDB, WorkWithODBC

app = QtWidgets.QApplication(sys.argv)
# e = WorkWithLiteDB("D:/Work/Py3proj/duties/a.db")
# e = WorkWithLiteDB("D:/Work/Py3proj/a.db")
e = WorkWithODBC("MySQL ODBC 5.3 Unicode Driver", "MY", "localhost", 3306, "root", "322067")
# e = WorkWithODBC("MySQL ODBC 5.3 Unicode Driver", "XESN", "localhost", 1521, "user5301", "us322067")
print("Name of database:", e.name)
connn = e.open_db()
if connn:
    print(e.name, "Database is opened.")
    record_info = e.record()
    connn.close()
