

def connect_to_base_and_execute(query, error_label, gui="pyqt", base="oracle"):
    print("query", query)
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



if __name__ == '__main__':
    pass
