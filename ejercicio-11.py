# Determinar la cantidad de digitos de un numero ingresado.

def cant_digitos(numero):
    digitos = 1
    condicion = 10
    while condicion <= numero:
        digitos += 1
        condicion *= 10

    return digitos

assert(cant_digitos(333) == 3)
