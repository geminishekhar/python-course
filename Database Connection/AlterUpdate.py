import mysql.connector
my_connection=(
    mysql.connector.connect(host="localhost",user="root",passwd="root",database="excel_db"))
my_cursor_object=my_connection.cursor()

query="alter table employees add column salary varchar(10) default '$10,000'"

try:
    my_cursor_object.execute(query)
    my_connection.commit()
except:
    my_connection.rollback()
my_connection.close()