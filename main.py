import sqlite3

with sqlite3.connect('Book.db') as db:
    cursor = db.cursor()
    query = """
    
    CREATE TABLE IF NOT EXISTS books(
        id INTEGER PRIMARY KEY,
        avtor_id INTEGER,
        book_name VARCHAR(100),
        age INTEGER,
        count INTEGER,
        cost INTEGER
    );

    CREATE TABLE IF NOT EXISTS avtors(
        id INTEGER PRIMARY KEY,
        name VARCHAR(100),
        age_born INTEGER,
        age_die INTEGER,
        city INTEGER
    )

    """
    # dict = {1:('Александр Сергеевич Пушкин', 1799, 1837, 'Москва'),2:('Фёдор Иванович Тютчев', 1803, 1873, 'Овстуг'), 3:('Фёдор Михайлович Достоевский', 1821, 1881, 'Москва'), 4:('Михаил Булгаков', 1891, 1940, 'Киев'), 5:('Иван Алексеевич Бунин', 1870, 1953, 'Воронеж'), 6:('Иван Сергеевич Тургенев', 1818, 1883, 'Орел')}

    cursor.executescript(query)
    cursor.execute("SELECT book_name, avtor_id FROM books WHERE avtor_id = 1")
    cursor.execute("SELECT book_name,cost FROM books WHERE cost = 240")
    for i in cursor.fetchall():
        print(i[0], 'Цена:' ,i[1])


def insert_books():
    global cursor, db
    avtor_id = int(input('avtor_id:'))
    book_name = input('book_name:')
    age = int(input('age:'))
    count = int(input('count:'))
    cost = int(input('cost:'))
    a = input('a:')

    book_name_arr = [book_name]
    age_arr = [age]
    count_arr = [count]
    cost_arr = [cost]
    se = 0

    while a != '':
        book_name_arr.append(book_name)
        age_arr.append(age)
        count_arr.append(count)
        cost_arr.append(cost)

        book_name = input('book_name:')
        age = int(input('age:'))
        cost = int(input('cost:'))
        count = int(input('count:'))
        a = input('a:')
        se += 1

    try:
        db = sqlite3.connect('Book.db')
        cursor = db.cursor()

        for i in range(se + 1):
            values = [avtor_id, book_name_arr[i], age_arr[i], count_arr[i], cost_arr[i]]
            cursor.execute("INSERT INTO books(avtor_id, book_name, age, count, cost) VALUES(?, ?, ?, ?, ?)", values)
        db.commit()

    except sqlite3.Error as e:
        print('Error', e)

    finally:
        cursor.close()
        db.close()
