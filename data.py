import pymysql
from config import host, user, password, db_name


try:
	connection = pymysql.connect(host=host,
                             user=user,
                             port=3306,
                             password=password,
                             database=db_name,
                             cursorclass=pymysql.cursors.DictCursor)
	print("Successfully connected")
except Exception as e:
	print("Connection refused")
	print(e)
