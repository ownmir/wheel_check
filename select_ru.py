from tkinter import *
from config import rushki

root = Tk()
root.title("Выбор РУ")

lbox_left = Listbox(selectmode=EXTENDED, width=20, height=26, font='Verdana 16')
lbox_left.pack(side=LEFT)
scroll = Scrollbar(command=lbox_left.yview)
scroll.pack(side=LEFT, fill=Y)
lbox_left.config(yscrollcommand=scroll.set)

def to_right():
    print('lbox_left.curselection()', lbox_left.curselection(), 'lbox_left.get(lbox_left.curselection())', lbox_left.get(lbox_left.curselection()))
    right_lbox.insert(END, lbox_left.get(lbox_left.curselection()))
    lbox_left.delete(lbox_left.curselection())

def back():
    lbox_left.insert(END, right_lbox.curselection())
    right_lbox.delete(right_lbox.curselection())

f = Frame()
f.pack(side=LEFT, padx=10)
#entry = Entry(f)
#entry.pack(anchor=N)
to_right_button = Button(f, text=">>>", command=to_right)
to_right_button.pack(fill=X)
back_button = Button(f, text="<<<", command=back)
back_button.pack(fill=X)

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
