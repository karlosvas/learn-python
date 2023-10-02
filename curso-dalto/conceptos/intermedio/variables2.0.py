datos = ("Carlos", "Vasquez", 19)
nombre,apellido,anos= datos
#Creaccion de tupola, y asignando valores.
tupla = tuple(["dato1","dato2"])
tuple = "dato1", "dato2"
#Al separar los parametros con coma automatiocamente se crea una tupla
conjunto = set(["Dato1", "Dato2", ("nuevatuple")])
#conjunto = set(["Dato1", "Dato2", ["nuevatuple"]])
#conjunto = set(["Dato1", "Dato2", {"nuevatuple"}])

#No se pueden hasear ni diciionarios ni litas, por lo que si creamos un conjunto y cqueremos crear iotro dentro devera ser una tupla u otro conjunto.
#Para metrer otro cunjunto devremos utilizar la funcion de frozenset.
nuevo_conjunto = frozenset(["Esto no es haseable", "Esta dentro de otro conjutno"])
conjunto2 = set(["Dato1", "Dato2", ("nuevatuple"), nuevo_conjunto])
conjunto3 = {"Dato1", "Dato2", ("nuevatuple"), nuevo_conjunto}
#Conjunto 2 y 3 hacen la misma función, soin diferentes formas de crear conjuntos.
x = {1,2,3,4}
y = {2,3}
subconjuntos = y.issubset(x)
superconjuntos = x.issuperset(y)
subconjuntos = y.isdisjoint(x)
#Con issubset verificamos si es un subconjunto de x, mientras que issuperset verifica si x es un superconjunto de y, en los dos casos daria True, isdisjoint verifica si hay algun resultado en común.
