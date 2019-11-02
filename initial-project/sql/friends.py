import sqlite3


connection = sqlite3.connect("my_friends.db")

# Create a cursor
c = connection.cursor()

# Execute some sql
c.execute("CREATE TABLE friends (first_name TEXT, last_name TEXT, closeness INTEGER);")

insert_query = '''INSERT INTO friends
                VALUES('Merriwether', 'Lewis', 7)
'''

c.execute(insert_query)

data = ('Steve', 'Irwin', 9)

query = f"INSERT INTO friends  VALUES(?,?,?)"

c.execute(query, data)
# commit the changes
connection.commit()

connection.close()
