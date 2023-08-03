#Toma una función y le añade una funcionalidad extra, para manejo de excepciones para la validacion de entrada, medicion del tiempo de ejecuición.
def decorador(funcion):
    def funcion_modificada():
        print("Antes de llamar a la función")
        funcion()
        print("Despues de llamar la a funcion")
    return funcion_modificada

# def saludo():
#     print("Hola a todos")
    
# saludo_modificado = decorador(saludo)
# saludo_modificado()

@decorador
def saludo():
    print("Hola Carlos como estas")

saludo()
#Gracias a @decorador Python ya sabe que es una función decoradora, por lo que no hace falta crear una nueva variable en el que guardar el resultado de la fucnión si no que lo hace automaticamente.