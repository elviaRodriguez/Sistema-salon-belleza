from modelos.servicio import Servicio


class ServicioCabello(Servicio):

    def __init__(self, nombre, precio, tipo_cabello):
        super().__init__(nombre, precio)
        self.tipo_cabello = tipo_cabello

     # POLIMORFISMO:
    # Sobrescribimos el método mostrar_detalle() heredado
    # de Servicio para agregar información específica
    # sobre el tipo de cabello.
    # El método mantiene el mismo nombre, pero adapta
    # su comportamiento según la clase que lo implementa.
    def mostrar_detalle(self, incluir_precio=True):
        return (
            f"{super().mostrar_detalle(incluir_precio)}, "
            f"Tipo de cabello: {self.tipo_cabello}"
        )
    

    
