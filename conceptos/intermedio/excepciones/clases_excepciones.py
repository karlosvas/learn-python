class MiExcepcion(Exception):
    def __init__(self,err):
        print(f"El error es: {err}")
#Manejando la excepcion
try:
    raise MiExcepcion("Persona poco culta")
except:
    print("Como te vas a equivocar")
