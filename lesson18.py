import mysql.connector

mydb = mysql.connector.connect(
    host='localhost',
    user = 'root',
    password = 'Pa44w0rD*',
    database = 'my_first_db'
)
#пишу (тренуюсь) код із лекціі
#mycursor = mydb.cursor()
#mycursor.execute('SHOW DATABASES')
#for i in mycursor :
    #print(i)
#mycursor2 = mydb.cursor()
#mycursor2.execute('SELECT * FROM countries')
#result2 = mycursor2.fetchall()
#for r in result2 :
    #print(r)


#створюємо нову базу даних
mycursor3 = mydb.cursor()
#mycursor3.execute('CREATE DATABASE my_first_db')

#створюємо 2 нові таблиці 'student' та 'employee'
#mycursor3.execute("CREATE TABLE student(id INT, name VARCHAR(255))")
#mycursor3.execute("CREATE TABLE employee(id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), salary INT(6))")

#додаємо дані до таблиці employee
#sql2 = "INSERT INTO employee(name, salary) VALUES(%s, %s)"
#val2 = [('John', 10000)]
#mycursor3.executemany(sql2, val2)
#mydb.commit()
#print(mycursor3.rowcount, 'it was inserted')

#додаємо дані до таблиці student
#sql = "INSERT INTO student(id, name) VALUES (%s,%s)"
#val = [(1,'John')]
#mycursor3.executemany(sql, val)
#mydb.commit()
#print(mycursor3.rowcount, 'it was inserted')

#змінюємо  id INT на id INT AUTO_INCREMENT PRIMARY KEY в таблиці student
mycursor3.execute("ALTER TABLE student MODIFY id INT PRIMARY KEY")

