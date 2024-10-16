import mariadb
import sys
import time

def passdata(result,userid):
    try:
        conn=mariadb.connect(
            user="phpmyadmin",
            password="1234",
            host="localhost",
            port=3306,
            database="FacialRecognition"
        )
    
    except mariadb.Error as e:
        print(f"Error conectando: {e}")
        sys.exit(1)

    cur = conn.cursor()
    test = conn.cursor()
    try:
        sql = "INSERT INTO catalog_doorrelease(recdate,success,userid) VALUES(NOW(),%s,%s)"
        val = (result,userid)
        cur.execute(sql,val)
    except mariadb.error as e:
        print(f"Error insert: {e}")
    conn.commit()

    param=test.execute("SELECT id,recdate,success,userid FROM catalog_doorrelease")
    #param=cur.fetchone() #coge el ultimo
    for param in test:
        print("Parametros: ",param)
    
    conn.close()



