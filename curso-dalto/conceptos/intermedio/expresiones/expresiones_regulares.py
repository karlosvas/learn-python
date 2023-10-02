import re

texto = """Hola como estas, esta es la cadena 1. como esta
Esta es la linea 2 columna de texto
Y esta es la final definitiva 3"""
#Haciendouna busqueda simeple
resulultado = re.findall("esta", texto)

#\d busca digitos numericos
resulultado = re.findall(r"\d",texto)

#\D muestra todo menos el numero
resulultado = re.findall(r"\D",texto)

#Muestra todos los alphanumeroicos
resulultado = re.findall(r"\w",texto)

#Muestra todos los no alphanumeroicos
resulultado = re.findall(r"\W",texto)

#Busca espacios, espacios, tabs, saltos en linea
resulultado = re.findall(r"\s",texto)

#Tdo menos los espacios saltos en linea y tabs
resulultado = re.findall(r"\S",texto)

#Busca todo menos los saltos en linea
resulultado = re.findall(r".",texto)

#Busca solo los saltos en linea
resulultado = re.findall(r"\n",texto)

#Cancela los caracteres especiales, como los puntos
resulultado = re.findall(r"\.",texto)

#haciendouna cadena que busque un número seguido de un texto seguido de un punto y un espacio.
resutlado = re.findall(r"\d\.\s" ,texto)
print(resutlado)