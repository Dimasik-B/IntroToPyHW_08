def show_menu():
    print('1. Распечатать справочник',
          '2. Найти телефон по фамилии',
          '3. Изменить номер телефона',
          '4. Удалить запись',
          '5. Найти абонента по номеру телефона',
          '6. Добавить абонента в справочник',
          '7. Скопировать строку из файла',
          '8. Закончить работу', sep = '\n')
    choice=int(input())
    return choice

def read_txt(filename):
    phone_book=[]
    fields=['Фамилия', 'Имя', 'Телефон', 'Описание']

    with open(filename, 'r', encoding='utf-8') as phb:
        for line in phb:
            if line == '\n':
                continue
            record = dict(zip(fields, line.split(',')))
            phone_book.append(record)
    return phone_book

def write_txt(filename, phone_book):
    with open(filename, 'w', encoding='utf-8') as phout:
        for i in range(len(phone_book)):
            s = ''
            for v in phone_book[i].values():
                s += v + ','
            phout.write(f'{s[:-1]}\n')

def find_by_field(field, phone_book, item):
    if field == 'Фамилия':
        for i in range(len(phone_book)):
            if phone_book[i]['Фамилия'] == item:
                return(phone_book[i])
        return False
    elif field == 'Имя':
        for i in range(len(phone_book)):
            if phone_book[i]['Имя'] == item:
                return(phone_book[i])
        return False
    elif field == 'Телефон':
        for i in range(len(phone_book)):
            if phone_book[i]['Телефон'] == item:
                return(phone_book[i])
        return False
    elif field == 'Описание':
        for i in range(len(phone_book)):
            if phone_book[i]['Описание'] == item:
                return(phone_book[i])
        return False

def print_result(phone_book):
    print()
    for el in phone_book:
        print(*el.values())

def find_by_lastname(phone_book, last_name):
    person = find_by_field('Фамилия', phone_book, last_name)
    if person != False:
            return(person['Телефон'])
    return 'Пользователь с такой фамилией не найден'

def change_number(phone_book, last_name, new_number):
    person = find_by_field('Фамилия', phone_book, last_name)
    if person != False:
        person['Телефон'] = new_number
        return f'Номер телефона {person["Фамилия"]} {person["Имя"]} изменён'
    return 'Пользователь с такой фамилией не найден'

def delete_by_lastname(phone_book, last_name):
    person = find_by_field('Фамилия', phone_book, last_name)
    if person != False:
        phone_book.pop(phone_book.index(person))
        return f'Запись удалена: {" ".join(person.values())}'
    return 'Пользователь с такой фамилией не найден'

def find_by_number(phone_book, number):
    person = find_by_field('Телефон', phone_book, number)
    if person != False:
            return(" ".join(person.values()))
    return 'Пользователь с таким номером не найден'

def add_user(phone_book, user_data):
    fields=['Фамилия', 'Имя', 'Телефон', 'Описание']
    record = dict(zip(fields, user_data.split(',')))
    phone_book.append(record)
    print('Данные добавлены')

def copy_string_from_file(file_out, file_in, string_number):
    temp = []
    with open(file_out, 'r', encoding='utf-8') as f_out:
        for line in f_out:
            temp.append(line)
        if len(temp) < string_number or string_number < 1:
            return 'Строки с таким номером нет в файле'
    with open(file_in, 'a', encoding='utf-8') as f_in:
        f_in.write(f'{temp[string_number - 1]}\n')

def work_with_phonebook():
    choice=show_menu()
    phone_book = read_txt('phonebook.txt')

    while (choice!=8):
        if choice==1:
            print_result(phone_book)
        elif choice==2:
            last_name=input('Введите фамилию ')
            print(find_by_lastname(phone_book, last_name))
        elif choice==3:
            last_name=input('Введите фамилию ')
            new_number=input('Введите номер ')
            print(change_number(phone_book,last_name, new_number))
            write_txt('phonebook.txt', phone_book)
        elif choice==4:
            lastname=input('Введите фамилию ')
            print(delete_by_lastname(phone_book, lastname))
            write_txt('phonebook.txt', phone_book)
        elif choice==5:
            number=input('Введите номер ')
            print(find_by_number(phone_book, number))
        elif choice==6:
            user_data=input('Введите фамилию, имя, номер и описание через запятую (без пробела) ')
            add_user(phone_book, user_data)
            write_txt('phonebook.txt', phone_book)
        elif choice==7:
            file_out = input('Введите имя файла - источника ')
            file_in = input('Введите имя файла для записи ')
            string_number = int(input('Введите номер строки '))
            copy_string_from_file(file_out, file_in, string_number)
        choice=show_menu()

work_with_phonebook()