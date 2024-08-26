import mysql.connector
my_connection=(
    mysql.connector.connect(host="localhost",user="root",passwd="root",database="excel_db"))
my_cursor_object=my_connection.cursor()

query="update employees set salary='$30,000' where employee_id=3"

try:
    my_cursor_object.execute(query)
    my_connection.commit()
except:
    my_connection.rollback()
my_connection.close()