#1 Alumno profesor, 1 Alumno asistente, Objetivos: pedir nombre y edad y ordenarlos de mayor a menor, el mayor de la clase es el profesor y el menor el asistente.

#Primera forma mia.
"""
def alumnos(name,eadge):
    edad_alumno = eadge.split(",")
    name_alumno = name.split(",")
    asistente = eadge.find(min(edad_alumno))
    profesor = eadge.find(max(edad_alumno))
    print(f"El asistente es {name_alumno[asistente]}, y el profesor es {name_alumno[profesor]}")
    orden = sorted(eadge)
    string_orden = ''.join(orden).replace(",", "")
    return string_orden

print(alumnos("Carlos,Ramón,Pedro,Adrian,Alejandro", "1,3,4,2,3"))
"""
#Segunda forma mia.
"""
def alumnos(name,eadge):
    orden = sorted(eadge)
    string_ordenado = ''.join(orden).replace(",", "")
    name_alumno = name.split(",")
    asistente = int(string_ordenado[0])
    profesor = int(string_ordenado[0-1])
    print(f"El asistente es {name_alumno[asistente]}, y el profesor es {name_alumno[profesor]}")
    return string_ordenado

print(alumnos("Carlos,Ramón,Pedro,Adrian,Alejandro", "1,3,4,2,3"))
"""
#Forma del curso

def new_compañero(cantidad):
    compañeros = []
    for i in range(cantidad):
        nombre = input("Insgresa el nombre del compañero: ")
        edad = int(input("ingresa la edad del compañero: "))
        compañero = (nombre,edad)
        compañeros.append(compañero)
    compañeros.sort(key=lambda x:x[1])
    asistente = compañeros[0][0]
    profesor= compañeros[-1][0]
    return asistente,profesor

asistente,profesor = new_compañero(5)
print(f"El profesor es : {profesor} y su asistente es  {asistente}")