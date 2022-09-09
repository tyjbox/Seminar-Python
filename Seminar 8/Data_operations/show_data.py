 
import tkinter as tk
from tkinter import *
from tkinter import scrolledtext


def run_window4():

    window4 = tk.Tk()


    window4.geometry('450x400+100+200')
    window4.title('СПИСОК КОНТАКТОВ')
    window4.config(background='coral')
    window4.resizable(False, False)

    frame = Frame(window4)
    frame.pack()
    
    text = scrolledtext.ScrolledText(frame,  
                    width = 50,
                    height=15,
                    foreground='brown',
                    font=('Arial', 11, 'italic', 'bold'),
                    )
    text.pack()

    def show_contact_list():
        with open('phone_book.txt', 'r', encoding='utf-8') as file:
            content = file.read()
            for values in content:
                text.insert(END, values)
      
    btn = tk.Button(window4,text='ПОКАЗАТЬ СПИСОК КОНТАКТОВ',
                    activebackground='peach puff',
                    fg='brown',
                    font=('Arial', 11, 'italic', 'bold'),
                    relief=tk.RAISED,
                    bd=10,
                    width=40,
                    height=2,
                    anchor='s',
                    command= show_contact_list)
    btn.place(x=33, y=280)

    window4.mainloop()




    # _____________________________________________________________

    # НЕ ПОЛУЧАЕТСЯ СДЕЛАТЬ ВЫВОД СПИСКА КОНТАКТОВ ЧЕРЕЗ LISTBOX, Т.К. ВЫВОДИТ КОНТАКТЫ ПО ОДНОЙ БУКВЕ В СТОЛБИК!!!!!!!!


    # window4 = tk.Tk()

    # window4.geometry('450x400+100+200')
    # window4.title('СПИСОК КОНТАКТОВ')
    # window4.config(background='coral')
    # window4.resizable(False, False)

    # frame = Frame(window4)
    # frame.pack()
    # scrollbar = Scrollbar(frame)
    # scrollbar.pack(side="right", fill="y")

    # listbox = Listbox(frame,  
    #                 width = 63,
    #                 height=15,
    #                 yscrollcommand = scrollbar.set)
    # listbox.pack()

    # def show_contact_list():
    #     with open('phone_book.txt', 'r', encoding='utf-8') as file:
    #         content = file.read()
    #         for values in content:
    #             listbox.insert(END, values)#
      
    # btn = tk.Button(window4,text='ПОКАЗАТЬ СПИСОК КОНТАКТОВ',
    #                 activebackground='peach puff',
    #                 fg='brown',
    #                 font=('Arial', 11, 'italic', 'bold'),
    #                 relief=tk.RAISED,
    #                 bd=10,
    #                 width=40,
    #                 height=2,
    #                 anchor='s',
    #                 command= show_contact_list)
    # btn.place(x=33, y=280)

    # scrollbar.config(command = listbox.yview)

    # window4.mainloop()