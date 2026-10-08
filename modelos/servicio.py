from modelos.servicio_base import ServicioBase
from modelos.excepciones import PrecioInvalidoError

class Servicio(ServicioBase):

    def __init__(self, nombre, precio):
        if precio <= 0:
            raise PrecioInvalidoError(
                "El precio debe ser mayor que cero."
            )

        self.nombre = nombre
        self.precio = precio

    def mostrar_detalle(self, incluir_precio=True):
        if incluir_precio:
            return f"Servicio: {self.nombre}, Precio: ${self.precio}"

        return f"Servicio: {self.nombre}"



