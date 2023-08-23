#Forma no optima
def suma(lista):
    num_sum = 0
    for numero in lista:
        num_sum += numero
    return num_sum

resultado = suma([5,3,9,10,20,3])
print(resultado)

#Pasandole el parametro args, el * se utiliza para que todos los siguientes parámeteros forman parte de una lista de el último parámetro.
def suma(nombre,*numeros):
    return f"{nombre}, la suma es: {sum(numeros)}"

resultado = suma("Carlos", 3,4,6,7,5)
print(resultado)

#Fomra optima de sumar valores, ya que no hace falta que sea el ultimo parámetro.
def suma(numeros, nombre):
    return f"{nombre}, la suma es: {sum([*numeros])}"

resultado = suma([3,4,6,7,5], "Carlos")
print(resultado)
