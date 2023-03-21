import sqlite3

conn = sqlite3.connect('mabaseDRM.db')
cr=conn.cursor()
cr.execute("SELECT * FROM personnes")
PR=cr.fetchall()
print(PR)

cr.execute("UPDATE personnes SET NomPersonne='KOUADIO' WHERE idpersonne=3")
conn.commit()

print(PR)


conn.close
