# Implementar la funcion crear_tabla, que cree una tabla Persona con:
# - IdPersona: Int() (autoincremental)
# - Nombre: Char(30)
# - FechaNacimiento: Date()
# - DNI: Int()
# - Altura: Int()

# Implementar la funcion borrar_tabla, que borra la tabla creada anteriormente.

import sqlite3

def crear_conexion():
    conn = sqlite3.connect('mibase.db')
    return conn

def crear_tabla():
    conn = crear_conexion()
    cur = conn.cursor()
    create_table = "CREATE TABLE IF NOT EXISTS persona(IdPersona INTEGER PRIMARY KEY AUTOINCREMENT, Nombre VARCHAR(30) NULL, FechaNacimiento DATETIME NULL, DNI INTEGER NULL, Altura INTEGER NULL)"
    cur.execute(create_table)
    
    cur.close()
    conn.commit()
    conn.close()



def borrar_tabla():
    conn = crear_conexion()
    cur = conn.cursor()
    drop_table = "DROP TABLE IF EXISTS persona"
    cur.execute(drop_table)

    cur.close()
    conn.commit()
    conn.close()


# no modificar
def reset_tabla(func):
    def func_wrapper():
        crear_tabla()
        func()
        borrar_tabla()
    return func_wrapper



crear_tabla()
