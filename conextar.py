import mysql.connector
from mysql.connector import errorcode
from datetime import date

pwd = input("Digite a senha do usuario do banco. : ")
try:
	db_connection = mysql.connector.connect(
		host='sergi3607.c35.integrator.host', 
		user='sergi3607_base', 
		password=pwd, 
		database='sergi3607_banco')
	print("Database connection made!")
	cursor = db_connection.cursor()
	sql = "INSERT INTO user (name, cpf) VALUES (%s, %s)"
	values = ("Maria", "025.658.698-55")
	cursor.execute(sql, values)
	current_date = date.today()
	formatted_date = current_date.strftime('%d/%m/%Y')
	print(formatted_date)
	print("\n")
	print(cursor.rowcount, "record inserted.")
	print("\n")
	sql = ("SELECT id, name, cpf FROM user")
	cursor.execute(sql)
	for (id, name, cpf) in cursor:
		print(id, name, cpf)
	print("\n")
	sql = ("update user set name = 'Regina Phalanges' where cpf='025.658.698-55'")
	cursor.execute(sql)
	print(cursor.rowcount, "record updated.")
	print("\n")
	sql = ("SELECT id, name, cpf FROM user")
	cursor.execute(sql)
	for (id, name, cpf) in cursor:
		print(id, name, cpf)
	cursor.close()
	db_connection.commit()
    #db_connection.close()

except mysql.connector.Error as error:
	if error.errno == errorcode.ER_BAD_DB_ERROR:
		print("Database doesn't exist")
	elif error.errno == errorcode.ER_ACCESS_DENIED_ERROR:
		print("User name or password is wrong")
	else:
		print(error)
else:
	db_connection.close()