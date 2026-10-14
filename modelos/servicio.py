from modelos.servicio_base import ServicioBase
from modelos.excepciones import PrecioInvalidoError

class Servicio(ServicioBase):
    """
    Representa un servicio ofrecido por el salón de belleza.
    Permite registrar el nombre y precio de un servicio,
    validar que su precio sea mayor que cero y consultar
    su información con o sin mostrar el precio.

    Hereda de ServicioBase e implementa mostrar_detalle().
    """

    def __init__(self, nombre, precio):
        # Inicializa los atributos del servicio.
        # El precio se asigna mediante el setter para validarlo.
        self.nombre = nombre
        self.precio = precio

    @property
    def precio(self):
        # Permite consultar el precio del servicio.
        return self.__precio

    @precio.setter
    def precio(self, nuevo_precio):
        # Valida que el precio sea mayor que cero.
        if nuevo_precio <= 0:
            raise PrecioInvalidoError(
                "El precio debe ser mayor que cero."
            )
        self.__precio = nuevo_precio

    # Simula la sobrecarga mediante un argumento por defecto.
    # Permite mostrar el detalle con o sin incluir el precio.
    def mostrar_detalle(self, incluir_precio=True):
        if incluir_precio:
            return f"Servicio: {self.nombre}, Precio: ${self.precio:.2f}"

        return f"Servicio: {self.nombre}"
