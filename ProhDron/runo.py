from PySide2 import QtWidgets
from PySide2.QtSql import QSqlQuery
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
    query = QSqlQuery()
    if 'good' not in tables:
        query.exec_("create table good(id integer primary key autoincrement, goodname text, goodcount integer) ")
    good_record = connn.record('good')
    if good_record == 0:
        query.prepare("insert into good values (null, ?, ?)")
        query.addBindValue('FlashDrive')
        query.addBindValue(10)
        query.exec_()
        query.prepare("insert into good values (null, ?, ?)")
        query.bindValue(0, 'Paper for printer')
        query.bindValue(1, 3)
        query.exec_()
        query.prepare("insert into good values (null, :name, :count)")
        query.bindValue(':name', 'Catrige for printer')
        query.bindValue(':count', 8)
        query.exec_()
        query.prepare("insert into good values (null, :name, :count)")
        list1 = ['Cd', 'Dvd', 'Scaner']
        list2 = [9, 4, 7]
        query.bindValue(':name', list1)
        query.bindValue(':count', list2)
        query.execBatch()
    query.prepare("select * from good order by goodname")
    query.setForwardOnly(True)
    query.exec_()

    connn.close()
