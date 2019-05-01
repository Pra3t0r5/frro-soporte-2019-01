# Implementar la funcion crear_tabla_peso, que cree una tabla PersonaPeso con:
# - IdPersona: Int() (Clave Foranea Persona)
# - Fecha: Date()
# - Peso: Int()

# Implementar la funcion borrar_tabla, que borra la tabla creada anteriormente.

from practico_03.ejercicio_01 import borrar_tabla, crear_tabla, crear_conexion


#PREGUNTAR AUTO
def crear_tabla_peso():
    conn = crear_conexion()
    cur = conn.cursor()
    consSQL = "CREATE TABLE IF NOT EXISTS PersonaPeso(IdPeso INTEGER PRIMARY KEY AUTO, \
                                                        IdPersona INTEGER, Fecha DATE, Peso INTEGER, \
                                                        CONSTRAINT FkPersonas, \
                                                        FOREIGN KEY (IdPersona), \
                                                        REFERENCES persona(IdPersona))"
    cur.execute(consSQL)
    cur.close()
    conn.commit()
    conn.close()


def borrar_tabla_peso():
    conn = crear_conexion()
    cur = conn.cursor()
    consSQL = "DROP TABLE PersonaPeso"
    cur.execute(consSQL)

    cur.close()
    conn.commit()
    conn.close()


# no modificar
def reset_tabla(func):
    def func_wrapper():
        crear_tabla()
        crear_tabla_peso()
        func()
        borrar_tabla_peso()
        borrar_tabla()
    return func_wrapper
