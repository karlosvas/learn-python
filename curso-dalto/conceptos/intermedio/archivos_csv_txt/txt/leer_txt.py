archivo = open("archivos\\texto.txt", encoding="UTF-8")
leer = archivo.read()
print(leer)
#reed() es un metodo para leer un txt antes de ello hay que avbirlo y expecificar su codificación con la funcion open().
lineas = archivo.readlines()
linea = archivo.readline()
print(linea)
print(lineas)
#Cuando un archivo se leee, si queremos volber a leerlo tenemos que cerrarlo primeramente.
#Al utilizar lines() muestra un array con todas las lineas de texto, mientras que con line() muestra un string con todas las lineas de la primera linea, si le das un argumento, mostrará la contidad de caracteres de ese argumento.
archivo.close()
#Deveremos cerrar el archivo siempre, para volber a utilizarlo o para terminar el programa.
