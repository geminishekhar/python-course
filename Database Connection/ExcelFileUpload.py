import mysql.connector
import xlrd
my_connection=(
    mysql.connector.connect(host="localhost",user="root",passwd="root",database="excel_db"))
my_cursor_object=my_connection.cursor()
loc=("C:\\Users\\Shekhar Yadav\\Downloads\\Employees.xls")
a=xlrd.open_workbook(loc)
sheet=a.sheet_by_index(0)
sheet.cell_value(0,0)
for i in range(1,12):
    print(sheet.row_values(i))
my_connection.close()