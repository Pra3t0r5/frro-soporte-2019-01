# Implementar la función multip() que devuelva el producto de todos los números de una lista.
def multip(lista):
    ac = 1
    for i in lista:
        ac *= i
    return ac

assert(multip([1, 2, 3, 4]) == 24)
