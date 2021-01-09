import mysql.connector


u='root'
p='root'
db='aliens'
mycon=mysql.connector.Connect(host='localhost',user=u,passwd=p,database=db)
cur=mycon.cursor()

def run():
    try:

        cur.execute('select * from good ')

        pr=cur.fetchall()
        for i in pr:
            print('%s  %s  %s'%(i[0],i[1],i[2]))
    except:
        mycon.rollback()

