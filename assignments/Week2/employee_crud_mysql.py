import pymysql

DB_NAME = "crudtest1"
TABLE_NAME = "employees"

def connect_server():
    try:
        connection = pymysql.connect(
            host="localhost",
            user="root",
            password="root",
            port=3306,
            charset="utf8"
        )
        return connection
    except Exception as e:
        print(f"Server connection failed: {e}")
        return None

def connect_db():
    try:
        connection = pymysql.connect(
            host="localhost",
            user="root",
            password="root",
            database=DB_NAME,
            port=3306,
            charset="utf8"
        )
        return connection
    except Exception as e:
        print(f"Database connection failed: {e}")
        return None

def disconnect_db(connection):
    try:
        if connection:
            connection.close()
    except Exception as e:
        print(f"DB disconnection failed: {e}")

# Create database if not exists
def create_db():
    query = f"CREATE DATABASE IF NOT EXISTS {DB_NAME}"
    conn = connect_server()
    if conn:
        try:
            cursor = conn.cursor()
            cursor.execute(query)
            print(f"Database '{DB_NAME}' ensured.")
            cursor.close()
        except Exception as e:
            print(f"Database creation failed: {e}")
        finally:
            disconnect_db(conn)

# Create table if not exists
def create_table():
    query = f'''
    CREATE TABLE IF NOT EXISTS {TABLE_NAME} (
        id INT PRIMARY KEY AUTO_INCREMENT,
        name VARCHAR(50) NOT NULL,
        designation VARCHAR(30),
        phone_number BIGINT UNIQUE,
        salary FLOAT,
        commission FLOAT DEFAULT 0,
        years_of_experience TINYINT,
        technology VARCHAR(30) NOT NULL
    )
    '''
    conn = connect_db()
    if conn:
        try:
            cursor = conn.cursor()
            cursor.execute(query)
            print(f"Table '{TABLE_NAME}' ensured.")
            cursor.close()
        except Exception as e:
            print(f"Table creation failed: {e}")
        finally:
            disconnect_db(conn)

def read_all_employees():
    query = f'SELECT * FROM {TABLE_NAME}'
    connection = connect_db()
    try:
        cursor = connection.cursor()
        cursor.execute(query)
        rows = cursor.fetchall()
        for row in rows:
            print(row)
        cursor.close()
    except Exception as e:
        print(f'Retrieving rows failed: {e}')
    finally:
        disconnect_db(connection)

def search_employee():
    id = int(input('Enter employee ID to search: '))
    query = f'SELECT * FROM {TABLE_NAME} WHERE id = %s'
    connection = connect_db()
    try:
        cursor = connection.cursor()
        cursor.execute(query, (id,))
        rows = cursor.fetchall()
        if rows:
            for row in rows:
                print(row)
        else:
            print("No employee found.")
        cursor.close()
    except Exception as e:
        print(f'Search failed: {e}')
    finally:
        disconnect_db(connection)

def read_employee_details():
    name = input('Enter employee name: ')
    designation = input('Enter employee designation: ')
    phone_number = int(input('Enter phone number: '))
    salary = float(input('Enter salary: '))
    commission = float(input('Enter commission: '))
    experience = int(input('Enter years of experience: '))
    technology = input('Enter technology: ')
    return (name, designation, phone_number, salary, commission, experience, technology)

def insert_employee():
    employee = read_employee_details()
    query = f'''
    INSERT INTO {TABLE_NAME}
    (name, designation, phone_number, salary, commission, years_of_experience, technology)
    VALUES (%s, %s, %s, %s, %s, %s, %s)
    '''
    conn = connect_db()
    try:
        cursor = conn.cursor()
        cursor.execute(query, employee)
        conn.commit()
        print("Employee inserted.")
        cursor.close()
    except Exception as e:
        print(f"Insertion failed: {e}")
    finally:
        disconnect_db(conn)

def update_employee():
    id = int(input("Enter employee ID to update: "))
    salary = float(input("Enter new salary: "))
    experience = int(input("Enter new years of experience: "))
    query = f'''
    UPDATE {TABLE_NAME}
    SET salary = %s, years_of_experience = %s
    WHERE id = %s
    '''
    conn = connect_db()
    try:
        cursor = conn.cursor()
        rows = cursor.execute(query, (salary, experience, id))
        conn.commit()
        if rows:
            print(f"Employee {id} updated.")
        else:
            print("Employee not found.")
        cursor.close()
    except Exception as e:
        print(f"Update failed: {e}")
    finally:
        disconnect_db(conn)

def delete_employee():
    id = int(input("Enter employee ID to delete: "))
    query = f'DELETE FROM {TABLE_NAME} WHERE id = %s'
    conn = connect_db()
    try:
        cursor = conn.cursor()
        rows = cursor.execute(query, (id,))
        conn.commit()
        if rows:
            print(f"Employee {id} deleted.")
        else:
            print("Employee not found.")
        cursor.close()
    except Exception as e:
        print(f"Deletion failed: {e}")
    finally:
        disconnect_db(conn)
def initialize_database():
    create_db()
    create_table()
