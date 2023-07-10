frutas = ["Platano", "Fresa", "Melón", "Manzana", "Naranja"]
for fruta in frutas:
    if fruta == "Fresa":
        continue
    elif fruta == "Manzana":
        break
    print(f"La fruta {fruta} esta buena pouedes comerla")
else:
    print("Bucle terminado")
#En este ejemplo el else nio se ejecuta ya que al encontrar Manzana termina el bucle.
cadena = "Un texto"
for letra in cadena:
    print (letra)
#Podremos iterar un texto.
numeros = [1,2,10,50] 
numeros_duplicados = [x*2 for x in numeros]
print(numeros_duplicados)
#De eta manera podremos multiplicar poior dos el valor de los números utilizando un bucle.