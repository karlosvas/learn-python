import random
import string

from palabras import palabras
from diagramas import vidas_diccionario_visual



def obtener_palabra_valida(palabras):
    palabra = random.choice(palabras)
    
    while "-" in palabra or " " in palabra:
         palabra = random.choice(palabras)
         
    return palabra.upper()

def hungman():
    palabra = obtener_palabra_valida(palabras)

    letras_por_adivinar = set(palabra)
    abedecedario = set(string.ascii_uppercase)
    letras_adivinadas = set()
    
    vidas = 7
    while len(letras_por_adivinar) > 0 and vidas > 0:
        print(f"Te quedan {vidas} vidas y has usado estas letras: {' '.join(letras_adivinadas)}")
        
        # List Comprehension.
        palabra_lista = [letra if letra in letras_adivinadas
        else '-' for letra in palabra]
        # Mostrar estado del ahorcado.
        print(vidas_diccionario_visual[vidas])
        print(f"Palabra: {' '.join(palabra_lista)}")
        
        letra_usuario = input("Escoje una letra: ").upper()
        # Si la letras esta en el abecedario y no esta en el conjubnto sde letras que ya se han ingreado se añade al grupo de letras ingresadas.
        if letra_usuario in abedecedario - letras_adivinadas:
            letras_adivinadas.add(letra_usuario)
            # Si la letra esta en la palabra,  quiitar la letra del conjunto, si no esta quitar una vida.
            if letra_usuario in letras_por_adivinar:
                letras_por_adivinar.remove(letra_usuario)
                print('')
            else:
                vidas -= 1
                print(f"\nTu letra, {letra_usuario} no está en la palabra.")
        # Si la letra esta esxcojida por el usuario ya fue ingresada.
        elif letra_usuario in letras_adivinadas:
            print("\nYa escogiste esa letra por favor escoje letra nueva")
        else:
            print("\nEsta letra no es valida")
    if vidas == 0:
        print(vidas_diccionario_visual[vidas])
        print(f"!Ahoracado perdiste¡\nLa palabra era {palabra}")
    else:
       print(f"!Excelente¡\nLa palabra era {palabra}")
            
hungman()