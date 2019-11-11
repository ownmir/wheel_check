from tkinter import *
from config import rushki, ru_dic
import os

root = Tk()
root.title("Выбор РУ")

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
        mail.To = 'jove@ukr.net'
        mail.Subject = '!!'
        mail.HTMLBody = '<h2>Hello!</h2>'
        # attachment = 'Path'
        # mail.Attachments.Add(attachment)

        mail.Display()

f = Frame()
f.pack(side=LEFT, padx=10)
#entry = Entry(f)
#entry.pack(anchor=N)
to_right_button = Button(f, text=">>>", command=to_right)
to_right_button.pack(fill=X)
back_button = Button(f, text="<<<", command=back)
back_button.pack(fill=X, pady=10)
email_button = Button(f, text="Отправить почту по автопереоформлению вкладов", command=email)
email_button.pack(fill=X, pady=20)

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
