import os
os.system("pip install -r requirements.txt")
try:
	import pymysql

	conn = pymysql.connect(host="localhost",user="root",password=str(input("Enter mysql password >> ")))
	c = conn.cursor()
	c.execute("create database adityagautampassmng25346")
	conn.commit()
	print ("Database Created!")
	conn.select_db("adityagautampassmng25346")
	print ("Database Selected!")
	c.execute("create table passlog(sno int not null, softname varchar(100),password varchar(512),emailId varchar(200), deviation bigint)")
	print ("Table Created!")
	conn.commit()
except:
	print ("Error!")
