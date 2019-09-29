# Implementar la función operacion, donde:
# - Si multiplicar es True: devolver la multiplicación entre a y b.
# - Si multiplicar es False: devolver la division entre a y b.
# - Si multiplicar es False y b es cero: imprimir por consola "Operación no valida".


def operacion(a, b, multiplicar):
    
    if multiplicar:
        return a*b
    elif b!=0:        
        return a/b
    else:
        print('Operacion invalida')
        return False

assert operacion(1, 2, True) == 2
assert operacion(2, 2, False) == 1
assert operacion(2, 0, False) == False


