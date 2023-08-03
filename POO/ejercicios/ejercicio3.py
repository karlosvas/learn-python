class Personajes:
    def __init__(self,nombre, poder):
        self.__nombre = nombre
        self.__poder = poder
        
    #Getter
    @property
    def poder(self):
        return self.__poder
    @property
    def nombre(self):
        return self.__nombre
        
    @poder.setter
    def poder(self,new_poder):
        self.new__poder = new_poder
        
    def __add__(self, new_poder):
        fusion = self.poder + new_poder.poder
        return fusion
            
naruto = Personajes("Naruto", 20)
sasuke = Personajes("Sasuke",30)

def fusion(pj1,pj2):
    fusion_poder = int(((pj1 + pj2)/2)**2)
    goku = Personajes("Goku", fusion_poder)
    print(f"El nuevo personaje se llama {goku.nombre}  y tiene un poder de {goku.poder}")

fusion(naruto,sasuke)