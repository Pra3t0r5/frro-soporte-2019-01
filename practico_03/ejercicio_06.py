# Implementar la funcion crear_tabla_peso, que cree una tabla PersonaPeso con:
# - IdPersona: Int() (Clave Foranea Persona)
# - Fecha: Date()
# - Peso: Int()

# Implementar la funcion borrar_tabla, que borra la tabla creada anteriormente.

from frro_soporte_2019_01.practico_03.ejercicio_01 import crear_conexion
from frro_soporte_2019_01.practico_03.ejercicio_01 import crear_tabla
from frro_soporte_2019_01.practico_03.ejercicio_01 import borrar_tabla


def crear_tabla_peso():
    conn = crear_conexion()
    cur = conn.cursor()
    create_table = 'CREATE TABLE IF NOT EXISTS PersonaPeso (id_peso INTEGER PRIMARY KEY AUTOINCREMENT, \
                                                  id_persona INTEGER, \
                                                  fecha DATETIME NULL, \
                                                  peso INT NULL, \
                                                  CONSTRAINT fk_personas \
                                                  FOREIGN KEY (id_Persona) \
                                                  REFERENCES persona(id_persona)); '
    cur.execute(create_table)
    cur.close()
    conn.commit()
    conn.close()


def borrar_tabla_peso():
    conn = crear_conexion()
    cur = conn.cursor()
    drop_table = "DROP TABLE PersonaPeso"
    cur.execute(drop_table)

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
