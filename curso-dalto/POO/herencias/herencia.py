class Persona():
    def __init__(self, nombre, edad, nacionalidad):
        self.nombre = nombre
        self.edad = edad
        self.nacionalidad = nacionalidad
    
    def hablar(self):
        print("Estoy funcionando")
#Podremos crear diferentres clases pasandole como parametro una clase padre.
class Empleado(Persona):
    def __init__(self, nombre, edad, nacionalidad, trabajo, salario):
        super().__init__(nombre, edad, nacionalidad)
        #Utilizamos super para referisrnos a el padre de la clase.
        #Con self accedemos especificamente ael de su clase.
        self.trabajo = trabajo
        self.salario = salario
        
class Estudiante(Persona):
    def __init__(self, nombre, edad, nacionalidad, notas, universidad):
        super().__init__(nombre, edad, nacionalidad)
        self.notas = notas
        self.universidad = universidad
        
roberto = Empleado("Roberto", 43, "Español", "Programador", "100.000 anuales")
antonio = Estudiante("Roberto", 43, "Español", "Media de 9","UVA")
print(roberto.trabajo)
print(antonio.notas)
roberto.hablar()
