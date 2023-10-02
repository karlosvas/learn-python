response = input("Di algo para analizar tu sentimiento: ")

class Robot:
    def __init__(self, response):
        self.__response = response
    
    @property
    def response(self):
        print(self.__response) 

    @response.setter
    def response(self, chat_response):
        self.__response = chat_response

class Analizar(Robot):
    
    def analizar_enfado(self):
        list_response = response.split()
        for enfado in list_response:
            if enfado == enfado.upper():
                print("Estas enfadado")
                return True    
               
    def analizar_felicidad(self):
        list_response = response.split()
        for alago in list_response:
            if alago == "guapo" or alago == "maquina" or alago == "feliz":
                print("Estas feliz")
                return True
                
    def analizar_tristeza(self):
        list_response = response.split()
        for mal in list_response:
            if mal == "mal" or mal == "triste":
                print("Estas triste")
                return True
            
    def analizar_estados(self):
        feliz = self.analizar_felicidad()
        enfadado = self.analizar_enfado()
        triste = self.analizar_tristeza()
        print(enfadado, feliz, triste)


chat = Analizar(Robot(response))   
chat.analizar_estados()