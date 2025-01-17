import psycopg2

def main():
    # connect
    conn = psycopg2.connect(database = 'leetcode', user = 'postgres', password = 'admin')
    conn.autocommit = True
    cursor = conn.cursor()

    # create table
    create_table_query = '''CREATE TABLE Views
                          (article_id int, 
                          author_id int, 
                          viewer_id int, 
                          view_date date);'''
    cursor.execute(create_table_query)

    # insert into table
    cursor.execute('''INSERT INTO Views (article_id, author_id, viewer_id, view_date) values ('1', '3', '5', '2019-08-01')''')
    cursor.execute('''INSERT INTO Views (article_id, author_id, viewer_id, view_date) values ('1', '3', '6', '2019-08-02')''')
    cursor.execute('''INSERT INTO Views (article_id, author_id, viewer_id, view_date) values ('2', '7', '7', '2019-08-01')''')
    cursor.execute('''INSERT INTO Views (article_id, author_id, viewer_id, view_date) values ('2', '7', '6', '2019-08-02')''')
    cursor.execute('''INSERT INTO Views (article_id, author_id, viewer_id, view_date) values ('4', '7', '1', '2019-07-22')''')
    cursor.execute('''INSERT INTO Views (article_id, author_id, viewer_id, view_date) values ('3', '4', '4', '2019-07-21')''')
    cursor.execute('''INSERT INTO Views (article_id, author_id, viewer_id, view_date) values ('3', '4', '4', '2019-07-21')''')

    # main Task
    cursor.execute('''SELECT DISTINCT author_id AS id FROM Views
                        WHERE author_id = viewer_id ORDER BY author_id ASC;''')

    for answ in cursor.fetchall():
        print(answ)

    # delete table
    cursor.execute('''DROP TABLE Views;''')

    # close DB
    conn.close()


if __name__ == '__main__':
    main()