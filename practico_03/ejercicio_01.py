# Implementar la funcion crear_tabla, que cree una tabla Persona con:
# - IdPersona: Int() (autoincremental)
# - Nombre: Char(30)
# - FechaNacimiento: Date()
# - DNI: Int()
# - Altura: Int()

# Implementar la funcion borrar_tabla, que borra la tabla creada anteriormente.

import sqlite3

connectionObject = sqlite3.connect("weather.db")

cursorObject = connectionObject.cursor()

def crear_tabla():
    createTable = "CREATE TABLE Persona(idPersona int AUTOINCREMENT, Nombre char, FechaNacimiento Date, Dni int, altura int)"
    cursorObject.execute(createTable)


def borrar_tabla():
    dropTable = "drop table Persona"
    cursorObject.execute(dropTable)


# no modificar
def reset_tabla(func):
    def func_wrapper():
        crear_tabla()
        func()
        borrar_tabla()
    return func_wrapper
