import psycopg2

try:
    conn = psycopg2.connect("dbname=crypto user=sketchmaster password=pythonPr0")
    print('connection success')
    cur = conn.cursor()
    cur.execute('SELECT version()')
    db_version = cur.fetchone()
    print(db_version)
    cur.close()

except: print("no connection was made")
finally:
    if conn is not None:
        conn.close()
        print('Database connection closed.')