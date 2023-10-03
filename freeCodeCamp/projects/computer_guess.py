import random


def adivina_el_numero_computadora(x):
    print(f"Seleciona el numero entre 1 y {x}")
    min = 1
    max = x
    respuesta = ""
    
    while respuesta != "c":
        if min != max:
            prediccion = random.randint(min, max)
        else:
            prediccion = min
            
        # Obtener respuesat del usuario.
        respuesta = input(f"Mi prediccione es: {prediccion}, si es muy alta ingresa (A) si es muy baja ingresa (B) y si es correcto ingresa (C): ").lower()
        
        if respuesta == "a":
            max = prediccion - 1
        if respuesta == "b":
            min = prediccion + 1
        if respuesta == "c":
            print(f"La prediccion es {prediccion}")
            print("=====WINNER=====")
            break
        
adivina_el_numero_computadora(200)