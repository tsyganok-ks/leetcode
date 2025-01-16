import psycopg2

def main():
    # connect
    conn = psycopg2.connect(database = 'leetcode', user = 'postgres', password = 'admin')
    #conn = psycopg2.connect(user = 'postgres', password = 'admin')
    conn.autocommit = True
    cursor = conn.cursor()

    # create local type
    #cursor.execute('''CREATE TYPE enum AS ENUM ('Y', 'N')''')

    # create table
    create_table_query = '''CREATE TABLE Products
                          (product_id int, 
                          low_fats enum, 
                          recyclable enum); '''
    cursor.execute(create_table_query)

    # insert into table
    cursor.execute('''INSERT INTO Products (product_id, low_fats, recyclable) values ('0', 'Y', 'N')''')
    cursor.execute('''INSERT INTO Products (product_id, low_fats, recyclable) values ('1', 'Y', 'Y')''')
    cursor.execute('''INSERT INTO Products (product_id, low_fats, recyclable) values ('2', 'N', 'Y')''')
    cursor.execute('''INSERT INTO Products (product_id, low_fats, recyclable) values ('3', 'Y', 'Y')''')
    cursor.execute('''INSERT INTO Products (product_id, low_fats, recyclable) values ('4', 'N', 'N')''')

    # main Task
    cursor.execute('''SELECT product_id FROM Products
                        WHERE low_fats = 'Y' AND recyclable = 'Y';''')
    for answ in cursor.fetchall():
        print(answ)

    # delete table
    cursor.execute('''DROP TABLE Products;''')

    # close DB
    conn.close()


if __name__ == '__main__':
    main()