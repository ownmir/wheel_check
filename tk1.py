from tkinter import *
from config import oop
import block
 
root = Tk()
 
if oop:
    first_block = block.Block(root)
    first_block.setFunc('strToSortlist')
 
    second_block = block.Block(root)
    second_block.setFunc('strReverse')
else:
    e = Entry(width=20)
    b = Button(text="Преобразовать")
    l = Label(bg='black', fg='white', width=20)

    entry1 = Entry(width=20)
    entry2 = Entry(width=20)
    button_nsum = Button(text="Сумма")
    button_sub = Button(text="Разность")
    button_mul = Button(text="Произведение")
    button_div = Button(text="Деление")
    l_result = Label(bg='blue', fg='white', width=20)
 
    def strToSortlist(event):
        s = e.get()
        s = s.split()
        s.sort()
        l['text'] = ' '.join(s)
 
    

    def add(event):
        try:
            operand1 = float(entry1.get())
            operand2 = float(entry2.get())
            result = operand1 + operand2
            l_result['text'] = str(result)
            l_result['bg'] = 'blue'
        except Exception as e:
            l_result['bg'] = 'red'
            l_result['text'] = 'Ошибка!'
            print(e)
    
    def sub(event):
        try:
            operand1 = float(entry1.get())
            operand2 = float(entry2.get())
            result = operand1 - operand2
            l_result['text'] = str(result)
            l_result['bg'] = 'blue'
        except Exception as e:
            l_result['bg'] = 'red'
            l_result['text'] = 'Ошибка!'
            print(e)
    
    def mul(event):
        try:
            operand1 = float(entry1.get())
            operand2 = float(entry2.get())
            result = operand1 * operand2
            l_result['text'] = str(result)
            l_result['bg'] = 'blue'
        except Exception as e:
            l_result['bg'] = 'red'
            l_result['text'] = 'Ошибка!'
            print(e)
    
    def div(event):
        try:
            operand1 = float(entry1.get())
            operand2 = float(entry2.get())
            result = operand1 / operand2
            l_result['text'] = str(result)
            l_result['bg'] = 'blue'
        except Exception as e:
            l_result['bg'] = 'red'
            l_result['text'] = 'Ошибка!'
            print(e)
    
    b.bind('<Button-1>', strToSortlist)
    button_nsum.bind('<Button-1>', add)
    button_sub.bind('<Button-1>', sub)
    button_mul.bind('<Button-1>', mul)
    button_div.bind('<Button-1>', div)
    e.pack()
    b.pack()
    l.pack()
    entry1.pack()
    entry2.pack()
    button_nsum.pack()
    button_sub.pack()
    button_mul.pack()
    button_div.pack()
    l_result.pack()
    
root.mainloop()

