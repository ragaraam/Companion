import aiml
import psycopg2

# Create the kernel and learn AIML files
kernel = aiml.Kernel()
kernel.learn("std-startup.xml")
kernel.respond("load aiml b")
conn = psycopg2.connect(database="prod", user="postgres", password="raga", host="127.0.0.1", port="5432")
cur = conn.cursor()
sessionId = 12345
cur.execute("create view new as select * from product")
#sessionData = kernel.getSessionData(sessionId)

# Press CTRL-C to break this loop
while True:
    res= kernel.respond(raw_input(),sessionId)
    print res
    item=kernel.getPredicate("item",sessionId)
    comp=kernel.getPredicate("company",sessionId)
    start=kernel.getPredicate("start",sessionId)
    end=kernel.getPredicate("end",sessionId)
    sugg=kernel.getPredicate("sugg",sessionId)
    book=kernel.getPredicate("book",sessionId)
    query="select * from product where "
    if item :
       cur.execute("create or replace view new as select * from product where category = %s",(item,))

    if comp :
       cur.execute("create or replace view new as select * from product where company = %s",(comp,))

    if start :
       cur.execute("create or replace view new as select * from product where price >= %s and price<=%s",(start,end,))    
    cur.execute("select * from new;")
    if sugg:
       rows = cur.fetchall()
       if rows:
          for row in rows:
             print "  ", row
       else:
          print "No match found"

    kernel.setPredicate("sugg",0,sessionId)
    close=kernel.getPredicate("close",sessionId)
    if close :
        break;
if book:
    cc=raw_input()
    if cc:
       print "Thnak you for purchasing!!"
    
