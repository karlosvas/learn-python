class MiClase:
    def __init__(self):
        self._atributo_privado = "Valor"
        #_ indica que es privado se puede acceder, __ significa muy privado y no se pueden acceder.
    def _hablar(self):
        print("Esto es convencion de privado")
    def __hablar(self):
        print("Esto es muy privado")
        
        
objeto = MiClase()
print(objeto._atributo_privado)
print(objeto._hablar())
print(objeto.__hablar())
#Los privados devuelben None