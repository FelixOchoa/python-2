
from Gestion_Restaurante import menu, agregar_restaurante, mostrar_restaurantes, eliminar_restaurante, mostrar_restaurantes_por_tipo

restaurantes = [
{
    "ID": 1,
    "informacion": {
        "nombre": "La Casa de Toño",
        "tipo": "Mexicana",
        "direccion": "Av. Insurgentes Sur 434",
    }
}
]

controlador = True

while controlador:

    opcion = menu()

    match opcion:
        case 1:
            agregar_restaurante(restaurantes)
        case 2:
            mostrar_restaurantes(restaurantes)
        case 3:
            eliminar_restaurante(restaurantes)
        case 4:
            mostrar_restaurantes_por_tipo(restaurantes)
        case 5:
            print("Saliendo del programa...")
            controlador = False