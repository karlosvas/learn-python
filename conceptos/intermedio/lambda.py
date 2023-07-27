#Lambda es una funcion anónima que permite crear funciones pequeñas y sencillas sin necesidad de definirlas. lambda argumentos : expresión. Se utilizan con las funciones pequeñas y sencillas, para funciones temporales.
por_dos = lambda x : x*2
def por_dos(x):
    return x*2
print (por_dos(2))

#Funcion para saver si un numero es par el resto tiene que ser igual a 0 y si es impar iguar a a 1.
numeros=[1,2,3,4,5,6,7,8,9,10]

def es_par(num):
    if (num%2==0):
        return True
num_par = filter(es_par, numeros)
print(list(num_par))

#Forma simplificada con lamda.
num_par = filter(lambda numero: numero%2 == 0, numeros)
print(list(num_par))
#Filter() aplica una función a cada elemento de la secuencia y devuelbe el iterador que contienene solo los los que sean True.

squared_numbers = list(map(lambda x: x**2, numeros))
#Map() aplica una funcion a cada elemento de la secuencia y dev1uelbe un iterador que contine los resultados de aplicar la función a cada elemento.
