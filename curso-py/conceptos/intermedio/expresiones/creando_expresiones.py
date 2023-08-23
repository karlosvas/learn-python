import re
texto= "Hola Pedro, mi numero es: +34 11 4321 +34 11 4321"

pattern = r"\+\d{2}\s\d{2}\s\d{4}-\d{4}"
remplazo = re.sub(pattern,"(numero oculto)",texto)
print(remplazo)