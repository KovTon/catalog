import sqlite3


def add_user(first_name, middle_name, last_name, email, age):
    connection = sqlite3.connect('pet_base.db')
    cursor = connection.cursor()
    cursor.execute(f"""
                   INSERT INTO Users (first_name,
                                    middle_name,
                                    last_name,
                                    email, age)
                   
                   VALUES ( '{first_name}',
                   '{middle_name}',
                   '{last_name}',
                   '{email}',
                   {age})
                   """)
    connection.commit()
    connection.close()


def delet_user(queri):
    connection = sqlite3.connect('pet_base.db')
    cursor = connection.cursor()
    cursor.execute(f"DELETE FROM Users WHERE first_name LIKE'%{queri}%' OR email LIKE '%{queri}%' OR age LIKE '{queri}'")
    connection.commit()
    connection.close()


def get_user(queri):
    connection = sqlite3.connect('pet_base.db')
    cursor = connection.cursor()
    cursor.execute(f"SELECT * FROM Users WHERE first_name LIKE'%{queri}%' OR email LIKE '%{queri}%' OR age LIKE '{queri}' ")
    search_results = cursor.fetchall()

    # Выводим результаты
    if len(search_results) != 0:
        for _ in search_results:
            print(_)
    else:
        print('Запись не обнаружена.')

    connection.commit()
    connection.close()


functions = '''
1. Добавить человека.
2. Найти человека.
3. Удалить человека.
4. Выйти
'''
choice = int()

while choice != 4:
    print(functions)
    try:
        print('Введите число')
        choice = int(input())
    except ValueError:
        print('Введите число от 1 до 4. Например: 1')

    # if type(choice) is not int:
        # print('Введите число. Например: 1')

    if choice == 1:
        print('Добавляем информацию о пользователе в базу.')
        first_name = input('Введите имя: ')
        middle_name = input('Введите фамилию: ')
        last_name = input('Введите отчество: ')
        email = input('Введите email: ')
        age = int(input('Введите возраст: '))
        add_user(first_name, middle_name, last_name, email, age)
        print('Данные добавлены')

    elif choice == 2:
        queri = input('Введите имя, email или возраст для поиска: ')
        get_user(queri)

    elif choice == 3:
        queri = input('Введите параметр точные данные для удаления: ')
        print(delet_user(queri))
        print(f"Строка с полем {queri} удалена.")
