import psycopg2
from psycopg2.extensions import AsIs


conn = psycopg2.connect(database="prod", user="postgres", password="raga", host="127.0.0.1", port="5432")
cur = conn.cursor()

while True:
    ido=AsIs(raw_input())
    name=AsIs(raw_input())
    cat=AsIs(raw_input())
    price=AsIs(raw_input())
    comp=AsIs(raw_input())
    cur.execute('INSERT INTO product(ID,NAME,CATEGORY,PRICE,COMPANY) \
             VALUES (%s, %s, %s, %s, %s )',(ido,name,cat,price,comp))
    print "inserted successfully"
    print cur.execute("select * from product")

conn.commit()
conn.close()

