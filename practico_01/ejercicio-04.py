# Implementar la función es_vocal, que reciba un carácter y
# devuelva un booleano en base a si letra es una vocal o no.


# Resolver utilizando listas y el operador in.

vocales=["a","e","i","o","u","A","E","I","O","U"]

def es_vocal(caracter):
    return caracter in vocales

assert(es_vocal("a") == True)
assert(es_vocal("b") == False)


