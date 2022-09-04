from Data_operations import import_data, export_data, show_data

def start_program():
    print('Ваc приветствует Ваш телефонный справочник!')
    while True:
        right_action = False
        while not right_action:
            choose_action = input('Выберите НОМЕР действия:'
            '\n1.Внести новый контакт'
            '\n2.Удалить контакт'
            '\n3.Показать все контакты справочника\n')
            if choose_action.isdigit():
                choose_action = int(choose_action)
                if 1 <= choose_action <= 3:
                    right_action = True
                else:
                    print('Введите НОМЕР действия от 1 до 3!')
            else: 
                print('Неверный ввод!')
    
        match (choose_action):
            case 1:
                import_data.import_contact()
            case 2:
                export_data.delete_contact()
            case 3:
                show_data.show_contact_list() 