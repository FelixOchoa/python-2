from math import pi
from mimodulo import menu, añadir_numeros, mostrar_numeros, sumar_numeros

# Función que calcule el area de un círculo dado su radio

# def area_circulo(radio: float):
#     area = pi * radio ** 2
#     return area
#
# Función que calcule el area de un triángulo dado su base y su altura

# def area_triangulo(base: float, altura: float):
#     area = (base * altura) / 2
#     return area

# Función que imprima un mensaje de saludo

# def saludo():
#     print("¡Hola! ¿Cómo estás?")
#
# def saludo_predeterminado(nombre = "desconocido"):
#     print(f"¡Hola {nombre}! ¿Cómo estás?")


# Función que calcula el peso de una persona en otro planeta, dado su peso en la Tierra y la gravedad del planeta

# def peso_en_otro_planeta(peso, gravedad_planeta = 9.81):
#     gravedad_tierra = 9.81
#     peso_planeta = peso * (gravedad_planeta / gravedad_tierra)
#     return peso_planeta

# # Función para determinar si un número es par o impar

# # Función para contar las vocales de una cadena de texto


# Utilizar listas, funciones, y ciclos

# 1. Función que se encargue de mostrar en pantalla lo que se va a realizar :

#  Programa que trabaja con listas
#  1. Añadir números a una lista.
#  2. Mostrar los números de la lista.
#  3. Sumar todos los números de la lista y mostrar el resultado.
#  4. Salir

#  Seleccionar una opción: _

# 2. Función por cada uno de los puntos que tendrá la aplicación

# 3. Utilizar ciclos para que el programa se ejecute hasta que el usuario seleccione la opción de salir

lista = []

controlador = True

while controlador:
    opcion = menu()

    match opcion:
        case 1:
            añadir_numeros(lista)
        case 2:
            mostrar_numeros(lista)
        case 3:
            sumar_numeros(lista)
        case 4:
            controlador = False
            print("¡Hasta luego!")
        case _:
            print("Opción inválida. Intente nuevamente.")

