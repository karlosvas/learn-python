class Persona():
    def __init__(self, nombre, edad, nacionalidad):
        self.nombre = nombre
        self.edad = edad
        self.nacionalidad = nacionalidad
    
    def hablar(self):
        print("Estoy funcionando")
    
class Artista():
    def __init__(self, habilidad):
        self.habilidad = habilidad
    def mostrar_habilidad(self):
        return f"Mi habilidad es: {self.habilidad}"
#Podremos crear una clase pasandole como parametro otras dos clases siempre y cuando estas clases no tengan una clase padre.        
class EmpleadoArtista(Persona,Artista):
    def __init__(self, nombre, edad, nacionalidad, habilidad, salario, empresa):
        Persona.__init__(self, nombre, edad, nacionalidad)
        Artista.__init__(self, habilidad)
        self.salario = salario
        self.empresa = empresa
        
    def presentarse (self):
        print(f"Hola, soy {self.nombre}, {self.mostrar_habilidad()} y trabajo en {self.empresa}")
        
#Aqui creamos a la persona            
roberto = EmpleadoArtista("roberto", 19, "Danés", "Escultor", "3000", "Microsoft")
roberto.presentarse()
#Con self accedemos a la persona que se inicializa en esa clase mientras que super siempre se accede a la clase padre.
#Normalmente se utiliza super para llmar a su padre.

#Pregunta si el primer parameto es una clase del segundo parametro.
herencia= issubclass(EmpleadoArtista, Artista)
#PRegunta si es una instancia de la clase que le damos como segundo parametro.
instancia= isinstance(roberto, EmpleadoArtista)
print(herencia)
print(instancia)