
class PrecioInvalidoError(Exception):
    """
    Excepción personalizada que se genera cuando
    se intenta asignar un precio menor o igual a cero
    a un servicio del salón de belleza.
    """
    pass
