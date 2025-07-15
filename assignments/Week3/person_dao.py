import pymysql

class Person:
    def __init__(self, name="", gender="", dob="", location=""):
        self.name = name
        self.gender = gender
        self.dob = dob
        self.location = location

    def __str__(self):
        return f'Name: {self.name}, Location: {self.location}'


class Db_operations:
    def __init__(self):
        self.db_name = 'test2'

    def connect_db(self, with_db=True):
        try:
            connection = pymysql.connect(
                host='localhost',
                port=3306,
                user='root',
                password='root',
                database=self.db_name if with_db else None,
                charset='utf8'
            )
            print('DB connected')
            return connection
        except Exception as e:
            print(f'DB connection failed: {e}')
            return None

    def disconnect_db(self, connection):
        try:
            connection.close()
            print('DB disconnected')
        except Exception as e:
            print(f'Error while disconnecting DB: {e}')

    def create_db(self):
        connection = self.connect_db(with_db=False)
        if connection:
            cursor = connection.cursor()
            cursor.execute(f'CREATE DATABASE IF NOT EXISTS {self.db_name}')
            print('Database created')
            cursor.close()
            self.disconnect_db(connection)

    def create_table(self):
        connection = self.connect_db()
        if connection:
            cursor = connection.cursor()
            query = """
                CREATE TABLE IF NOT EXISTS people (
                    id INT PRIMARY KEY AUTO_INCREMENT,
                    name VARCHAR(32) NOT NULL,
                    gender CHAR(1) CHECK (gender IN ('m','M','f','F')),
                    location VARCHAR(32),
                    dob DATE
                );
            """
            cursor.execute(query)
            print('Table created')
            cursor.close()
            self.disconnect_db(connection)

    def insert_row(self, person):
        query = 'INSERT INTO people(name, gender, location, dob) VALUES (%s, %s, %s, %s);'
        connection = self.connect_db()
        cursor = connection.cursor()
        cursor.execute(query, (person.name, person.gender, person.location, person.dob))
        connection.commit()
        cursor.close()
        self.disconnect_db(connection)
        return self.get_latest_row_id()

    def update_row(self, data):
        query = 'UPDATE people SET name=%s, gender=%s, location=%s, dob=%s WHERE id=%s'
        connection = self.connect_db()
        cursor = connection.cursor()
        cursor.execute(query, data)
        connection.commit()
        cursor.close()
        self.disconnect_db(connection)

    def delete_row(self, id):
        query = f'DELETE FROM people WHERE id = {int(id)}'
        connection = self.connect_db()
        cursor = connection.cursor()
        count = cursor.execute(query)
        connection.commit()
        cursor.close()
        self.disconnect_db(connection)
        if count == 0:
            print(f'Person with id = {id} not found')
        else:
            print(f'Person with id = {id} deleted')

    def search_row(self, id):
        row = None
        query = f'SELECT * FROM people WHERE id = {int(id)}'
        connection = self.connect_db()
        cursor = connection.cursor()
        count = cursor.execute(query)
        if count > 0:
            row = cursor.fetchone()
            print('Person found:', row)
        else:
            print(f'Person with id = {id} not found')
        cursor.close()
        self.disconnect_db(connection)
        return row

    def list_all_rows(self):
        query = 'SELECT * FROM people;'
        connection = self.connect_db()
        cursor = connection.cursor()
        count = cursor.execute(query)
        rows = cursor.fetchall() if count > 0 else []
        cursor.close()
        self.disconnect_db(connection)
        return rows

    def get_latest_row_id(self):
        query = 'SELECT MAX(id) FROM people;'
        connection = self.connect_db()
        cursor = connection.cursor()
        cursor.execute(query)
        id = cursor.fetchone()[0]
        cursor.close()
        self.disconnect_db(connection)
        return id
