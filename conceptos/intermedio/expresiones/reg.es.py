import re

text= "The quick brawn for jumps over the lazy dog"
x = re.search("The.*dogs$", text)
if x:
    print("Se a encontrado")
else:
    print("No se a encontrado")
    
#Ejemplo2
text = "La fecha es 23/06/2021 y el telefono es -1-555-555-5555"
replacement = "fecha oculta"
pattern = r"\d{2}/\d{2}/\d{4}"
#Sub encuentra la cadena y realiza un remplazo
new_text = re.sub(pattern, replacement, text)
print("Texto modificado: ",new_text)

#Ejempo3
text= "Remplazando todas las vocasles poir asteriscos"
email = "correogithub@gmail.com"
pattern = "[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
result = re.match(pattern, email)
if result:
    print("Direccion de correo valida")
else:
    print("Porfavor ingrese un correo valido")

#Emeplo4
text="Este es un ejemplo de una pagina web: https://github.com/karlosvas y tambien podemos buscarlo"
pattern = "https?://[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
result= re.findall(pattern, text)
print(result)
