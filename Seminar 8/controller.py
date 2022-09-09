import tkinter as tk
from tkinter import font as tkFont
from tkinter import *


from Data_operations import import_data, export_data, show_data


def run_main_window():

    window = tk.Tk()

    window.geometry('400x440+100+200')
    window.title('ТЕЛЕФОННЫЙ СПРАВОЧНИК')
    window.config(background='coral')
    window.resizable(False, False)

    arial16 = tkFont.Font(family='Arial', size=16, weight=tkFont.BOLD)
    btn1 = tk.Button(window,text='Внести новый контакт',
                    activebackground='peach puff',
                    fg='brown',
                    font=arial16,
                    relief=tk.RAISED,
                    bd=10,
                    padx=10,
                    pady=10,
                    command=import_data.run_window2)
    btn1.place(x=55, y=60)

    btn2 = tk.Button(window,text='Удалить контакт',
                    activebackground='peach puff',
                    fg='brown',
                    font=arial16,
                    relief=tk.RAISED,
                    bd=10,
                    padx=43,
                    pady=10,
                    command=export_data.run_window3)
    btn2.place(x=55, y=180)

    btn3 = tk.Button(window,text='Показать все контакты',
                    activebackground='peach puff',
                    fg='brown',
                    font=arial16,
                    relief=tk.RAISED,
                    bd=10,
                    padx=9,
                    pady=10,
                    command=show_data.run_window4)
    btn3.place(x=55, y=300)


    window.mainloop()