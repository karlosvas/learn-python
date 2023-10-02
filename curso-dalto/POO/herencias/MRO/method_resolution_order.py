#Es el orden en el que python busca el orden.
class A():
    def hablar(self):
        print("Hola desde A")
        
class B(A):
    def hablar(self):
        print("Hola desde B")

class F:
    def hablar(self):
        print("Hola desde F")

class C(F):
    def hablar(self):
        print("Hola desde C")

class D(B,C):
    def hablar(self):
        print("Hola desde D")
        
d= D()
d.hablar()
#Busca primero en el primer parámetro, despues en el segundo parametro, despues en el padre de las dos si comoparten padre, en el caso de que no compartan padre, busca hacia toda la rama de el primer parámetro, y despues a toda la rama del segundo parámetro.
