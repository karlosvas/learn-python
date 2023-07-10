diccionario = {
    "nombre": "Carlos",
    "apellidos": "Vasquez",
    "años": "19"
}

for key in diccionario:
    key
    print(f"La clave es: {key}")

for datos in diccionario.items():
    key = datos[0]
    value = datos[1]
    print(f"La clave es: {key}, y el valor es: {value}")
#Iterando un diccionario para obtener la key, y iterando el diccionario para obtener la key y el valor, y asi poder recorrerlo.