t1 = (10, "hola", 13.6)

print(id(t1), t1)

#t1(2) = "nuevo" #no se puede modificar un elemento de tupla

d = dict() # d = {}
print (type(d))

d= {'origen':(0,0), 'Uno':(1,1), 'final':(3,5)}
print(d)
print('consultamos un elemento por su clave:', d['origen'])

d['otro punto agregado'] = (1,2)

print('claves', d.keys())
print('valores', d.values())

def func(a, b=28): #b tiene valor por defecto
    a = a+1
    b = b+1
    return a,b #parentesis opcionales, pero automaticamente lo toma como tupla

c1 = 2
e1 = 3
x,y = func(c1,e1)
print(x,y)
x,y = func(c1) #toma valor por defecto para b
print(x,y)
x,y = func(b=e1, a=c1) # no se necesita saber en que orden van los parametros si se especifica el nombre
print(x,y)

