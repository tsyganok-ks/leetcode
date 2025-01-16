import psycopg2

def main():
    # connect
    conn = psycopg2.connect(database = 'leetcode', user = 'postgres', password = 'admin')
    conn.autocommit = True
    cursor = conn.cursor()

    # create table
    create_table_query = '''CREATE TABLE World (
                                name varchar(255), 
                                continent varchar(255), 
                                area int, 
                                population int, 
                                gdp bigint); '''
    cursor.execute(create_table_query)

    # insert into table
    cursor.execute('''INSERT INTO World (name, continent, area, population, gdp) values ('Afghanistan', 'Asia', '652230', '25500100', '20343000000')''')
    cursor.execute('''INSERT INTO World (name, continent, area, population, gdp) values ('Albania', 'Europe', '28748', '2831741', '12960000000')''')
    cursor.execute('''INSERT INTO World (name, continent, area, population, gdp) values ('Algeria', 'Africa', '2381741', '37100000', '188681000000')''')
    cursor.execute('''INSERT INTO World (name, continent, area, population, gdp) values ('Andorra', 'Europe', '468', '78115', '3712000000')''')
    cursor.execute('''INSERT INTO World (name, continent, area, population, gdp) values ('Angola', 'Africa', '1246700', '20609294', '100990000000')''')

    # main Task
    cursor.execute('''SELECT name, population, area FROM World
                        WHERE area >= 3000000 OR population >= 25000000;''')

    for answ in cursor.fetchall():
        print(answ)

    # delete table
    cursor.execute('''DROP TABLE World;''')

    # close DB
    conn.close()


if __name__ == '__main__':
    main()