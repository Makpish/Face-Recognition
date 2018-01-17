#database to store trained users
import sqlite3

class Users():

	def __init__(self):
		conn = sqlite3.connect('face.db')
		conn.execute("create table if not exists members(id int primary key not null, name text not null);")
		conn.close()

	def checkMember(self,name):
		conn = sqlite3.connect('face.db')
		cursor = conn.execute("SELECT * from members")
		for row in cursor:
			if row[1]==name:
				x = row[0]
				conn.close()
				return x
		conn.close()
		return 0

	def newMember(self,name):
		conn = sqlite3.connect('face.db')
		cursor = conn.execute("SELECT * from members")
		x=1
		# print(cursor)
		for row in cursor:
			x+=1
		print(x)
		conn.execute("insert into members(id,name) values("+ str(x) +",'"+ name +"');")
		conn.commit()
		conn.close()
		return x

	def getMember(self,_id):
		conn = sqlite3.connect('face.db')
		cursor = conn.execute("SELECT name from members where id="+str(_id))
		for row in cursor:
			x = row[0]
			conn.close()
			return x
		conn.close()
		return "Unknown"
