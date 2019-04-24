# Metodos de CONEXION--------------------------------------

# importa una db, sqlite viene incluida en python
import sqlite3
from sqlite3 import Cursor

# crea una base de datos en memoria que dura tanto como el programa funcione
db = sqlite3.connect(':memory:')

# crea un archivo que se guarda en el disco, puede ponerse una locacion absoluta si se quiere especificar la misma ademas del nombre
db = sqlite3.connect('mibase.db')

# instancia un cursor
cur: Cursor = db.cursor()

# query SQL para crear una tabla
cSQL = 'CREATE TABLE IF NOT EXISTS ventas (id INTEGER PRIMARY KEY ASC, descrip TEXT(25), cant REAL(15,2))'

# ejecuta la query
cur.execute(cSQL)
db.commit()
db.close()

# Metodos de INSERT--------------------------------------


# con mysql es '%', con sqlite es '?', otros usan :1
caux = 'INSERT INTO persona (nombre,fechanacimiento,dni,altura) VALUES (%s,%s,%s,%s)'
tdatos = (cnom, dfecha_nac, ndni, naltura)
cur.execute(caux, tdatos)

# otra forma, EXPONE A SQLINJECTION, los textos van con comilla, los numeros no
caux = "INSERT INTO persona (nombre,fechanacimiento,dni,altura) VALUES ('{0}','{1}',{2},{3})"
cins = caux.format(cnom, dfecha_nac, ndni, naltura)
cur.execute(cins)

# Ejemplo completo--------------------------------------

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

# Ejemplo completo SELECT--------------------------------------

cur.execute('''SELECT name, email, phone FROM users''')
for fila in cur:
    print('{0}:{1}. {2}'.format(fila[0], fila[1], fila[2]))

# otro metodo
usu_id = 3
cur.execute('''SELECT name, email, phone FROM users WHERE id=?''',
            (usu_id,))  # con la coma final lo toma como tupla

# Ejemplos de metodos estilo DAO--------------------------------------
#se obvian metodos crear y conectar

def listar():
    global cur
    try:
        cur.execute("SELECT * FROM ventas2")
        # print(cur.description)
        lista = cur.fetchall()
        for row in lista:
            print(row)
    except Exception as f:
        print('Error al ejecutar SQL' + str(f))


def cerrar():
    conn = db
    try:
        cur.close()
        conn.commit()
        conn.close()
    except Exception as f:
        print('Error al cerrar' + str(f))

if __name__ == '__main__':
    conectar()
    crear()