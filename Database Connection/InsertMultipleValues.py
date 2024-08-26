import mysql.connector
my_connection=(
    mysql.connector.connect(host="localhost",user="root",passwd="root",database="excel_db"))
my_cursor_object=my_connection.cursor()

query="insert into employees(employee_id,e_name,postion) values (%s,%s,%s)"
values=[(2,"Roshan Yadav","Pharma Engineer"),(3,"Bickey Don","Chemical Engineer")]
try:
    my_cursor_object.executemany(query,values)
    my_connection.commit()
except:
    my_connection.rollback()
my_connection.close()