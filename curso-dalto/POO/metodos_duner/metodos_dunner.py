class Persona():
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    #__str__ sirve para dar un string que se retorna.
    def __str__(self):
        return f"Persona (nombre={self.nombre}), (edad={self.edad})"
    #Para acceder a la representacion del metodo
    def __repr__(self):
        return f"Persona({self.nombre},{self.nombre})"
    #Define el funcionamiento que teine al sumar dos estancias de personas.
    def __add__(self,otro):
        nuevo_valor = self.edad + otro.edad
        return Persona(self.nombre+otro.nombre,nuevo_valor)
    
carlos = Persona("Carlos", 19)
ivan = Persona("Iván", 17)
valeria = Persona("valeria", 34)

# repre = repr(carlos)
# print(repre)

resultado = carlos + ivan + valeria
print(resultado.edad)