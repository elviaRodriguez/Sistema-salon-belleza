
from modelos.servicio import Servicio
from modelos.categoria_servicios import CategoriaServicio


class ServicioComposicion:
    """
    Utiliza composición para relacionar un servicio
    con su categoría, sin crear subclases por tipo.
    """

    def __init__(self, servicio, categoria):
        if not isinstance(servicio, Servicio):
            raise TypeError("Se requiere un objeto Servicio.")

        if not isinstance(categoria, CategoriaServicio):
            raise TypeError("Se requiere una categoría válida.")

        self.servicio = servicio
        self.categoria = categoria

    def mostrar_detalle(self):
        return (
            f"{self.servicio.mostrar_detalle()}, "
            f"Categoría: {self.categoria.nombre}"
        )
