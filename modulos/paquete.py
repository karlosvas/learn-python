#Un paquete es una carpeta con un conjunto de modulos, python al reconocer el módulo de __init__.py reconoce a la carpeta que contienene los modulos como paquete, si no lo tiene  no lo cuenta como tal.
import paquete.paquetes_saludar
#Puede tener paquetes dentro del paquete, a estos se  les donomina subpaquetes.
print(paquete.paquetes_saludar.Saludar("Antonio"))
print(paquete.__path__)
