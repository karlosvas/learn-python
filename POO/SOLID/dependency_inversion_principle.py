# class Diccionario:
#     def verificar_palabra(self, palabra):
#         pass

# class CorregirOrtografico:
#     def __init__(self):
#         self.diccionario = Diccionario()
        
#     def corregir_texto(self, texto):
#         pass
from abc import ABC, abstractmethod

class VerificadorOrtografico(ABC):
    @abstractmethod
    def verificar_palabra():
        pass
    
class Diccionario(VerificadorOrtografico):
    def verificar_palabra(self, palabra):
        pass

class ServicioOnline(VerificadorOrtografico):
    pass

class CorreguirOrtografia:
    def __init__(self, verificador):
        self.verificador = verificador
    
    def correguir_tetxo(self,texto):
        pass
    
corrector = CorreguirOrtografia(Diccionario())