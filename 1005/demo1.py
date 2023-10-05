import pymysql

host = ''
port = 3306
user = 'root'
password = 'pythonmysql'
database = 'mycompany'
conn = pymysql.connect(port=port, user=user,
                       host=host, password=password, database=database)

cursor = conn.cursor()
sql = ""
cursor.execute(sql)
results = cursor.fetchall()
cursor.close()
conn.close()