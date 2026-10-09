
from modelos.servicio import Servicio

class ServicioUnas(Servicio):

    def __init__(self, nombre, precio, tipo_esmalte):
        super().__init__(nombre, precio)
        self.tipo_esmalte = tipo_esmalte

    def mostrar_detalle(self, incluir_precio=True):
            return f"{super().mostrar_detalle(incluir_precio)}, Tipo de esmalte: {self.tipo_esmalte}"

   
     

