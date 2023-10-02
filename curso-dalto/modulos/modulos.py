#Todos los archivos terminados en .py se les conoce como modulos. 
import modulo_saludar as m_welcome
#De esta manera importamos un modulo, la referencia a la funcion de un modulo se le conoce como un objeto namespace
saludo = m_welcome.Saludar("Pedro")
print(saludo)
#Desde este archivo quiero importar solo esta función
from modulo_saludar import Saludar
saludo = Saludar("Pedro")
print(saludo)
#Propiedades del modulo
print(dir(m_welcome))
#Accedemos al nombre de este modulo
print(__name__)
#Accedemos al nombre del modulo de w_welcome desde este modulo.
print(m_welcome.__name__)
#El lugar donde se encuentra
print(m_welcome.__file__)
