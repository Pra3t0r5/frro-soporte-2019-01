# Implementar la función mayor, que reciba tres números y devuelva el mayor de ellos.


def mayor(a, b, c):
    # n = max(a, b, c)
    elementos = [a, b, c]
    n = max(elementos)
    print('mayor: ', n)
    return n


# si no falla es porque esta bien
assert mayor(1, 10, 5) == 10
assert mayor(4, 9, 18) == 18
