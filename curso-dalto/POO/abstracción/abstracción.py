from abc import ABC, abstractclassmethod

class Coche():
    def __init__(self):
        self.__estado = "apagado"
    def encender(self):
        self.__estado = "encendido"
        print("El coche esta encendido")
    def conducir(self):
        if self.__estado == "apagado":
            self.encender()
        print("Conducioendo el coche")

coche = Coche()
coche.conducir()

class Persona(ABC):
    @abstractclassmethod
    def __init__(self, nombre, edad, sexo, actividad):
        self.nombre = nombre
        self.edad = edad
        self.sexo = sexo
        self.actividad = actividad
        
    @abstractclassmethod
    def hacer_actividad(self):
        pass
    
    def presentarse(self):
        print(f"Hola me llamo {self.nombre} y tengo {self.edad} años")
        
class Estudiante(Persona):
    def __init__(self, nombre, edad, sexo, actividad):
        super().__init__(nombre, edad, sexo, actividad)
    def hacer_actividad(self):
        print(f"Estoy {self.actividad}")
class Trabajador(Persona):
    def __init__(self, nombre, edad, sexo, actividad):
        super().__init__(nombre, edad, sexo, actividad)
    def hacer_actividad(self):
        print(f"Estoy ejerciendo de {self.actividad}")
        
        
carlos = Estudiante("Carlos", 19, "hombre", "programando")
adrian = Trabajador("Adrian", 20, "hombre", "mecanico")

carlos.presentarse()
carlos.hacer_actividad()

adrian.presentarse()
adrian.hacer_actividad()
