type("devolvera class `str`")
#Type es una funcion que, nos devuelbe de que tipo es.
dir()
#Devuulebe todos los atributos de un objeto.
resultado = "hola"
resultado.upper()
resultado.lower()
resultado.capitalize()
#Upper transforma en mayúsculas, lower en minúsculas, capitalize transforma todo a minusulas menos la primera letra.
resultado.find("h")
resultado.index("h")
#Busca la posición del índice de lo buscado en la variable, index funciona igual pero si find no encuentra nada devuelbe -1, y si index no lo encuentra, genera un error.
resultado.isnumeric()
resultado.isalpha()
#Isnumeric devuelbe True o False si es un número, isalpha devuelbe True o Flase si es alphaniumerico (Unicamente texto sin contar espacios).
resultado.count("a")
len(resultado)
resultado.startswith("h")
resultado.endswith("a")
#Count cuenta las coincidencias, la función len nos dice cuantos caracteres tiene una cadena, lo mismo que (lenght). startswith devuelbe True o False si empieza con el parametro que le damos, lo mimo con endswitch.
resultado.replace(",", " ")
resultado.split(",")
#Replace remplaza el primer parametro con el segundo, split nos devuelbe una array del texto que le pasemos, lo separa por el parametro que le demos como una coma, un punto o una letra.