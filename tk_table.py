from tkinter import *

root = Tk()

c = Canvas(root, width=100, height=50, bg='white')
c.create_rectangle(2, 2, 100, 50)
c.create_text(50, 25, text="Hello World,\nPython\nand Tk",
                justify=CENTER, font="Verdana 10")
c.grid(row=0, column=0)

c01 = Canvas(root, width=100, height=50, bg='#ccffff')
c01.create_rectangle(2, 2, 100, 50)
c01.create_text(50, 25, text="0 1",
                justify=CENTER, font="Verdana 10")
c01.grid(row=0, column=1)

c10 = Canvas(root, width=100, height=50, bg='#ccffff')
c10.create_rectangle(2, 2, 100, 50)
c10.create_text(50, 25, text="1 0",
                justify=CENTER, font="Verdana 10")
c10.grid(row=1, column=0)

c11 = Canvas(root, width=100, height=50, bg='white')
c11.create_rectangle(2, 2, 100, 50)
c11.create_text(12, 9, text="1 1",
                justify=CENTER, font="Verdana 10")
c11.grid(row=1, column=1)


def func_ok():
    pass


ButtonOk = Button(c11, width=4, text='Ok', command=func_ok)
ButtonOk.pack()
ButtonNo = Button(c11, width=4, text='No', command=func_ok)
ButtonNo.pack()
c11.create_window((4, 22), anchor="nw", window=ButtonOk)
c11.create_window((61, 22), anchor="nw", window=ButtonNo)

root.mainloop()