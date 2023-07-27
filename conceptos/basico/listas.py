lista = ["Primer elemento", "Segundo elemento", "Tercero", 45]
tupla = ("primer elemento", "Segundo elemento", "Tercero", 45)
conjunto = {"primer elemento", "Segundo elemento", "Tercero", 45}
#Las tuplas no permiten modificar nunca los elementos, mientras que las listas si, al mostrar el índice de las tuplas o listas utilizamos corchetes.
#Los conjuntos o (set) son elementos que pueden cambiar de lugar, pero no modificar el  elemento, no permite duplicar valores, y no podremos acceder a los elementos mediante un indice.
diccionario = {
    "nombre" : "Carlos Vásquez",
    "github" : "karlosvas",
    "años_actuales" : 19,
    "altura" : 1.70 
}
#Pprecido al JSON de JavaScript, se puede acceder a cada elemento con [].
print(diccionario["nombre"])