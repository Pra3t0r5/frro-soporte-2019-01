





#revisar

vocales = ["a","e","i","o","u","A","E","I","O","U"]

print("ingrese una letra")
letra = input()

def esVocal(letra):
    if letra in vocales:
        return True
    else:
        return False

if esVocal(letra):
    print({letra}," es vocal")
else:
    print({letra}," es consonante")
