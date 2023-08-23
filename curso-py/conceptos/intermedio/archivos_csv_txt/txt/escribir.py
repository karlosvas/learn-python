#Gracias a esto sobre escvribe el archivo.
with open("archivos\\texto2.txt", "w", encoding="UTF-8") as archivo:
    archivo.write("Veamos si funciona")
    archivo.writelines(["Veamos si funciona ","esta array, "])
    archivo.writelines(["esto no lo sobrescribe\n","salto de línea"])
    #Con writelines() nos pide solo un argumento iterable por lo que si queremos poner mas de un texto devermemos parsalo en dentro de array. Y a diferencia de write() no sobrescribe si no que agrega el texto en caso de tener mas de una línea.
#Con el permiso a agregamos texto en vez de sobresribirlo incluso con write()
with open("archivos\\texto3.txt", "a", encoding="UTF-8") as archivo:
    archivo.write("Este archivo tiene permisos a\n")
    archivo.write("¿Este texto se sobrescribira\n")
    archivo.write("Yo diria que no")

