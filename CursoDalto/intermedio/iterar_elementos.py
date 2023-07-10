animales = ["loro", "gato", "perro", "lobo"]
numeros = [10,16,47,99]
 
for animal in animales:
    print (f"El animal en esta vuelta es {animal}")   
for numero in numeros:
    resultado = numero * 10
    print(resultado)
    
for animal,numero in zip(animales,numeros):
    print(f"Recorriendo lista 1 {numero}")
    print(f"Recorriendo lista 2 {animal}")
#De esta forma podremos iterar dos listas al mismo tiempo,
for num in range(0,10):
    print(num)
#De esta manera podremos iterar en el buvcle las veces que queremos tambien podremos utilizar la funcion range utilizando un paarametro para las vueltas que queremos que de sin incluir el úlltimo range(11) = 10 vueltas.
for num in enumerate(numeros):
    indice = num[0]
    valor = num[1]
    print(f"Indice es {indice} y el valor es {valor}")
else:
    print("El bucle terminó")
#Devuelve una tupla, con el valor del indice, el segundo el valor, podremos utilizar else y para que el bucle lo ejecute si no tiene mas elementos que recorrer.