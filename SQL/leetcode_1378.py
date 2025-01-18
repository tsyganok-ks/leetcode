import psycopg2

def main():
    conn = psycopg2.connect(database = 'leetcode', user = 'postgres', password = 'admin')
    cursor = conn.cursor()

    create_table_query = '''CREATE TABLE IF NOT EXISTS Employees 
                          (id int PRIMARY KEY, 
                          name varchar(25));'''
    cursor.execute(create_table_query)

    create_table_query = '''CREATE TABLE IF NOT EXISTS EmployeeUNI 
                          (id int PRIMARY KEY, 
                          unique_id int);'''
    cursor.execute(create_table_query)

    cursor.execute('''INSERT INTO Employees (id, name) values ('1', 'Alice')''')
    cursor.execute('''INSERT INTO Employees (id, name) values ('7', 'Bob')''')
    cursor.execute('''INSERT INTO Employees (id, name) values ('11', 'Meir')''')
    cursor.execute('''INSERT INTO Employees (id, name) values ('90', 'Winston')''')
    cursor.execute('''INSERT INTO Employees (id, name) values ('3', 'Jonathan')''')

    cursor.execute('''INSERT INTO EmployeeUNI (id, unique_id) values ('3', '1')''')
    cursor.execute('''INSERT INTO EmployeeUNI (id, unique_id) values ('11', '2')''')
    cursor.execute('''INSERT INTO EmployeeUNI (id, unique_id) values ('90', '3')''')

    cursor.execute('''SELECT name, unique_id FROM Employees
                        LEFT OUTER JOIN EmployeeUNI ON Employees.id = EmployeeUNI.id''')

    for answ in cursor.fetchall():
        print(answ)

    cursor.execute('''DROP TABLE Employees;''')
    cursor.execute('''DROP TABLE EmployeeUNI;''')

    conn.close()


if __name__ == '__main__':
    main()