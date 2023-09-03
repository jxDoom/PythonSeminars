import json
import time

phone_book = {"Дядя Петя": {'Номер телефона': '9998881234', 'Дополнительный номер': '9997772233', 'Комментарий': 'Дядя'}, 
              "Тетя Песя": {'Номер телефона': '9998881444', 'Дополнительный номер': '', 'Комментарий': ''}}

#phone_book = {}

def save():
    with open('PhoneBook.json', 'w', encoding = 'utf-8') as fh:
        fh.write(json.dumps(phone_book, ensure_ascii=False))
    print('Контакт сохранен\n')
def load():
    with open('PhoneBook.json', 'r', encoding = 'utf-8') as fh:
        phone_book = json.load(fh)
    return phone_book

def show_all():
    if phone_book:
        for key, values in phone_book.items():
            if (lambda x: x[1] == '', values.items()):
                tmp = dict(filter(lambda x: x[1] != '', values.items()))
                print(f'{key}: {tmp}')
    else:
        print('Телефонный справочник пуст')
        

def search_contact():
    name = input("Введите имя для поиска: ")
    if name in phone_book:
        print(name, phone_book[name])

def add_new_contact():
    name = input('Введите имя: ')
    num1 = input('Введите номер: ')
    print('Если дополнительных параметров нет, пропускаем, нажимая клавишу Enter')
    num2 = input('Дополнительный номер: ')
    comment = input('Дополнительный комментарий к контакту: ')
    phone_book[name] = {'Номер телефона': num1, 'Дополнительный номер': num2, 'Комментарий': comment}
    print('Контакт добавлен. Сохранить?')
    if input().lower() == 'да':
        save()
    else:
        print('Контакт не сохранен\n')
    
def change_contact():
    name = input("Введите имя контакта, которого хотите изменить: ")
    if name in phone_book:
        
        num1 = input('Введите номер: ')
        print('Если дополнительных параметров нет, пропускаем, нажимая клавишу Enter')
        num2 = input('Дополнительный номер: ')
        comment = input('Дополнительный комментарий к контакту: ')
        zip([],[num1, num2, comment])

        # print('Контакт изменен. Сохранить?')
        # if input().lower() == 'да':
        #     save()
        # else:
        #     print('Контакт не сохранен\n')
    else:
        print(f'Контакт с именем {name} в Вашем справочнике не существует\n')

def delete_contact():
    name = input("Введите имя контакта, которого надо удалить: ")
    if name in phone_book:
        del phone_book[name]
        print('Удаление успешно завершено\n')
    else:
        print(f'Контакт с именем {name} в Вашем справочнике не существует\n')

def start():
    flag = True
    while flag:
        time.sleep(2)
        answer = input('Phone book:\n'
                       '1. Показать все контакты\n'
                       '2. Найти контакт\n'
                       '3. Добавить контакт\n'
                       '4. Изменить контакт\n'
                       '5. Удалить контакт\n'
                       '6. Импортировать контакт\n'
                       '0. Выход\n')

        match answer:
            case '0':
                flag = False
            case '1':
                show_all()
            case '2':
                search_contact()
            case '3':                                
                add_new_contact()
            case '4':
                change_contact()
            case '5':
                delete_contact()
            case _:
                print('Введите цифру заново!\n')
                

start()
