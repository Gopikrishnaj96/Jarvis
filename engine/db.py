import sqlite3
con =sqlite3.connect("eve.db")
cursor=con.cursor()
query= "CREATE TABLE IF NOT EXISTS sys_command(id integer primary key, name VARCHAR(100), path VARCHAR(1000))"
cursor.execute(query)

#query="INSERT INTO sys_command VALUES(null,'word','c:\ProgramData\Microsoft\Windows\Start Menu\Programs\Microsoft Office\Microsoft Word 2010.lnk')"
#query="DELETE FROM sys_command where id="
#cursor.execute(query)
#con.commit()
query= "CREATE TABLE IF NOT EXISTS web_command(id integer primary key, name VARCHAR(100), path VARCHAR(1000))"
cursor.execute(query)
query="INSERT INTO web_command VALUES(null,'youtube','https://www.youtube.com/')"
#query="DELETE FROM sys_command where id="
cursor.execute(query)
con.commit()