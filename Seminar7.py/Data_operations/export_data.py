from view import input_data, view_data
import re

def delete_contact():
    find = False
    while not find:

        search_result = list()
        del_contact = input_data('Введите контакт(имя и фамилию), который хотите удалить:\n')

        with open('phone_book.txt', 'r', encoding='utf-8') as file:
            phonebook = file.readlines()
            for contact in phonebook:
                if del_contact in contact:
                    search_result.append(contact)

        if search_result != []:
            view_data(del_contact, ' - найден в списке контактов.')
            find = True

            confirm_word = bool(input_data('Введите "да", если подтверждаете операцию удаления!\n' 
                                           'Нажмите кнопку Enter, если хотите отменить операцию удаления!\n'))

            if confirm_word:

                with open('phone_book.txt', 'r', encoding='utf-8') as file:
                    all_content = file.readlines()

                    delete_line = del_contact 
                    pattern = re.compile(re.escape(delete_line))
                    with open('phone_book.txt', 'w', encoding='utf-8') as file:
                        for line in  all_content:
                            result = pattern.search(line)
                            if result is None:
                                file.write(line)
                                    
                
                    with open('phone_book.txt', "r", encoding='utf-8') as file:
                        changed_content = file.read() 
                        view_data('Удален контакт: ', del_contact)          
                        view_data('Ваш телефонный справочник после удаления выбранного контакта:\n', changed_content)

            else:
                view_data(del_contact, '- НЕ удален!\n')
        else: 
            view_data(del_contact, ' НЕ найден в списке контактов!\n')
            find = False
            break