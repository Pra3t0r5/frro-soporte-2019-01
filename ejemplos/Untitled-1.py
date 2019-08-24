def func3(nombre, *telefonos, **varios):
    print(nombre)
    for nt in telefonos:
        print(nt)
    for clave in varios:
        print(clave + ": "+varios[clave])


func3('Matías', '1234567', '155-458798',
      domicilio='Junín', profesion='ingeniero')
