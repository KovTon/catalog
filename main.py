import sqlite3


def add_user(name, email, age):
    connection = sqlite3.connect('pet_base.db')
    cursor = connection.cursor()
    cursor.execute(f"INSERT INTO Users ( username, email, age) VALUES ('{name}', '{email}', {age})")
    connection.commit()
    connection.close()


def delet_user(queri):
    connection = sqlite3.connect('pet_base.db')
    cursor = connection.cursor()
    cursor.execute(f"DELETE FROM Users WHERE username = '{queri}' OR email = '{queri}' OR age = {queri} ")
    connection.commit()
    connection.close()


def get_user(queri):
    connection = sqlite3.connect('pet_base.db')
    cursor = connection.cursor()
    cursor.execute(f"SELECT * FROM Users WHERE username = '{queri}' OR email = '{queri}' OR age = {queri} ")
    search_results = cursor.fetchall()

    # Выводим результаты
    for _ in search_results:
        print(_)

    connection.commit() 
    connection.close()


functions = '''
1. Добавить человека.
2. Найти человека.
3. Удалить человека.
'''

print(functions)
choice = int(input())

if choice == 1:
    name = input('Введите имя: ')
    email = input('Введите email: ')
    age = int(input('Введите возраст: '))
    add_user(name, email, age)
    print('Данные добавлены')

elif choice == 2:
    queri = input('Введите точные данные для поиска: ')
    get_user(queri)

elif choice == 3:
    queri = input('Введите параметр точные данные для удаления: ')
    print(delet_user(queri))
    print(f"Строка с полем {queri} удалена.")
