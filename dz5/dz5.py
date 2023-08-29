""" Задача 38: Дополнить телефонный справочник возможностью изменения и удаления данных. 
Пользователь также может ввести имя или фамилию, и Вы должны реализовать функционал для изменения и удаления данных """
def redact_contact(phonebook, search_key):
    search_key = search_key.capitalize()
    for i in range(len(phonebook)):
        if search_key in phonebook[i].values():
            phonebook[i]['last_name'] = input("Фамилия ")
            phonebook[i]['first_name'] = input("Имя ")
            phonebook[i]['middle_name'] = input("Отчество ")
            phonebook[i]['phone_number'] = input("Номер телефона ")


def dell_contact(phonebook, searh_key):
    for i in range(len(phonebook) -1, -1, -1):
        if searh_key.capitalize() in phonebook[i].values():
            del phonebook[i]
            return


def load_file(filename):
    phonebook = []
    try:
        with open(filename, 'r', encoding= 'UTF-8') as file:
            for contact in file:
                last_name, first_name, middle_name, phone_number = contact.split(',')
                phonebook.append({
                    'last_name': last_name,
                    'first_name': first_name,
                    'middle_name': middle_name,
                    'phone_number': phone_number
                })
            print('Данные успешно загружены')
    except FileNotFoundError:
        print('Файл не найден')
    return phonebook


def search_contacts(phonebook, search_key):
    results = []
    for contact in phonebook:
        if (search_key.lower() in contact['last_name'].lower() or search_key.lower() in contact['first_name'].lower()):
            results.append(contact)
    return results



def views_contacts(phonebook):
    for index, contact in enumerate(phonebook, start=1):
        print(f"{index}. {contact['last_name']}, {contact['first_name']}, {contact['middle_name']}, {contact['phone_number']}\n")


def save_to_file(filename, phonebook):
    with open(filename, 'w', encoding= 'UTF-8') as file:
        for contact in phonebook:
            file.write(f"{contact['last_name']}, {contact['first_name']}, {contact['middle_name']}, {contact['phone_number']}\n")
    print('Данные сохранены в файле')

def add_contact(phonebook, last_name, first_name, middle_name, phone_number):
    contact = {
        'last_name': last_name,
        'first_name': first_name,
        'middle_name': middle_name,
        'phone_number': phone_number
    }
    phonebook.append(contact)
    print('Контакт добавлен')


def main():
    phonebook = []
    filename = 'contacts.txt'

    while True:
        print("1. Добавить контакт")
        print("2. Сохранить файл")
        print("3. Вывести все контакты")
        print("4. Поиск по имени/фамилии")
        print("5. Загрузить из файла")
        print("6. Изменить данные")
        print("7. Удалить данные")
        print("0. Выход")

        choice = input('Выберите действие: ')
        if choice == '1':
            last_name = input('Фамилия: ')
            first_name = input('Имя: ')
            middle_name = input('Отчество: ')
            phone_number = input('Номер телефона: ')
            add_contact(phonebook, last_name, first_name, middle_name, phone_number)
        elif choice == '2':
            save_to_file(filename, phonebook)
        elif choice == '3':
            views_contacts(phonebook)
        elif choice == '4':
            search_key = input("Введите имя или фамилию для поиска: ")
            results = search_contacts(phonebook, search_key)
            if (results):
                print('Найдены контакты: ')
                for cur_dict in results:
                    for item in cur_dict.values():
                        print(item, end='')
            else:
                print('Контактов по вашему запросу нет!')
        elif choice == '5':
            phonebook = load_file(filename)
        elif choice == '6':
            search_key = input("Введите имя или фамилию для поиска: ")
            redact_contact(phonebook, search_key)
            print("Данные изменены")
        elif choice == '7':
            search_key = input("Введите имя или фамилию для поиска: ")
            dell_contact(phonebook, search_key)
            print("Данные удалены")
        elif choice == '0':
            break
        else:
            print('Некорректный выбор. Попробуйте снова')




if __name__ == "__main__":
    main()