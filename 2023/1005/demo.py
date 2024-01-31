import pymysql


# 1. Connect
conn = None
try :
    conn = pymysql.connect(host='3.39.6.238', port=3306, 
                       user='root', password='pythonmysql')
    
# 2.cursor
    cursor = conn.cursor()

# 3, SQL Statement
    sql = "SELECT NOW()"  
    cursor.execute(sql)
# 4. fetch
    result = cursor.fetchone()
    print(result)
except Exception as err:
    print(err)  
finally : 
# 5.close
    conn.close()
    
