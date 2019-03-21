# Implementar las funciones superposicion(), que tomen dos listas y devuelva un booleano en base a
# si tienen al menos 1 elemento en común.


# se debe implementar utilizando bucles for anidados.

def superposicion(lista_1, lista_2):
    ac = 0
    for i in lista_1:
        for k in lista_2:
            if i == k:
                ac += 1

    if ac == 0:
        return False
    return True

assert(superposicion(["Hola" , "Adios" ,"Hasta Luego"], ["Hello" ,"Goodbye" ,"Adios"]) == True)
assert(superposicion(["Hola" , "Adios" ,"Hasta Luego"], ["Hello" ,"Goodbye" ,"Bye"]) == False)

