Learn more or give us feedback
from tkinter import *
from _tkinter import TclError
from config import rushki, ru_dic, ru_dic_of, to, write_to_clipboard
import os, glob
import argparse
import getpass
import keyring
import time

def tick():
    root.after(200, tick)
    root.title("Выбор РУ версия 0.2 " + time.strftime('%H:%M:%S')) 

root = Tk()
# root.title("Выбор РУ")
root.after_idle(tick)

lbox_left = Listbox(selectmode=EXTENDED, width=20, height=26, font='Verdana 16')
lbox_left.pack(side=LEFT)
scroll = Scrollbar(command=lbox_left.yview)
scroll.pack(side=LEFT, fill=Y)
lbox_left.config(yscrollcommand=scroll.set)

def to_right():
    select = list(lbox_left.curselection())
    for item in select:
        right_lbox.insert(END, lbox_left.get(item))
    select.reverse()
    for item in select:
        lbox_left.delete(item)
    error_label['text'] = ''

def back():
    select = list(right_lbox.curselection())
    for item in select:
        lbox_left.insert(END, right_lbox.get(item))
    select.reverse()
    for item in select:
        right_lbox.delete(item)

def email():
    if right_lbox.get(END) == '':
        error_label['text'] = 'Не выбраны области!'
    else:
        error_label['text'] = ''
        list_mfo = []
        for item in right_lbox.get(0, END):
            list_mfo.append(ru_dic[item])
        #os.system('powershell D:/Work/Py3proj/TK/tk1/tk1/sendlong.ps1 '+ list_mfo[0])
        import win32com.client as win32
        #  Зайдите в папку C:\Python32\Lib\site-packages\pywin32_system32 и скопируйте оттуда 2 файла (pywintypes32.dll и pythoncom32.dll) в папку C:\Python32\Lib\site-packages\win32.
        outlook = win32.Dispatch('outlook.application')
        mail = outlook.CreateItem(0)
        mail.To = to
        text_ru = ''
        for item in right_lbox.get(0, END):
            text_ru += ru_dic_of[item]
            text_ru += ', '
        text_ru = text_ru.rstrip(', ')
        mail.Subject = 'Повідомлення для здійснення процедури автолонгації  по: ' + text_ru
        HTMLBody = '<h3>Доброго дня!</h3><br>Процедура «Автопереоформлення вкладів» по: <strong>' + text_ru + '</strong> виконана.<br><br>'
        appdata_env = os.environ['APPDATA']
        # print('appdata_env', appdata_env)
        sign_body = ''
        sign_body_txt = ''
        files_signs =  glob.glob(appdata_env + '\\Microsoft\\Signatures\\*.htm')
        # print('files_signs', files_signs)
        htm_size = -1
        for file_sign in files_signs:
            htm_size = os.path.getsize(file_sign)
            if htm_size <= 0:
                break
            with open(file_sign, 'r', encoding='1251') as sign:
                for line in sign:
                    # print('line', line)
                    sign_body += line
            break
        files_signs =  glob.glob(appdata_env + '\\Microsoft\\Signatures\\*.txt')
        # print('files_signs', files_signs)
        for file_sign in files_signs:
            with open(file_sign, 'r', encoding='utf-16') as sign:
                for line in sign:
                    # print('line', line)
                    sign_body_txt += line
            break
        if htm_size <= 0:
            mail.HTMLBody = HTMLBody + sign_body_txt
        else:
            mail.HTMLBody = HTMLBody + sign_body
                # attachment = 'Path'
        # mail.Attachments.Add(attachment)

        mail.Display()

def connect_to_oracle_and_execute(query):
    error_label['text'] = ''
    try:
        import cx_Oracle as ora
    except ImportError as info:
        print('Import Error:', info)
        return
    except ModuleNotFoundError as info:
        print('Module Not Found Error:', info)
        return
    print('Welcome to Oracle driver!')
    user = user_entry.get()
    password = pass_entry.get()
    try:
        connection = ora.connect(user, password, 'MMFO')
        print("Connect is created.")
        parse_button['text'] = 'Список МФО, запрос (Пользователь и пароль должны быть правильными.)'
        result = ''
        with connection.cursor() as cursor:
            print("Cursor is created.")
            # так объявляется курсорная переменная
            # ret = cursor.var(ora.CURSOR)
            # cursor.execute('''begin test_cur(1, 20, :ret); end; ''', ret=ret)
            cursor.execute('''begin  bars.bars_login.login_user(sys_guid, 1, null, null); end; ''')
            print("Bars login.")
            #print(cursor)
            for row in cursor.execute(query):
                result += '{}\n'.format(row)
            print("Executed.")
        if result == '':
            error_label['text'] = 'Нет данных по блокированным.'
        else:
            error_label['text'] = result
    except ora.DatabaseError as connect_error:
        parse_button['text'] = 'Список МФО, запрос (БЫЛА ОШИБКА СОЕДИНЕНИЯ!)'
        print('Connect error: ', connect_error)
    



def parse():
    if right_lbox.get(END) == '':
        error_label['text'] = 'Не выбраны области!'
    else:
        list_mfo_entry.delete(0, END)
        error_label['text'] = ''
        text_sql = ''
        str_list_mfo = "('"
        for item in right_lbox.get(0, END):
            str_list_mfo += ru_dic[item]
            str_list_mfo += "', '"
        str_list_mfo = str_list_mfo.rstrip(", '")
        str_list_mfo += "')"
        print('List mfo:', str_list_mfo)
        list_mfo_entry.insert(0, str_list_mfo)
        str_parse_sql = 'SELECT a.KF "МФО", c.NAME "Регіон", a.BLK "Код блок.", a.KV "Валюта", count(*) "Кільк.",' + "to_char(sum(a.S)/100,'999G999G999G999D99')" + ' "На суму" from bars.ARC_RRP a, bars.REC_QUE b, bars.REGIONS c\n' + \
            'where b.REC = a.REC\n' + 'and a.BLK > 0 and a.S > 0\nand a.KF in ' + str_list_mfo + '\n' + 'and c.KF = b.KF\n' + 'group by c.NAME, a.KF, a.BLK, a.KV\n' + 'order by 2,3,4'
        print('Sql:', str_parse_sql)
        connect_to_oracle_and_execute(str_parse_sql)
        # connect_to_oracle_and_execute('select * from bars.dk')
        #        Работа с буфером обмена для текста
        #Запись:
        #1 from Tkinter import Tk
        #2 c = Tk()
        #3 c.withdraw()
        #4 c.clipboard_clear()
        
        #5 c.clipboard_append('sample text')
        copied = ''
        was = ''
        text_was = ''
        if write_to_clipboard:
            try:
                was = root.clipboard_get()
            except TclError as clipboard_error:
                print("Ошибка копирования в буфер: ", clipboard_error)
                was = 'Empty'
            copied = ' Список МФО скопирован в буфер обмена.'
            text_was = ' Было в буфере обмена: '
            root.clipboard_append(str_list_mfo)
        list_mfo_entry.delete(0, END)
        if was != '':
            list_mfo_entry.insert(0, "Список мфо: {0}{1}{2}{3}".format(str_list_mfo, copied, text_was, was))
        else:
            list_mfo_entry.insert(0, str_list_mfo)
        #6 c.update()
        #7 c.destroy()

        #Извлечение:
        #1 from Tkinter import Tk
        #2 c = Tk()
        #3 c.withdraw()
        #4 clip = c.clipboard_get()
        #5 c.update()
        #6 c.destroy()
        #7 print(clip)
        

f = Frame()
f.pack(side=LEFT, padx=10)
#entry = Entry(f)
#entry.pack(anchor=N)
to_right_button = Button(f, text=">>>", command=to_right)
to_right_button.pack(fill=X)
back_button = Button(f, text="<<<", command=back)
back_button.pack(fill=X, pady=10)
email_button = Button(f, text="Отправить почту по автопереоформлению вкладов (OUTLOOK должен быть загружен!)", command=email)
email_button.pack(fill=X, pady=20)
user_label = Label(f, text="Имя пользователя:", justify='center')
user_label.pack(fill=X, pady=5)
user_entry = Entry(f, justify='center')
user_entry.insert(0, 'user5301')
user_entry.pack(fill=X, pady=5)
pass_label = Label(f, text="Пароль:", justify='center')
pass_label.pack(fill=X, pady=5)
pass_entry = Entry(f, show='*', justify='center')
pass_entry.insert(0, 'p')
pass_entry.pack(fill=X, pady=5)
parse_button = Button(f, text="Список МФО, запрос (Пользователь и пароль должны быть правильными!)", command=parse)
parse_button.pack(fill=X, pady=20)
list_mfo_entry = Entry(f, justify='center')
list_mfo_entry.insert(0, '')
list_mfo_entry.pack(fill=X, pady=5)

error_label = Label(f, text="")
error_label.pack(fill=X, pady=10)

fr = Frame()
fr.pack(side=LEFT, padx=10)
right_lbox = Listbox(fr, selectmode=EXTENDED, width=20, height=26, font='Verdana 16')
right_lbox.pack(fill=X)
rscroll = Scrollbar(command=right_lbox.yview)
rscroll.pack(side=LEFT, fill=Y)
right_lbox.config(yscrollcommand=rscroll.set)

# в rushki список областей
for ru in rushki:
    lbox_left.insert(END, ru)

root.mainloop()
