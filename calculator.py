from logging import root
from tkinter import *


class Calculator:
    def __init__(self, window):
        window.title('Calculator')
        window.geometry('357x420+0+0')
        window.config(bg='black')
        window.resizable(False, False)

        self.equation = StringVar()
        self.entry_value = ''
        Entry(width=17, bg='#fff', font=('Arial Bold', 28),
              textvariable=self.equation).place(x=0, y=0)

        xPlace = 0
        yPlace = 50
        symbols = ['(', ')', '%', '1', '2', '3', '4', '5', '6', '7',
                   '8', '9', '0', '.', '+', '-', '/', 'x', '=', 'C']
        for i in range(1, 21):
            Button(width=11, height=4, text=symbols[i-1], relief='flat', bg='white',
                   command=lambda: self.show('')).place(x=xPlace, y=yPlace)
            xPlace += 90
            if(i % 4 == 0):
                yPlace += 75
                xPlace = 0

    def show(self, value):
        self.entry_value += str(value)
        self.equation.set(self.entry_value)

    def clear(self):
        self.entry_value = ''
        self.equation.set(self.entry_value)

    def solve(self):
        result = eval(self.entry_value)
        self.equation.set(result)


root = Tk()
calculator = Calculator(root)
root.mainloop()
