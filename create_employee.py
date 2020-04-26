import pymysql.cursors
from utils import *

connection = utils.connectdb.getConnection()

try:
    cursor = connection.cursor()
    # SQL
    sql = "INSERT INTO employee(emp_no,emp_name,emp_salary) values (%s, %s, %s)"

    # execute sql and pass 3 parameter
    cursor.execute(sql, ('1', 'Nee', '20000'))
    connection.commit()

    print("Create new employee success")
except pymysql.Error as e:
    print("Error %s" % e.args[1])
finally:
    # ปิดการ connection
    connection.close()
