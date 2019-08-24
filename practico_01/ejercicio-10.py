# escribir una función mas_larga() que tome una lista de palabras y devuelva la más larga

def mas_larga(lista):
    lens = []

    for x in lista:
        lens.append(len(x))
    maximum = max(lens)
    index = lens.index(maximum)

    return lista[index]


assert (mas_larga(["Hola", "El dia está soleado", "Goodbye"]) == "El dia está soleado")
