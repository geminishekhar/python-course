import mysql.connector
my_connection=(
    mysql.connector.connect(host="localhost",user="root",passwd="root",database="excel_db"))
my_cursor_object=my_connection.cursor()
#q=create table employees(employee_id int )
my_cursor_object.execute("create table employees(employee_id int not null primary key,e_name varchar(30) not null,postion varchar(30) not null)")
my_connection.close()