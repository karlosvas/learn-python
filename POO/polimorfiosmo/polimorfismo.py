#Es un concepto que hace referencia a poder envciar los mensajes sintacticos a diferentes objetos, el mensaje es el mismo pero el resultado no.
class Gato():
    def sonido(self):
       return "Miau"
class Perro():
    def sonido(self):
        return "Guau"

def hacer_sonido(animal):
    print(animal.sonido())
    
gato = Gato()
perro = Perro()

print(gato.sonido())
print(perro.sonido())

hacer_sonido(gato)
hacer_sonido(perro)
#A diferencia de otros lenguajes de programación, en Python si se puede acceder los metodos de las clases, sin ser necesario que estos hereden de un padre que disponga de esos métodos.
#Esto es gracias a que Python es un lenguiaje de programación dinámico.
#Polimorfismo de sobrecarga de datos es utilizado en JavaScript cuando al crear un método, dependiendo de los parametrois que le asignes da un resultado u otro.
num1 = 1
num2 = 1.5
resultado = num1 + num2
print(resultado)
print(type(num1))
print(type(num2))
print(type(resultado))
#En Python utiliza la coversión, en este ejemplo coje el primer numero int y lo pasa a flotante para poder realizar la suma, esto se considera polimorfismo porque con distintos tipos de datos el comportamiento es el mismo.