import mysql.connector
my_connection= mysql.connector.connect(host="localhost",user="root",passwd="root")
print(my_connection)
my_cursor_object=my_connection.cursor()
print(my_cursor_object)

my_cursor_object.execute("show databases")
print(my_cursor_object)

for i in my_cursor_object:
    print(i)

my_cursor_object.execute("create database excel_db")
