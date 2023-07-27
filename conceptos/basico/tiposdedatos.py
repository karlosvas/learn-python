nueva_lista = list([])
print(len(nueva_lista))
#El resultado de nueva lista es 0, list suele solo se utiliza para crear listas vacias, len es la longitud.
nueva_lista.append("Nuevo elemento final")
nueva_lista.insert(2, "Acctualizacion indice 2")
nueva_lista.extend([False, 2020, "texto"])
#Append añade un elemento final, insert añede une elemento al indice selecionado, extend añade elementos al array.
nueva_lista.pop(0)
nueva_lista.pop(-1)
nueva_lista.remove(2020)
nueva_lista.clear()
#Eleimina un elemento selecionado su índice, si utilizamos -1 se eliminará el ultimo elemento, -2 penultimo. Eliimina un elemnto por su valor, clear elimina todos los elementos.
nueva_lista.sort(reverse=True)
nueva_lista.reverse()
#short ordena los elementos de mayor a menor de forma ascendente, reverse= true lo ordena en reversa. reverse, invierte los elementos sde una lista.
print(nueva_lista)