from tkinter import *
 
root = Tk()
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
b_red.pack(side=LEFT)

def orange_set_le():
    l_color['text'] = 'Color: orange'
    l_color['fg'] = '#ff7d00'
    e_code_color.delete(0, 'end')
    e_code_color.insert(0, '#ff7d00')

b_orange = Button(width=25, bg='#ff7d00', command=orange_set_le)
b_orange.pack(side=LEFT)

def yellow_set_le():
    l_color['text'] = 'Color: yellow'
    l_color['fg'] = '#000000'
    e_code_color.delete(0, 'end')
    e_code_color.insert(0, '#ffff00')

b_yellow = Button(width=25, bg='#ffff00', command=yellow_set_le)
b_yellow.pack(side=LEFT)

def green_set_le():
    l_color['text'] = 'Color: green'
    l_color['fg'] = '#00ff00'
    e_code_color.delete(0, 'end')
    e_code_color.insert(0, '#00ff00')

b_green = Button(width=25, bg='#00ff00', command=green_set_le)
b_green.pack(side=LEFT)

def blue_set_le():
    l_color['text'] = 'Color: blue'
    l_color['fg'] = '#007dff'
    e_code_color.delete(0, 'end')
    e_code_color.insert(0, '#007dff')

b_blue = Button(width=25, bg='#007dff', command=blue_set_le)
b_blue.pack(side=LEFT)

def dark_blue_set_le():
    l_color['text'] = 'Color: dark blue'
    l_color['fg'] = '#0000ff'
    e_code_color.delete(0, 'end')
    e_code_color.insert(0, '#0000ff')

b_dark_blue = Button(width=25, bg='#0000ff', command=dark_blue_set_le)
b_dark_blue.pack(side=LEFT)

def purple_set_le():
    l_color['text'] = 'Color: purple'
    l_color['fg'] = '#7d00ff'
    e_code_color.delete(0, 'end')
    e_code_color.insert(0, '#7d00ff')

b_purple = Button(width=25, bg='#7d00ff', command=purple_set_le)
b_purple.pack(side=LEFT)
root.mainloop()

