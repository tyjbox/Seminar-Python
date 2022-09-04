from view import input_data, view_data

def import_contact():

    first_name = input_data('Введите имя: ')
    last_name = input_data('Введите фамилию: ')
    phone_number = input_data('Введите номер телефона: ')
    description = input_data('Введите описание: ')
    new_contact = f'{first_name} {last_name} {phone_number} {description}'
    view_data('Введен новый контакт: ', data=new_contact)
    
    with open('phone_book.txt', 'a', encoding='utf-8') as file:
        file.write('{}\n'.format(new_contact))
    print('Новый контакт внесен в телефонный справочник!\n')