from modelos.servicio_cabello import ServicioCabello
from modelos.servicio_unas import ServicioUnas
from modelos.servicio_facial import ServicioFacial
from modelos.excepciones import PrecioInvalidoError
from modelos.servicio import Servicio

def mostrar_menu():
    print("\n===== SISTEMA DE SALÓN DE BELLEZA =====")
    print("1. Registrar servicio")
    print("2. Mostrar catálogo y polimorfismo")
    print("3. Validar excepciones")
    print("4. Demostrar sobrecarga y sobrescritura")
    print("5. Procesar servicios con hilos")
    print("6. Guardar servicio en JSON")
    print("7. Recuperar servicio desde JSON")
    print("8. Demostrar composición")
    print("9. Salir")


def registrar_servicio(catalogo):
    print("\n=== REGISTRAR SERVICIO ===")
    print("1. Servicio de cabello")
    print("2. Servicio de uñas")
    print("3. Servicio facial")

    tipo = input("Seleccione el tipo de servicio: ")

    if tipo not in ("1", "2", "3"):
        print("Tipo de servicio no válido.")
        return

    nombre = input("Ingrese el nombre del servicio: ")

    try:
        precio = float(input("Ingrese el precio: "))

        if tipo == "1":
            detalle = input("Ingrese el tipo de cabello: ")
            servicio = ServicioCabello(nombre, precio, detalle)

        elif tipo == "2":
            detalle = input("Ingrese el tipo de esmalte: ")
            servicio = ServicioUnas(nombre, precio, detalle)

        else:
            detalle = input("Ingrese el tipo de tratamiento: ")
            servicio = ServicioFacial(nombre, precio, detalle)

        catalogo.append(servicio)
        print("Servicio registrado correctamente.")

    except (ValueError, PrecioInvalidoError) as error:
        print(f"Error al registrar el servicio: {error}")


def mostrar_catalogo(catalogo):
    print("\n=== CATÁLOGO DE SERVICIOS ===")

    if not catalogo:
        print("No hay servicios registrados.")
        return

    # POLIMORFISMO:
    # La lista contiene objetos de distintas subclases.
    # Todos utilizan el mismo método mostrar_detalle(),
    # pero cada clase responde según su implementación.

    for indice, servicio in enumerate(catalogo, start=1):
        print(f"{indice}. {servicio.mostrar_detalle()}")


def validar_excepciones():
    print("\n=== VALIDACIÓN DE EXCEPCIONES ===")

    # Creamos un servicio con un precio válido.
    servicio = Servicio("Corte de cabello", 15.00)

    print("Precio original:", servicio.precio)

    try:
        # Intentamos asignar un precio inválido.
        servicio.precio = -10

    except PrecioInvalidoError as error:
        print(f"Error controlado: {error}")

    # Comprobamos que el precio original se conserva.
    print("Precio después de la validación:", servicio.precio)


def main():
    catalogo = []

    while True:
        mostrar_menu()

        opcion = input("\nSeleccione una opción: ")

        if opcion == "1":
           registrar_servicio(catalogo)

        elif opcion == "2":
            mostrar_catalogo(catalogo)

        elif opcion == "3":
            validar_excepciones()

        elif opcion == "4":
            print("Demostrar sobrecarga y sobrescritura")

        elif opcion == "5":
            print("Procesar servicios con hilos")

        elif opcion == "6":
            print("Guardar servicio en JSON")

        elif opcion == "7":
            print("Recuperar servicio desde JSON")

        elif opcion == "8":
            print("Demostrar composición")

        elif opcion == "9":
            print("Gracias por utilizar el sistema.")
            break

        else:
            print("Opción no válida. Intente nuevamente.")


if __name__ == "__main__":
    main()
