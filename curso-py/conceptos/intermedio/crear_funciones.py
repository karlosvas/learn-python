#Crear una función con parámetros
def saludar(nombre, sexo):
    sexo = sexo.lower()
    if(sexo == "mujer"):
        adjetivo = "reyna"
    elif(sexo == "hombre"):
        adjetivo = "rey"
    else:
        adjetivo= "nose" 
    
    print(f"Hola {nombre} que tal mi {adjetivo}")
    
saludar("Camila", "Mujer")
saludar("Dalto", "HOMbre")

#Crear una fuunción que nos rertorne valores para poder guardar el dato en la funcion
def crear_contrasena_rnd(num):
    chars = "qwertyuiopasdfghjklzxcvbnm"
    num_str = str(num)
    num = int(num_str[0])
    c1 = num - 2
    c2 = num
    c3 = num - 5
    contrasena = f"{chars[c1]}{chars[c2]}{chars[c3]}{num*2}"
    return contrasena,num
#Desepaquetando la función. y mostrando los resultados obtenidos y los datos utilizados para obtenerlo.
password,first_num = crear_contrasena_rnd(1)
print (f"Tu contraseña es: {password}")
print (f"Tu contraseña es: {first_num}")
