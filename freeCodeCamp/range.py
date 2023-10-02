# i es la variable de control o índice.
# Secuencia de numeros  => 0,1,2,3
for i  in range(4):
    print(i)

# Start se utiliza para identificarq ue deve comenzar en 0
# Stop el valor de fin del rango.
# Step cuanto sumarle al indice.
# for i in range(start, stop[step]):
#     print(i)
    
# Los iterables en python son: Cadenas de caracteres, listas, tuplas, dicionarios , otros.
diccionario = {
    "curso": "FreeCodeCamp",
    "nivel": "Basico",
    "key": "value"
}
# Para acceder a las keys devemos hacerlo asi
for key in diccionario:
    print(key)
# Para acceder a los valores de un diccionario utilizamos:
for valor in diccionario.values():
    print(valor)
    
# Para acceder a las dos a la vez utilizamos:
for key, valor in diccionario.items():
    print(key)
    print(valor)