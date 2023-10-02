class Persona():
    def __init__(self,nombre,edad):
        self.__nombre = nombre
        self.__edad = edad
   #Gracias a esto le dice que no va a swer una funcion si no una propiedad. Esto se conoce como getter
    @property
    def nombre(self):
        return self.__nombre
    #Gracias a este decorador podremos utilizarlo y se le conoce como como setter.
    @nombre.setter
    def nombre(self, new_nombre):
        self.__nombre = new_nombre
    #Gracias a este decorador poderemos utilklizarlo y se le conoze como setter
    @nombre.deleter
    def nombre(self):
        del self.__nombre

persona = Persona("Gregorio", 25)
#Getter (acceder al valor)
nombre = persona.nombre
print(nombre)
#Setter (Dar otro valor)
persona.nombre = "Adrian"
print(persona.nombre)
#Delater (Eliminar delater)
del persona.nombre
print(persona.nombre)