import sqlite3
#Connexion à la base de donnée
conn=sqlite3.connect('ma_base.db')
#Création de la table
conn.execute('''CREATE TABLE clients(id INT PRIMARY KEY NOT NULL,nom TEXT NOT NULL, prenoms TEXT NOT NULL,adresse TEXT NOT NULL,Ville TEXT NOT NULL,codePostal TEXT NOT NULL)''')
#Fermeture de la connexion
conn.close()

#insertion de client dans la table clients de la base de donnée ma_base.bd
conn = sqlite3.connect('ma_base.db')
cursor = conn.cursor()
cursor.execute('INSERT INTO clients (id, nom, prenoms,adresse,ville,codepostal) VALUES ( ?,?, ?,?,?, ?)', ('1', 'Kamenan','dane','cocody blockauss','abidjan','225'))
cursor.execute('INSERT INTO clients (id, nom, prenoms,adresse,ville,codepostal) VALUES ( ?,?, ?,?,?, ?)', ('2', 'Koffi','bernard','cocody centre','abidjan','225'))
cursor.execute('INSERT INTO clients (id, nom, prenoms,adresse,ville,codepostal) VALUES ( ?,?, ?,?,?, ?)', ('3', 'Vali','Gregroire','cocody st jean','abidjan','225'))
cursor.execute('INSERT INTO clients (id, nom, prenoms,adresse,ville,codepostal) VALUES ( ?,?, ?,?,?, ?)', ('4', 'Sangare','silla','cocody st jean','abidjan','225'))
cursor.execute('INSERT INTO clients (id, nom, prenoms,adresse,ville,codepostal) VALUES ( ?,?, ?,?,?, ?)', ('5', 'Materus','yra','cocody st jean','abidjan','225'))
conn.commit()
conn.close()