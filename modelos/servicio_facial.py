
from modelos.servicio import Servicio


class ServicioFacial(Servicio):
    """
    Representa un tratamiento facial del salón de belleza.

    Hereda nombre y precio de Servicio e incorpora
    el tipo de tratamiento facial.

    Sobrescribe mostrar_detalle() para incluir
    información específica del tratamiento.
    """

    def __init__(self, nombre, precio, tipo_tratamiento="Limpieza básica"):
        super().__init__(nombre, precio)
        self.tipo_tratamiento = tipo_tratamiento

    # ==================================================
    # SOBRECARGA SIMULADA - ACTIVIDAD 2
    # ==================================================
    # En Python no existe la sobrecarga tradicional
    # de métodos como en Java.
    #
    # En la clase Servicio utilizamos el parámetro
    # opcional incluir_precio=True.
    #
    # Ejemplos:
    # servicio.mostrar_detalle()
    # servicio.mostrar_detalle(False)
    #
    # Esto permite llamar al mismo método de diferentes
    # maneras sin definir dos métodos separados.

    # ==================================================
    # SOBRESCRITURA - ACTIVIDAD 3, EJERCICIO 2
    # ==================================================
    # ServicioFacial redefine mostrar_detalle(),
    # método que ya existe en la clase padre Servicio.
    #
    # Utilizamos super().mostrar_detalle() para
    # reutilizar el comportamiento heredado y
    # agregar el tipo de tratamiento facial.
    #
    # DIFERENCIA:
    # La sobrecarga simulada permite diferentes formas
    # de llamar a un método mediante parámetros opcionales.
    #
    # La sobrescritura permite que una clase hija
    # redefina un método heredado para adaptar
    # su comportamiento.

    def mostrar_detalle(self, incluir_precio=True):
        return (
            f"{super().mostrar_detalle(incluir_precio)}, "
            f"Tratamiento facial: {self.tipo_tratamiento}"
        )
