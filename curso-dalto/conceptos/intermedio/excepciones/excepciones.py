def sumar_dos():
    a=input("Numero 1: ")
    b=input("Numero 2: ")
    while True:
        try:
            resultado = int(a)+int(b)
            return resultado
        except Exception as e:
            print(f"Ha habido el siguiente error: {e}")
            return False
        finally:
            print("Esto se ejecuta siempre")
        
print(sumar_dos())