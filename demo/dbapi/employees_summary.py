# Display count of employees and average salary

import sqlite3
import dbutil

try:
    con = sqlite3.connect(dbutil.DBNAME)
    cur = con.cursor()
    cur.execute("select count(*), avg(salary) from employees")  # SQL Command
    count_emp, avg_salary = cur.fetchone()
    print(f"Count   : {count_emp:10}")
    print(f"Average : {avg_salary:10.0f}")
    cur.close()
    con.close()
except Exception as ex:
    print('Error :', ex)
