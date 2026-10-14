
from modelos.servicio import Servicio


class CatalogoServicios:
    """
    Representa el catálogo de servicios del salón de belleza.

    Permite almacenar y administrar una colección de objetos
    de tipo Servicio, incluyendo sus clases derivadas.

    Proporciona métodos para agregar servicios al catálogo
    y mostrar la información de los servicios registrados.
    """

    def __init__(self):
        # Inicializa una lista vacía para almacenar los servicios.
        # Cada instancia del catálogo tiene su propia colección.
        self.servicios = []

    def agregar_servicio(self, servicio):
        # Verifica que el objeto sea una instancia de Servicio
        # o de alguna de sus clases hijas.
        if not isinstance(servicio, Servicio):
            raise TypeError(
                "Solo se pueden agregar objetos de tipo Servicio."
            )

        self.servicios.append(servicio)

    def mostrar_servicios(self):
        # Recorre la colección y muestra los detalles
        # de cada servicio mediante polimorfismo.
        for servicio in self.servicios:
            print(servicio.mostrar_detalle())
