from tkinter import *
# from config import oop
# import block
 
root = Tk()
b1 = Button(text="Изменить", width=15, height=3)

def change():
    b1['text'] = "Изменено"
    b1['bg'] = '#000000'
    b1['activebackground'] = '#555555'
    b1['fg'] = '#ffffff'
    b1['activeforeground'] = '#ffffff'
    l1['bg'] = 'green'

b1.config(command=change)
l1 = Label(text="Машинное обучение", font="Arial 32")
l2 = Label(text="Распознавание образов", font=("Comic Sans MS", 24))
l1.config(bd=20, bg='#ffaaaa')
l2.config(bd=20, bg='#aaffff')
# bd=20

def take():
    l['text'] = "Выдано"

Label(text="Пункт выдачи").pack()
Button(text="Взять", command=take).pack()
l = Label(width=10, height=1)
l.pack()
l1.pack()
l2.pack()
b1.pack()
e1 = Entry(width=50)

def insert():
    if l['text'] == 'Выдано':
        e1.insert(0,l['text'] + ' ')
    else:
        e1.insert(0,"Tkinter - GUI ")

b = Button(text="Вставить", command=insert)
e1.pack()
b.pack()
l_color = Label(width=30)
e_code_color = Entry(width=30, bg='#ffffff', justify='center')

def red_set_le():
    l_color['text'] = 'Color: red'
    l_color['fg'] = '#ff0000'
    e_code_color.delete(0, 'end')
    e_code_color.insert(0, '#ff0000')

b_red = Button(width=25, bg='#ff0000', command=red_set_le)
l_color.pack()
e_code_color.pack()
b_red.pack()

def orange_set_le():
    l_color['text'] = 'Color: orange'
    l_color['fg'] = '#ff7d00'
    e_code_color.delete(0, 'end')
    e_code_color.insert(0, '#ff7d00')

b_orange = Button(width=25, bg='#ff7d00', command=orange_set_le)
b_orange.pack()

def yellow_set_le():
    l_color['text'] = 'Color: yellow'
    l_color['fg'] = '#000000'
    e_code_color.delete(0, 'end')
    e_code_color.insert(0, '#ffff00')

b_yellow = Button(width=25, bg='#ffff00', command=yellow_set_le)
b_yellow.pack()

def green_set_le():
    l_color['text'] = 'Color: green'
    l_color['fg'] = '#00ff00'
    e_code_color.delete(0, 'end')
    e_code_color.insert(0, '#00ff00')

b_green = Button(width=25, bg='#00ff00', command=green_set_le)
b_green.pack()

def blue_set_le():
    l_color['text'] = 'Color: blue'
    l_color['fg'] = '#007dff'
    e_code_color.delete(0, 'end')
    e_code_color.insert(0, '#007dff')

b_blue = Button(width=25, bg='#007dff', command=blue_set_le)
b_blue.pack()

def dark_blue_set_le():
    l_color['text'] = 'Color: dark blue'
    l_color['fg'] = '#0000ff'
    e_code_color.delete(0, 'end')
    e_code_color.insert(0, '#0000ff')

b_dark_blue = Button(width=25, bg='#0000ff', command=dark_blue_set_le)
b_dark_blue.pack()

def purple_set_le():
    l_color['text'] = 'Color: purple'
    l_color['fg'] = '#7d00ff'
    e_code_color.delete(0, 'end')
    e_code_color.insert(0, '#7d00ff')

b_purple = Button(width=25, bg='#7d00ff', command=purple_set_le)
b_purple.pack()
root.mainloop()
