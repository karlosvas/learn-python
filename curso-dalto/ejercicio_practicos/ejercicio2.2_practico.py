#Creando una función que nos devuelba los numeros primos entre 2 y el argumento que pasemos los numeros primos son numeros que solo pueden ser divcididos por si mismo o por 1.
def primos(arg):
    for i in range(2,arg-1):
        if arg % i == 0: return False

    return True

def recorrer_primos(arg):
    primo = []
    for i in range(3,arg+1):
        resultado = primos(i)
        if resultado == True: primo.append(i)
    return primo
    
resultado = recorrer_primos(13)
print(resultado)


