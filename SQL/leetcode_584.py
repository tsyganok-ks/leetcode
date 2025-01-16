import psycopg2

def main():
    # connect
    conn = psycopg2.connect(database = 'leetcode', user = 'postgres', password = 'admin')
    conn.autocommit = True
    cursor = conn.cursor()

    # create table
    create_table_query = '''CREATE TABLE Customer
                          (id int, 
                          name varchar(25), 
                          referee_id int); '''
    cursor.execute(create_table_query)

    # insert into table
    cursor.execute('''INSERT INTO Customer (id, name, referee_id) values ('1', 'Will', NULL)''')
    cursor.execute('''INSERT INTO Customer (id, name, referee_id) values ('2', 'Jane', NULL)''')
    cursor.execute('''INSERT INTO Customer (id, name, referee_id) values ('3', 'Alex', '2')''')
    cursor.execute('''INSERT INTO Customer (id, name, referee_id) values ('4', 'Bill', NULL)''')
    cursor.execute('''INSERT INTO Customer (id, name, referee_id) values ('5', 'Zack', '1')''')
    cursor.execute('''INSERT INTO Customer (id, name, referee_id) values ('6', 'Mark', '2')''')

    # main Task
    cursor.execute('''SELECT name FROM Customer
                        WHERE referee_id != 2 or referee_id IS NULL;''')

    for answ in cursor.fetchall():
        print(answ)

    # delete table
    cursor.execute('''DROP TABLE Customer;''')

    # close DB
    conn.close()


if __name__ == '__main__':
    main()