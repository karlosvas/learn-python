import random
import time


def native_search(list, objetivo):
    for i in range(len(list)):
        if list[i] == objetivo:
           return i
    return -1 

def binary_search(list, objetivo, limite_inferior=None, limite_superior= None):
    if limite_inferior is None:
        limite_inferior = 0
    if limite_superior is None:
        limite_superior = len(list) -1

    # No es válido
    if limite_superior < limite_inferior:
        return -1
    
    punto_medio = (limite_inferior + limite_superior) // 2
    
    if list[punto_medio] == objetivo:
        return punto_medio
    elif objetivo < list[punto_medio]:
        return binary_search(list, objetivo, limite_inferior, punto_medio -1)
    else:
        return binary_search(list, objetivo, punto_medio +1, limite_superior)
        

if __name__ == "__main__":
    size = 10000
    conjunto_inicial = set()
    
    while len(conjunto_inicial) < size:
        conjunto_inicial.add(random.randint(-3* size, 3 * size))

    list = sorted(list(conjunto_inicial))
    
    inicio = time.time()
    for objetivo in list:
        native_search(list, objetivo)
    fin = time.time()
    print(f"Native version time: {fin - inicio} segundos")   
     
    inicio = time.time()
    for objetivo in list:
        binary_search(list, objetivo)
    fin = time.time()
    print(f"Native binary time: {fin - inicio} segundos")    