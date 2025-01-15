import sqlite3
con =sqlite3.connect("eve.db")
cursor=con.cursor()
query= "CREATE TABLE IF NOT EXISTS sys_command(id integer primary key, name VARCHAR(100), path VARCHAR(1000))"
cursor.execute(query)

#query="INSERT INTO sys_command VALUES(null,'word','c:\ProgramData\Microsoft\Windows\Start Menu\Programs\Microsoft Office\Microsoft Word 2010.lnk')"
#query="DELETE FROM web_command where id>2"
#cursor.execute(query)
#con.commit()
#query= "CREATE TABLE IF NOT EXISTS web_command(id integer primary key, name VARCHAR(100), path VARCHAR(1000))"
#ursor.execute(query)
#query="INSERT INTO web_command VALUES(null,'youtube','https://www.youtube.com/')"
query="DELETE FROM contacts where id between 3 and 6"
cursor.execute(query)
con.commit()
#cursor.execute('''CREATE TABLE IF NOT EXISTS contacts (id integer primary key, name VARCHAR(200), mobile_no VARCHAR(255), email VARCHAR(255) NULL)''')
#uery="INSERT INTO contacts (id,'name','mobile_no')VALUES(null,'amma','9447465239')"
#ursor.execute(query)
#con.commit()
#query='aaron'
#query=query.strip().lower()
#cursor.execute("SELECT mobile_no FROM contacts   ")