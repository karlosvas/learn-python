#Los parametros de una función son parámetreos posicionales parametro1, parametro2, parametrop3, el orden afecta.
def frase(nombre, apellido, adjetivo):
    return f"Hola {nombre} {apellido} eres muy {adjetivo}"

#Utlilizando "keyword arguments", o de "argumentos palabras clave", se utilizara como parametro por defecto en el caso de no añadirle otro.
frase_resultado = frase(adjetivo = "grande", nombre= "Carlos", apellido = "Vásquez")
print(frase_resultado)
