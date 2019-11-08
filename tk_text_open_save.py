from tkinter import *
 
root = Tk()
f_top = Frame() # root можно не указывать
f_bot = Frame()
name_file_l = Label(f_top, width=20, text='File name')

name_file_e = Entry(f_top, width=20, bg='#ffffff', justify='center')


def open_file():
    edit_text.delete(1.0, END)
    with open(name_file_e.get(), 'r', encoding='utf-8') as edit_file:
        for line in edit_file:
            edit_text.insert(INSERT, line)

open_b = Button(f_top, width=20, bg='#007dff', command=open_file, text='Open')


def save_file():
    with open(name_file_e.get(), 'w', encoding='utf-8') as save_file:
        save_file.write(edit_text.get(1.0, END))

save_b = Button(f_top, width=20, bg='#007dff', command=save_file, text='Save')
f_top.pack()
f_bot.pack()
name_file_l.pack(side=LEFT)
name_file_e.pack(side=LEFT)
open_b.pack(side=LEFT)
save_b.pack()
edit_text = Text(f_bot)

scroll_y = Scrollbar(f_bot, command=edit_text.yview)
scroll_y.pack(side=RIGHT, fill=Y)
edit_text.config(yscrollcommand=scroll_y.set)
scroll_x = Scrollbar(f_bot, command=edit_text.xview, orient=HORIZONTAL)
scroll_x.pack(side=BOTTOM, fill=X)
edit_text.config(xscrollcommand=scroll_x.set)
edit_text.pack(side=LEFT)


root.mainloop()
