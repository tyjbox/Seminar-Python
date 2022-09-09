import tkinter as tk
from tkinter import *
from tkinter import messagebox as mb
import re

def run_window3():

    window3 = tk.Tk()

    window3.geometry('450x400+100+200')
    window3.title('УДАЛИТЬ КОНТАКТ')
    window3.config(background='coral')
    window3.resizable(False, False)


    lable = tk.Label(window3, text='Введите контакт для удаления',
                        background='coral',
                        foreground='brown',
                        font=('Arial', 11, 'italic', 'bold'),
                        width=20,
                        height=3,
                        padx=130,
                        pady=5,
                        anchor='center',
                        ).grid(row=0,column=1)

    input_text_entry = tk.Entry(window3,
                        width=40,
                        foreground='brown',
                        font=('Arial', 11, 'italic', 'bold'),
                        )
    input_text_entry.grid(row=10,column=1)


    def find_contact():   
       
        search_result = list()
        del_contact = input_text_entry.get()     
        with open('phone_book.txt', 'r', encoding='utf-8') as file:
            phonebook = file.readlines()
            for contact in phonebook:
                if del_contact in contact:
                    search_result.append(contact)

        if search_result != []:
            mb.showinfo('ПОИСК КОНТАКТА', 'КОНТАКТ НАЙДЕН!')                   
        else:
            mb.showinfo('ПОИСК КОНТАКТА', 'КОНТАКТ НЕ НАЙДЕН!!!')  

    btn1 = tk.Button(window3,text='НАЙТИ КОНТАКТ В СПИСКЕ ДЛЯ УДАЛЕНИЯ',
                    activebackground='peach puff',
                    fg='brown',
                    font=('Arial', 11, 'italic', 'bold'),
                    relief=tk.RAISED,
                    bd=10,
                    width=40,
                    height=2,
                    anchor='s',
                    command=find_contact) 
    btn1.place(x=33, y=150)


    def delete_contact():

        del_contact = input_text_entry.get() 

        with open('phone_book.txt', 'r', encoding='utf-8') as file:
            all_content = file.readlines()

            delete_line = del_contact 
            pattern = re.compile(re.escape(delete_line))
            with open('phone_book.txt', 'w', encoding='utf-8') as file:
                for line in  all_content:
                    result = pattern.search(line)
                    if result is None:
                        file.write(line)
            mb.showinfo('УДАЛЕНИЕ КОНТАКТА', 'КОНТАКТ УДАЛЕН!')                      

    btn2 = tk.Button(window3,text='УДАЛИТЬ НАЙДЕННЫЙ КОНТАКТА',
                    activebackground='peach puff',
                    fg='brown',
                    font=('Arial', 11, 'italic', 'bold'),
                    relief=tk.RAISED,
                    bd=10,
                    width=40,
                    height=2,
                    anchor='s',
                    command=delete_contact)
    btn2.place(x=33, y=280)

    window3.mainloop()