lab = [[1, 1, 1, 0, 1],
       [1, 0, 0, 0, 1],
       [1, 0, 1, 1, 1],
       [1, 0, 0, 1, 1],
       [1, 1, 0, 1, 1]]


# busqueda recursiva sobre la matriz lab empezando en la fila f y la columna c


def busca(f, c):
    if lab[f][c] == 0 and (f == 0 or f == len(lab)-1 or c == 0 or c == len(lab)-1) and (f != a or c != b):
        print("Salida encontrada en " + str(f) + "," + str(c))
        return True

    elif lab[f][c] == 1:
        print("Pared en " + str(f) + "," + str(c))
        return False

    elif lab[f][c] == 2:
        print("Ya visitada en " + str(f) + "," + str(c))
        return False

    print("Pasando por " + str(f) + "," + str(c))
    lab[f][c] = 2

    # Terminan casos especiales, comienza busqueda recursiva
    salida = (busca(f+1, c) or busca(f, c+1) or busca(f-1, c) or busca(f, c-1))
    if salida:
        return True

    return False


a = 0
b = 3
busca(a, b)
