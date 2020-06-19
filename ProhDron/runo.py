from PySide2 import QtWidgets
import sys
from wwdb import WorkWithLiteDB, WorkWithMyDB, WorkWithODBC

app = QtWidgets.QApplication(sys.argv)
# e = WorkWithLiteDB("D:/Work/Py3proj/duties/a.db")
e = WorkWithLiteDB("D:/Work/Py3proj/pyqt5/lisql/testdb.db")
# e = WorkWithODBC("MySQL ODBC 5.3 Unicode Driver", "MY", "localhost", 3306, "root", "322067")
# e = WorkWithODBC("MySQL ODBC 5.3 Unicode Driver", "XESN", "localhost", 1521, "user5301", "us322067")
print("Name of database:", e.name)
connn = e.open_db()
if connn:
    print(e.name, "Database is opened.")
    tables = connn.tables()
    print("tables", tables)
    for table in tables:

        record = connn.record(table)
        if record.isEmpty():
            print("No fields in table", table)
            continue
        print("Count of fields", record.count())
        for i in range(0, 2):
            field = record.field(i)
            print("field.name()", field.name(), "field.type()", field.type(), "field.length()", field.length(),
                  "field.precision()", field.precision(), "field.defaultValue()", field.defaultValue(),
                  "requiredStatus", field.requiredStatus(), "isAutoValue", field.isAutoValue(),
                  "isReadOnly", field.isReadOnly())
        index = connn.primaryIndex(table)
        print("name", index.name(), "Count of fields in index", index.count(), "isDescending", index.isDescending(0),
              )
    connn.close()
