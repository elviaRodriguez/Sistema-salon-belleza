from modelos.servicio_base import ServicioBase
from modelos.excepciones import PrecioInvalidoError

class Servicio(ServicioBase):

    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

    @property
    def precio(self):
        return self.__precio

    @precio.setter
    def precio(self, nuevo_precio):
         # Validamos el precio para evitar que un servicio
         # tenga un costo menor o igual a cero.
        if nuevo_precio <= 0:
            raise PrecioInvalidoError(
                "El precio debe ser mayor que cero."
            )
        self.__precio = nuevo_precio

    def mostrar_detalle(self, incluir_precio=True):
       if incluir_precio:
          return f"Servicio: {self.nombre}, Precio: ${self.precio:.2f}"

          return f"Servicio: {self.nombre}"
    