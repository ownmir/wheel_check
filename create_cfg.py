from django.template import Context, Template
from tkinter import *
from django.conf import settings
from django.template.engine import Engine

settings.configure()
root = Tk()
f_top = Frame()  # root можно не указывать
f_mid = Frame()
f_bot = Frame()
name_file_l = Label(f_top, padx=5, text='File name')

name_file_e = Entry(f_top, width=10, bg='#ffffff', justify='center')

title_l = Label(f_mid, padx=5, text='Title')
title_e = Entry(f_mid, width=10, bg='#ffffff', justify='center')

base_l = Label(f_mid, padx=5, text='База')
base_e = Entry(f_mid, width=10, bg='#ffffff', justify='center')

def generate():
    template = Template("title {{ my_title }}\nbase {{ base }}", engine=Engine())
    title = title_e.get()
    base = base_e.get()
    context = Context({"my_title": title, "base": base})
    edit_text.insert(INSERT, template.render(context))

generate_b = Button(f_mid, width=10, bg='#99ccff', command=generate, text='Generate')

def open_file():
    edit_text.delete(1.0, END)
    with open(name_file_e.get(), 'r', encoding='utf-8') as edit_file:
        for line in edit_file:
            edit_text.insert(INSERT, line)

open_b = Button(f_top, width=10, bg='#6699ff', command=open_file, text='Open')


def save_file():
    with open(name_file_e.get(), 'w', encoding='utf-8') as save_file:
        save_file.write(edit_text.get(1.0, END))

save_b = Button(f_top, width=10, bg='#6699ff', command=save_file, text='Save')
f_top.pack(ipadx=5, padx=5, pady=1)
f_mid.pack(ipadx=5, padx=5)
f_bot.pack()
name_file_l.pack(side=LEFT)
name_file_e.pack(side=LEFT)
open_b.pack(side=LEFT, padx=5)
save_b.pack(side=LEFT, padx=5)
title_l.pack(side=LEFT)
title_e.pack(side=LEFT)
base_l.pack(side=LEFT)
base_e.pack(side=LEFT)
generate_b.pack()
edit_text = Text(f_bot)

scroll_y = Scrollbar(f_bot, command=edit_text.yview)
scroll_y.pack(side=RIGHT, fill=Y)
edit_text.config(yscrollcommand=scroll_y.set)
scroll_x = Scrollbar(f_bot, command=edit_text.xview, orient=HORIZONTAL)
scroll_x.pack(side=BOTTOM, fill=X)
edit_text.config(xscrollcommand=scroll_x.set)
edit_text.pack(side=LEFT)


root.mainloop()
