from tkinter import *

def change():
    if var.get() == 0:
        label['bg'] = 'red'
    elif var.get() == 1:
        label['bg'] = 'green'
    elif var.get() == 2:
        label['bg'] = 'blue'

root = Tk()

var = IntVar()
var.set(0)

red = Radiobutton(text="Red", variable=var, value=0)
green = Radiobutton(text="Green", variable=var, value=1)
blue = Radiobutton(text="Blue", variable=var, value=2)
button = Button(text="Изменить", command=change)
label = Label(width=20, height=10)
red.pack()
green.pack()
blue.pack()
button.pack()
label.pack()

cvar1 = BooleanVar()
cvar1.set(0)
c1 = Checkbutton(text="First", variable=cvar1, onvalue=1, offvalue=0)
c1.pack(anchor=W)
 
cvar2 = BooleanVar()
cvar2.set(0)
c2 = Checkbutton(text="Second", variable=cvar2, onvalue=1, offvalue=0)
c2.pack(anchor=W)

def tel():
    tel_label['text'] = svar.get()

svar = StringVar()
svar.set('+380630631010')
f_left = Frame(root)
f_right = Frame(root)
f_left.pack(side=LEFT)
va = Radiobutton(f_left, text="Вася", variable=svar, value='+380630631010', indicatoron=0, command=tel) 
pe = Radiobutton(f_left, text="Петя", variable=svar, value='+380505031010', indicatoron=0, command=tel)
ma = Radiobutton(f_left, text="Маша", variable=svar, value='+380670671010', indicatoron=0, command=tel)
f_right.pack(side=LEFT)
tel_label = Label(f_right, width=20, height=20)
tel_label['text'] = svar.get()

va.pack()
pe.pack()
ma.pack()
tel_label.pack(side=LEFT)


root.mainloop()
