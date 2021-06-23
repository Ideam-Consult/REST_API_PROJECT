# import the connect library from psycopg2
from psycopg2 import connect

table_name = "some_table"

# declare connection instance
conn = connect(
    dbname="pythondb",
    user="phetho",
    password="Password1",
    port='5432'
)

# declare a cursor object from the connection
cursor = conn.cursor()
cursor.execute("drop table Userinfo")
cursor.execute("""CREATE TABLE IF NOT EXISTS Userinfo(
                      FIRST_NAME varchar(20),
                      SURNAME varchar(20),
                      Date_of_birth date
                       )""")


conn.commit()

