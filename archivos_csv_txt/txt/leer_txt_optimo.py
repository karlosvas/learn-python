#Gracias a with el archivo se abre y se cierra una vez se ejecutaron las instruciones, por lo que no hace falta close()
with open("archivos\\texto.txt", encoding="UTF-8") as archivo:
    print(archivo.read())