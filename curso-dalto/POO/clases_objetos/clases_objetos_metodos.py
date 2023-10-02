#class PrimeraLEtraEnMayuscula = "pascalcase"
# utilizamso pascalcase  para trabajar con las clases en POO
snake_case = "Asi se esciben las variables en python"
#git-poo = "Asi combramos a los archivos en git"

class Movil():
    #constructor
    def __init__(self, marca, modelo, camara):
        self.marca = marca
        self.modelo = modelo
        self.camara = camara
        #Todas las funciones dentro de una clase se llaman metodos.
    def llamar(self):
        print(f"Estas haciendo una llamada desde un {self.modelo}")
    def cortar(self):
        print(f"Cortaste la llamada desde tu : {self.modelo}")
    
movil1 = Movil("Samsumg", "S23", "48MP")
movil2 = Movil("Apple", "S23", "48MP")

movil1.llamar()
movil1.cortar()
#Un obhjeto es una instancia de una clase, se guardan en la RAM.
