from PySide2 import QtWidgets, QtCore
from PySide2.QtSql import QSqlQuery, QSqlQueryModel
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
        if query.exec_("create table good(id integer primary key autoincrement, goodname text, goodcount integer) "):
            query.finish()
            query.prepare("insert into good values (null, ?, ?)")
            query.addBindValue('FlashDrive')
            query.addBindValue(10)
            if not query.exec_():
                print("Error with insert record flashdrive", e.lastError().text())
            query.finish()
            query.prepare("insert into good values (null, ?, ?)")
            query.bindValue(0, 'Paper for printer')
            query.bindValue(1, 3)
            if not query.exec_():
                print("Error with insert record paper", e.lastError().text())
            query.finish()
            query.prepare("insert into good values (null, :name, :count)")
            query.bindValue(':name', 'Cartridge for printer')
            query.bindValue(':count', 8)
            if not query.exec_():
                print("error with insert record cartridge", e.lastError().text())
            query.finish()
            query.prepare("insert into good values (null, :name, :count)")
            list1 = ['Cd', 'Dvd', 'Scanner']
            list2 = [9, 4, 7]
            query.bindValue(':name', list1)
            query.bindValue(':count', list2)
            if not query.execBatch():
                print("error with batch", e.lastError().text())
            query.finish()
        else:
            print("Error with create table good", e.lastError().text())
    good_select = "select * from good order by goodname"
    query.prepare(good_select)
    query.setForwardOnly(True)
    if query.exec_():
        print("Select is done")
        lst =[]
        if query.isActive():  # запрос находится в активном состоянии, т е ранее вызывались методы exec_, execBatch
            query.first()  # Есть еще seek
            while query.isValid():  # если внутренний указатель указывает на какую-либо запись
                lst.append(query.value('goodname') + ": " + str(query.value('goodcount')) + ' шт.')
                print("Number of record", query.at(), "about record", query.record())
                query.next()
            for p in lst: print(p)
    else:
        print("Error in select")

    query.finish()
    window = QtWidgets.QTableView()
    window.setWindowTitle("QSqlQueryModel")
    # Create model
    sqm = QSqlQueryModel(parent=window)
    sqm.setQuery(good_select)
    # Задаем заголовки для столбцов модели
    sqm.setHeaderData(1, QtCore.Qt.Horizontal, "Название")
    sqm.setHeaderData(2, QtCore.Qt.Horizontal, "Количество")
    # Задаем для талицы только что созданную модель
    window.setModel(sqm)
    # Скрываем первый столбец, в котором выводится идентификатор
    window.hideColumn(0)
    window.setColumnWidth(1, 150)
    window.setColumnWidth(2, 60)
    window.resize(230, 130)
    window.show()
    connn.close()
    print("Close. Thanks.")
    sys.exit(app.exec_())