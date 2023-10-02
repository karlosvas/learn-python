# De esta manera podremos manejar las excepcioones como el try catch de js.
try:
    print(not_defined)
except:
    print("Alerta, Excepción")
else:
# si no hubo ningun error se ejecuta.
    print("Else")
finally:
    print("Siempre estoy")
# Una vez fibnalizado ejecuta este codigo si o si.