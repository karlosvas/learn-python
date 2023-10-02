diccionario = dict(nombre="Carlos", apellido="Vasquez")

diccionario = {
    "nombre": "Carlos",
    "apellido" : "Vasquez"
}

#Estas son las dos formas de crear un diccionario, la función dict() se suele utilizar para crear diccionarios vacíos.
diccionario =  {frozenset(["dato1", "dato2"]),"dato3"}
#Las listas no pueden ser claves, utilizamos frozensets para añadir  conjuntos en otros conjuntos.
diccionario = dict.fromkeys(["nombre", "apellidos"], "hola")
#Otra forma de crear diccionarios es con fromkeys con todos los valores sin asignar (None). Es un iterable, de esta manera le damos el valor hola a todos los elementos.