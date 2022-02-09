import sqlite3

# conn = sqlite3.connect(':memory:')
conn = sqlite3.connect('movies.db')

# create a cursor
cur = conn.cursor()

# create a table
cur.execute("""CREATE TABLE crudmovies(
        movie_name text,
        actor_name text,
        actress_name text,
        release_year text,
        director_name
    )""")

# ####### insert record into table #######
many_records = [
    ('English Vinglish', 'Adil', 'Sri Devi', '2012', 'Gauri'),
#     ('Airlift', 'Akshay', 'Nimrat', '2016', 'Rajakrishnan'),
#     ('Bhag Milkha Bhag', 'Farhan', 'Sonam', '2013', 'Rakeysh'),
]
cur.executemany("INSERT INTO crudmovies VALUES (?,?,?,?,?)", many_records)
# we can insert only one record
cur.execute("INSERT INTO crudmovies VALUES ('Chak De India', 'Sharukh', 'Vidhya', '2007', 'Shimit')")

# ###### Update records into the table ######
'''cur.execute("""UPDATE crudmovies SET release_year='1 October 2002'
    WHERE rowid = 2
    """) '''

# #### Delete record into the table ####
''' cur.execute("DELETE from crudmovies WHERE rowid=4") '''

# Drop table
''' cur.execute("DROP TABLE crudmovies") '''

# Query The Database
cur.execute("SELECT rowid, * FROM crudmovies")
# print(cur.fetchone())
# print(cur.fetchmany(3))
# fetch and print all records of the table
items = cur.fetchall()
# print(items)
for item in items:
    print(item)

# commit our command
conn.commit()

# close our connection
conn.close()