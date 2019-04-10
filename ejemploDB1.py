import sqlite3

db = sqlite3.connect('mibase.db')

cur = db.cursor
# la triple comilla permite poner strings dentro de strings sin necesidad de escapar
cSQL = '''CREATE TABLE IF NO EXISTS ventas (id INTEGER PRIMARY KEY ASC, descrip TEXT(25), cant REAL(15,2))'''
cur.execute(cSQL)

cSQL = "INSERT into ventas (descript,cant) VALUES (?,?)"
tdatos = ('queso', 12.5)

cur.execute(cSQL, tdatos)
id = cur.lastrowind
db.dbcommit()
db.close()
