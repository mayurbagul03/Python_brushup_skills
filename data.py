import mysql.connector
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Root"
)

cursor =conn.cursor()

cursor.execute("CREATE DATABASE IF NOT EXISTS school")
cursor.execute('USE school')

cursor.execute("""
    CREATE TABLE IF NOT EXISTS students(
               id INT AUTO_INCREMENT PRIMARY KEY,
               name VARCHAR(50),
               marks INT,
               age INT
               )

"""
)

print("Database Table is Ready!")
conn.close()