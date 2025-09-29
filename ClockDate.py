from tkinter import *
import datetime

def update():
    clock = datetime.datetime.now().strftime("%H:%M:%S %p")
    clock_lable.config(text=clock)

    day = datetime.datetime.now().strftime("%A")
    day_lable.config(text=day)

    date = datetime.datetime.now().strftime("%Y-%m-%d")
    date_lable.config(text=date)


    window.after(1000, update)


window = Tk()

clock_lable = Label(window, text='', font=('Arial', 50), fg='green', bg='black')
clock_lable.pack()

day_lable = Label(window, text='', font=("Monotype Corsiva", 50))
day_lable.pack()

date_lable = Label(window, text='', font=("Monotype Corsiva", 50))
date_lable.pack()


update()

window.mainloop()