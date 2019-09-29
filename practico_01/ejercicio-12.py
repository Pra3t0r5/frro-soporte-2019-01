# Determinar la suma de todos los numeros de 1 a N. N es un numero que se ingresa por consola.


def suma_1_a_n(n):
    ac=0
    for i in range (1, n+1):
        ac += i
    return ac

num = int(input("Ingrese un numero: "))

assert(suma_1_a_n(num) == suma_1_a_n(num))
