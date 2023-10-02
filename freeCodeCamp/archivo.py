# Trabaja con archivos.
with open("archivo.txt", "r") as archivo:
    for linea in archivo:
        print(linea)
# r => read
# w => write
# a => append
# Agregar + incluye leer, w+ ,q+
notas = {
    "Nora": 87,
    "Gino": 100,
    "Loretto": 67,
    "Talina": 45
}

with open("archivo.txt", "a+") as archivo:
    for nombre, nota in notas.items():
        archivo.write(nombre + " - " + str(nota) + "\n")
