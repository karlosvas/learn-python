class Notificador:
    def __init__(self, usuario, mensaje):
        self.usuario = usuario
        self.mensaje = mensaje
    
    def notificar(self):
        raise NotImplementedError
    
class NotificadorEmail(Notificador):
    def Notificador(self):
        print(f"Enviando mensaje a {self.usuario.email}")
        
class NotificadorSMS(Notificador):
    def Notificador(self):
        print(f"Enviando mensaje a {self.usuario.sms}")