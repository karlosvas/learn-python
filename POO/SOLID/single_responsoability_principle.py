class Coche:
    def __init__(self,tanque):
        self.tanque = tanque
        self.posicion = 0
        
    def mover(self, distancia):
        if self.tanque.obtener_combustible() >= distancia /2:
            self.posicion += distancia
            self.tanque.usar_combustible(distancia/2)
            print("funcionando")
        else:
            print("No hay suficiente combustible")
            
    def obtener_posicion(self):
        return self.posicion

class TanqueCombustible(Coche):
    def __init__(self):
        self.combustible = 100
        
    def agregar_combustible(self, cantidad):
        self.combustible += cantidad
    
    def obtener_combustible(self):
        return self.combustible
    
    def usar_combustible(self, cantidad):
        self.combustible -= cantidad


tanque = TanqueCombustible()
coche = Coche(tanque)


print(coche.obtener_posicion())
coche.mover(10)
print(coche.obtener_posicion())
coche.mover(20)
print(coche.obtener_posicion())
coche.mover(60)
print(coche.obtener_posicion())
coche.mover(100)
print(coche.obtener_posicion())
coche.mover(100)
print(coche.obtener_posicion())