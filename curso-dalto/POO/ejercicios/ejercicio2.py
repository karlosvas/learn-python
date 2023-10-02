class Persona():
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    def datos_persona(self):
        print(f"Mi nombre es {self.nombre} mi edad es {self.edad}")

class Estudiante(Persona):
    def __init__(self, nombre, edad, grado):
        super().__init__(nombre, edad)
        self.grado = grado
    def datos_estudiante(self):
        print(f"Estoy en un grado de {self.grado}")
        
antonio = Estudiante("Pedro", 21, "Superior")
antonio.datos_persona()
antonio.datos_estudiante()