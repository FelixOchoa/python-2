# Modulos

def menu() -> int:
    try:
        print("\n\nSistema de gestión de Restaurante")
        print("\n1. Agregar un restaurante.")
        print("2. Ver todos los restaurantes.")
        print("3. Eliminar un restaurante.")
        print("4. Mostrar restaurantes por tipo.")
        print("5. Salir del programa.")

        opcion = int(input("Seleccione una opción: "))
        return opcion
    except Exception as e:
        print(f"Ocurrió el siguiente error: {e}")

def agregar_restaurante(restaurantes: list):
    try:

        controlador = True

        while controlador:
            print("\n\nAgregar un restaurante")

            nombre = input("Nombre del restaurante: ")
            tipo = input("Tipo de comida / Restaurante: ")
            direccion = input("Dirección del restaurante: ")

            restaurante = {
                "ID": obtener_indice_restaurante(restaurantes),
                "informacion": {
                    "nombre": nombre,
                    "tipo": tipo,
                    "direccion": direccion
                }
            }

            restaurantes.append(restaurante)

            opcion = input("\n¿Desea agregar otro restaurante? (s/n): ").upper()

            while (opcion != "S" and opcion != "N"):
                opcion = input("\nOpción no válida. ¿Desea agregar otro restaurante? (s/n): ").upper()
            else:
                if (opcion == "N"):
                    controlador = False
                elif (opcion == "S"):
                    continue

    except Exception as e:
        print(f"Ocurrió el siguiente error: {e}")


def mostrar_restaurantes(restaurantes: list):
    try:
        print("\n\nLista de restaurantes")
        for restaurante in restaurantes:
            print(f"ID: {restaurante['ID']}")
            print(f"Nombre: {restaurante['informacion']['nombre']}")
            print(f"Tipo: {restaurante['informacion']['tipo']}")
            print(f"Dirección: {restaurante['informacion']['direccion']}")
            print()
    except Exception as e:
        print(f"Ocurrió el siguiente error: {e}")

def eliminar_restaurante(restaurantes: list):
    try:
        tipo_busqueda = input("\n\n¿Desea buscar por ID o por nombre? (ID/nombre): ").upper()

        if (tipo_busqueda == "ID"):
            id_busqueda = int(input("\nIngrese el ID del restaurante a eliminar: "))

            for restaurante in restaurantes:
                if (restaurante["ID"] == id_busqueda):
                    restaurantes.remove(restaurante)
                    print("Restaurante eliminado correctamente.")
                    break
            else:
                print("Restaurante no encontrado.")

        elif (tipo_busqueda == "NOMBRE"):
            nombre_busqueda = input("\nIngrese el nombre del restaurante a eliminar: ")

            for restaurante in restaurantes:
                if (restaurante["informacion"]["nombre"] == nombre_busqueda):
                    restaurantes.remove(restaurante)
                    print("Restaurante eliminado correctamente.")
                    break
            else:
                print("Restaurante no encontrado.")
        else:
            print("Opción no válida.")
    except Exception as e:
        print(f"Ocurrió el siguiente error: {e}")

def mostrar_restaurantes_por_tipo(restaurantes: list):
    try:
        controlador = True

        while controlador:

            tipo = input("\n\nIngrese el Tipo de comida / Restaurante: ")

            for restaurante in restaurantes:
                if (restaurante['informacion']['tipo'] == tipo):
                    print(f"\nID: {restaurante['ID']}")
                    print(f"Nombre: {restaurante['informacion']['nombre']}")
                    print(f"Tipo: {restaurante['informacion']['tipo']}")
                    print(f"Dirección: {restaurante['informacion']['direccion']}")
            else:
                print("\nNo existen restaurantes con ese tipo de comida / restaurante.")

                opcion = input("\n¿Desea buscar otro tipo de restaurante? (s/n): ").upper()

                while (opcion != "S" and opcion != "N"):
                    opcion = input("\nOpción no válida. ¿Desea buscar otro tipo de restaurante? (s/n): ").upper()
                else:
                    if (opcion == "N"):
                        controlador = False
                    elif (opcion == "S"):
                        continue

    except Exception as e:
        print(f"Ocurrió el siguiente error: {e}")
def obtener_indice_restaurante(restaurantes: list, aux = 0) -> int:
    for restaurante in restaurantes:
        if (aux < restaurante["ID"]):
            aux = restaurante["ID"]
    return aux + 1