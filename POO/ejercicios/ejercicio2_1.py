class Animal:
    def comer(self):
        print("Estoy comiendo")
        
class Mamifero(Animal):
    def amamantar(self):
        print("Estoy amamantando")
        
class Ave(Animal):
    def volar(self):
        print("Estoy volando")
        
class Muercilago(Mamifero, Ave):
    pass
        
animal = Muercilago()

animal.comer()
animal.amamantar()
animal.volar()