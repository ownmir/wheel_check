

def connect_to_base_and_execute(query, error_label, user, password, parse_button, gui="pyqt", base="oracle"):

    if gui == "tkinter":
        error_label['text'] = ''
    else:
        error_label.setText(query)
    try:
        if base == "oracle":
            import cx_Oracle as ora
        else:
            pass
    except ModuleNotFoundError as info:
        print('Module Not Found Error:', info)
        return
    if base == "oracle":
        print('Welcome to Oracle driver!')
    else:
        print('Welcome to else driver!')
    try:
        connection = ora.connect(user, password, 'MMFO')
        print("Connect is created.")
        if gui == "tkinter":
            parse_button['text'] = 'Список МФО, запрос (Пользователь и пароль должны быть правильными.)'
        else:
            parse_button.setText("Запрос (Пользователь и пароль должны быть правильными.)")
        result = ''
        with connection.cursor() as cursor:
            print("Cursor is created.")
            # так объявляется курсорная переменная
            # ret = cursor.var(ora.CURSOR)
            # cursor.execute('''begin test_cur(1, 20, :ret); end; ''', ret=ret)
            cursor.execute('''begin  bars.bars_login.login_user(sys_guid, 1, null, null); end; ''')
            print("Bars login.")
            # print(cursor)
            try:
                print("After query", query)
                for row in cursor.execute(query):
                    result += '{}\n'.format(row)
                print("Executed.")
            except ora.DatabaseError as query_error:
                if gui == "tkinter":
                    parse_button['text'] = 'Список МФО, запрос (БЫЛА ОШИБКА ЗАПРОСА!)'
                else:
                    parse_button.setText("Запрос (БЫЛА ОШИБКА ЗАПРОСА!)")
                print('Query error: ', query_error)
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
    except ora.DatabaseError as connect_error:
        if gui == "tkinter":
            parse_button['text'] = 'Список МФО, запрос (БЫЛА ОШИБКА СОЕДИНЕНИЯ!)'
        else:
            parse_button.setText("Запрос (БЫЛА ОШИБКА СОЕДИНЕНИЯ!)")
        print('Connect error: ', connect_error)
    print("query", query)


if __name__ == '__main__':
    pass
