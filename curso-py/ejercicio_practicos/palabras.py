#Calcular cuanto tarda en decir esta frase, ¿Cuantas palabras dijo?
#Si se tarda mas de un minuto, decirle: "Tampoco te pedí un testamento"
#Cuanto tardará dálto teniendo en cuenta que tarda un 30% mas rapido

request =  input("Dime una frase y te dire cuanto tarda en decirla una persona normal y cuanto tardaria Dalto: ")
request = request.replace(" ", "")
dalto = len(request) - (len(request) * 0.3)

letra = 0.1
letraXSegundo = len(request) * letra

print(f"Esa frase tiene {len(request)} letas")

if (letraXSegundo >= 2):
   print("No me cuentes un testamento")
else:
   print(f"Esa frase tardará en decirse {letraXSegundo} minutos")
   print(f"Una persona normal tardaria {letraXSegundo}minutos mientras que dalto tardaria {dalto}minutos")
   