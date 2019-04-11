# Implementar la funcion crear_tabla, que cree una tabla Persona con:
# - IdPersona: Int() (autoincremental)
# - Nombre: Char(30)
# - FechaNacimiento: Date()
# - DNI: Int()
# - Altura: Int()

# Implementar la funcion borrar_tabla, que borra la tabla creada anteriormente.

import sqlite3

db = sqlite3.connect('mibase.db')

cur = db.cursor()

def crear_tabla():
    createTable = "CREATE TABLE IF NOT EXISTS Persona(IdPersona INTEGER PRIMARY KEY ASC,Nombre char(30),FechaNacimiento " \
                  "Date, DNI INTEGER, Altura INTEGER)"
    cur.execute(createTable)


def borrar_tabla():
    dropTable = "drop table Persona"
    cur.execute(dropTable)

def cerrar_conexión():
    cur.close()
    db.commit()
    db.close()



# no modificar
def reset_tabla(func):
    def func_wrapper():
        crear_tabla()
        func()
        borrar_tabla()
    return func_wrapper
