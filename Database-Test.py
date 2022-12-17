import mysql.connector

conn = mysql.connector.connect(
    username='root', password='vishh@123', host='localhost', database='attendence_management')
cursor = conn.cursor()

cursor.execute("show databases")

data = cursor.fetchall()

print(data)

conn.close()
