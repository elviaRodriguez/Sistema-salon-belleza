class Servicio:

    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

    def mostrar_detalle(self, incluir_precio=True):
     if incluir_precio:
        return f"Servicio: {self.nombre}, Precio: ${self.precio}"
     return f"Servicio: {self.nombre}"



