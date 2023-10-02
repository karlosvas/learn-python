class Estudiante():
    def __init__(self, nombre, edad, grado):
        self.nombre = nombre
        self.edad = edad
        self.grado = grado
    def estudiar(self):
        print("Estudiando...")
    def datos():
        print(f"El estudiante {estudiante.nombre}, esta estudiando un {estudiante.grado}")
    
        
estudiante = Estudiante(input("Introduce nombre: "),input("Introduce edad: "),input("Introduce Grado: "))
Estudiante.datos()
while True:
    estudiar = input("Que haces: ")
    if (estudiar.lower()=="estudiar"):
        estudiante.estudiar()
        break

