def menu():
    print("Programa que trabaja con listas\n")
    print("1. Añadir números a una lista.")
    print("2. Mostrar los números de la lista.")
    print("3. Sumar todos los números de la lista y mostrar el resultado.")
    print("4. Salir")
    print("\nSeleccionar una opción: ")
    opcion = int(input())
    return opcion

def añadir_numeros(lista):
    cantidad_numeros = int(input("¿Cuántos números desea añadir a la lista? "))
    for i in range(cantidad_numeros):
        numero = int(input(f"Digite el número {i+1}: "))
        lista.append(numero)

def mostrar_numeros(lista):
    print("Los números de la lista son: ", lista)

def sumar_numeros(lista):
    suma = sum(lista)
    print(f"La suma de los números de la lista es: {suma}")