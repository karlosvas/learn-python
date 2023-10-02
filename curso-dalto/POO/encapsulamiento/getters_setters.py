class Persona():
    def __init__(self,nombre,edad):
        self.__nombre = nombre
        self.__edad = edad
    def get_nombre(self):
        return self.__nombre
    def set_nombre(self, new_nombre):
        self.__nombre = new_nombre

persona1 = Persona("Gregorio", 25)
nombre = persona1.get_nombre()
print(nombre)
#Un getter es un concepto para hacer referencia a una funcion para acceder a un valor supuestamente privado
#Los setters hacen lo mismo pero en vez de acceder a eklloos los define.
nombre = persona1.set_nombre("Adrian")
nombre = persona1.get_nombre()
print(nombre)
#Un setter la da una nueva propiedad, y con getter accedemosa  ella.