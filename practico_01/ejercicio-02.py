# Implementar la función mayor, que reciba tres números y devuelva el mayor de ellos.

def max_de_tres(a,b,c):
    n=max(a,b,c)
    return n

assert max_de_tres(10, 5, 3) == 10
assert max_de_tres(9, 18, 15) == 18
