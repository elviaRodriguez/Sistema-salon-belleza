
from modelos.servicio import Servicio

#Significa que ServicioCabello hereda de Servicio. 
#Por eso no necesito volver a definir los atributos nombre y precio.
class ServicioCabello(Servicio):

    def __init__(self, nombre, precio, tipo_cabello):
        super().__init__(nombre, precio) #Llamando al constructor de la clase padre 
        self.tipo_cabello = tipo_cabello #para inicializar los atributos que comparten ambas clases

    
    def mostrar_detalle(self, incluir_precio=True):
        return f"{super().mostrar_detalle(incluir_precio)}, Tipo de cabello: {self.tipo_cabello}"

    
