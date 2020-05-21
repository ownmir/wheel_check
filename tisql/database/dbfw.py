

def connect_to_base_and_execute(query, error_label, user, password, parse_button, table_name, gui="pyqt", base="oracle",
                                name_base_sqlite3="testdb.db"):

    if gui == "tkinter":
        error_label['text'] = ''
    else:
        error_label.setText(query)
    try:
        if base == "oracle":
            import os
            os.environ['NLS_LANG'] = 'American_America.AL32UTF8'
            import cx_Oracle as driver
        else:
            import sqlite3 as driver
    except ModuleNotFoundError as info:
        print('Module Not Found Error:', info)
        return
    if base == "oracle":
        print('Welcome to Oracle driver!')
    else:
        print('Welcome to else driver!')
    try:
        if base == "oracle":
            # connection = driver.connect(user, password, 'XE')
            connection = driver.connect(user, password, 'MMFO')
            print("Connect encod", connection.encoding)
        else:
            connection = driver.connect(name_base_sqlite3)
        print("Connect is created.")
        if gui == "tkinter":
            parse_button['text'] = 'Список МФО, запрос (Пользователь и пароль должны быть правильными.)'
        else:
            parse_button.setText("Запрос (Пользователь и пароль должны быть правильными.)")
        result = ''
        if base == 'oracle':
            context = connection.cursor()
        else:
            context = connection

        with context as cursor:
            print("Cursor is created.")
            # так объявляется курсорная переменная
            # ret = cursor.var(ora.CURSOR)
            # cursor.execute('''begin test_cur(1, 20, :ret); end; ''', ret=ret)
            if base == "oracle":
                cursor.execute('''begin  bars.bars_login.login_user(sys_guid, 1, null, null); end; ''')
                print("Bars login.")
            # print(cursor)
            try:
                print("After query", query)
                if table_name == "''":
                    rows = list(cursor.execute(query))
                else:
                    print("table_name in dbfw.connect_to_base_and_execute")
                    print(table_name)
                    named_params = {'table_name': table_name}
                    rows = list(cursor.execute(query, named_params))
                if rows:

                    print("Executed.")

                    print("base", base)
                    if base == "oracle":
                        num_lines = str(len(rows))
                        result += '\nСтрок ' + num_lines
                        # for row in rows:
                        #     result += '{}\n'.format(row)
                    else:
                        num_lines = str(rows.arraysize)
                        result += '\nСтрок ' + num_lines
            except driver.DatabaseError as query_error:
                if gui == "tkinter":
                    parse_button['text'] = 'Список МФО, запрос (БЫЛА ОШИБКА ЗАПРОСА!)'
                else:
                    parse_button.setText("Запрос (БЫЛА ОШИБКА ЗАПРОСА!)")
                print('Query error: ', query_error)
                rows = None
        if result == '':
            if gui == "tkinter":
                error_label['text'] = 'Нет данных по блокированным.'
            else:
                error_label.setText('Нет данных')
        else:
            if gui == "tkinter":
                error_label['text'] = result
            else:
                error_label.setText(result)
        if rows:
            print("Возвращаем rows..", rows)
            return rows
    except driver.DatabaseError as connect_error:
        if gui == "tkinter":
            parse_button['text'] = 'Список МФО, запрос (БЫЛА ОШИБКА СОЕДИНЕНИЯ!)'
        else:
            parse_button.setText("Запрос (БЫЛА ОШИБКА СОЕДИНЕНИЯ!)")
        print('Connect error: ', connect_error)
    print("query", query)


if __name__ == '__main__':
    pass
