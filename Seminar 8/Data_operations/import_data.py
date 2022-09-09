import tkinter as tk
from tkinter import *
from tkinter import messagebox as mb
from Data_operations import show_data


def run_window2():
   

    window2 = tk.Tk()


    window2.geometry('450x400+100+200')
    window2.title('ВНЕСТИ НОВЫЙ КОНТАКТ')
    window2.config(background='coral')
    window2.resizable(False, False)

    lable_1 = tk.Label(window2, text='Введите имя',
                        background='coral',
                        foreground='brown',
                        font=('Arial', 11, 'italic', 'bold'),
                        width=20,
                        height=3,
                        padx=30,
                        pady=5,
                        anchor='w',
                        ).grid(row=0,column=1)                
    first_name_entry = tk.Entry(window2,
                    fg='brown',
                    font=('Arial', 11, 'italic', 'bold'),
                    )
    first_name_entry.grid(row=0,column=2)


    lable_2 = tk.Label(window2, text='Введите фамилию',
                        background='coral',
                        foreground='brown',
                        font=('Arial', 11, 'italic', 'bold'),
                        width=20,
                        height=3,
                        padx=30,
                        pady=5,
                        anchor='w',
                        ).grid(row=1,column=1)  
    last_name_entry = tk.Entry(window2,
                    fg='brown',
                    font=('Arial', 11, 'italic', 'bold'),
                    )
    last_name_entry.grid(row=1,column=2)


    lable_3 = tk.Label(window2, text='Введите номер телефона',
                        background='coral',
                        foreground='brown',
                        font=('Arial', 11, 'italic', 'bold'),
                        width=20,
                        height=3,
                        padx=30,
                        pady=5,
                        anchor='w',
                        ).grid(row=2,column=1)                         
    phone_number_entry = tk.Entry(window2,
                    fg='brown',
                    font=('Arial', 11, 'italic', 'bold'),
                    )  
    phone_number_entry.grid(row=2,column=2)


    lable_4 = tk.Label(window2, text='Введите описание',
                        background='coral',
                        foreground='brown',
                        font=('Arial', 11, 'italic', 'bold'),
                        width=20,
                        height=3,
                        padx=30,
                        pady=5,
                        anchor='w',
                        ).grid(row=3,column=1)
    description_entry = tk.Entry(window2,
                    fg='brown',
                    font=('Arial', 11, 'italic', 'bold'),
                    )                       
    description_entry.grid(row=3,column=2)


    def import_contact() -> None:   

        text_1 = first_name_entry.get()
        text_2 = last_name_entry.get()
        text_3 = phone_number_entry.get()
        text_4 = description_entry.get()
        contact =[text_1 + ' ' + text_2 + '__' + text_3 + '__' +  text_4] 
       
        with open('phone_book.txt', 'a', encoding='utf-8') as file:
            for item in contact: 
                file.write('{}\n'.format(item))
                mb.showinfo('СОХРАНЕНИЕ', 'Контактакт успешно сохранен!')


    btn = tk.Button(window2,text='ЗАПИСАТЬ',
                    activebackground='peach puff',
                    fg='brown',
                    font=('Arial', 11, 'italic', 'bold'),
                    relief=tk.RAISED,
                    bd=10,
                    width=40,
                    height=2,
                    anchor='s',
                    command=import_contact)
                                   
    btn.place(x=33, y=280)


    window2.grid_columnconfigure(1, minsize=275)
 
    window2.mainloop()