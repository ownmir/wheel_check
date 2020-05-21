class str2(str):
    def __repr__(self):
        return ''.join(('"', super().__repr__()[1:-1], '"'))


def connect_to_base_and_execute(query, user, password, parameter):
    import os
    os.environ['NLS_LANG'] = 'American_America.AL32UTF8'
    try:
        import cx_Oracle as driver
        import json
    except ModuleNotFoundError as info:
        print('Module Not Found Error:', info)
        return
    print('Welcome to Oracle driver!')
    try:
        connection = driver.connect(user, password, 'MMFO')
        print("Connect is created.")
        context = connection.cursor()
        with context as cursor:
            print("Cursor is created.")
            named_params = {"table_name": parameter}
            print('named_params["table_name"]', named_params["table_name"])
            # double_query = str2(query)
            # print(double_query)
            # print(query)
            try:
                rows = list(cursor.execute(query, named_params))
            except driver.DatabaseError as query_error:
                print('Query error: ', query_error)
                rows = None
        if rows:
            print(rows)
            return rows
    except driver.DatabaseError as connect_error:
        print('Connect error: ', connect_error)
