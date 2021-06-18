from psycopg2 import connect

table_name = "some_table"

	# declare connection instance
conn = connect(
dbname = "postgres",
user = "postgres",
host = "172.28.1.4",
password = "1234"
	)

	# declare a cursor object from the connection
cursor = conn.cursor()
cursor .execute("""CREATE TABLE IF NOT EXISTS User_info
                                                      (
id INT PRIMARY KEY NOT NULL,
FirstName INT NOT NULL,
Surname TEXT NOT NULL,
Dateofbirth BOOL NOT NULL
                                                      )"""	)
# execute an SQL statement using the psycopg2 cursor object
# cursor.execute(f"SELECT * FROM {table_name};")
