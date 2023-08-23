#Podremos aceder a las distintas carpetas utilizando su nombre seguido de un punto hasta llegar al destino, con as le cambio el nonmbre al que hace referencxia desde este modulo.
import enrutamiento_modulos.modulo_saludarV2 as m_welcome
#Desde este modulo quiero importar solo esta función
from enrutamiento_modulos.modulo_saludarV2 import Saludar
saludo = Saludar("Pedro")
print(saludo)
#Si el mdolulo se ecuentra en una carpeta en un disrectorio anterior accedemos a el mediante su ruta.
import sys
sys.path.append("C:\\??\\??\\??\\??\\ejemplo_fuera")
print(sys.path)

