



# 1. Añadir estudiante
# 2. Consultar estudiante por cédula
# 3. Eliminar estudiante por cédula
# 4. Mostrar la nota global de un estudiante por cédula
# 5. Promedio de nota global de todos los estudiantes
# 6. Mostrar todos los estudiantes
# 7. Salir

def menu():
    print("Programa que trabaja con diccionarios")
    print("1. Añadir estudiante")
    print("2. Consultar estudiante por cédula")
    print("3. Eliminar estudiante por cédula")
    print("4. Mostrar la nota global de un estudiante por cédula")
    print("5. Promedio de nota global de todos los estudiantes")
    print("6. Mostrar todos los estudiantes")
    print("7. Salir")
    opcion = int(input("Seleccione una opción: "))
    return opcion


lista_estudiantes = [{
    "nombre": "Felix Ochoa",
    "cedula": "123456789",
    "edad": 25,
    "notaGlobal": 4.4
}]

def añadir_estudiante(lista_estudiantes):

    nombre = input("Ingrese el nombre del estudiante: ")
    cedula = input("Ingrese la cédula del estudiante: ")
    edad = int(input("Ingrese la edad del estudiante: "))
    nota_global = float(input("Ingrese la nota global del estudiante: "))

    estudiante = {
        "nombre": nombre,
        "cedula": cedula,
        "edad": edad,
        "notaGlobal": nota_global
    }

    lista_estudiantes.append(estudiante)

    print("Estudiante añadido correctamente.")

def consultar_estudiante(lista_estudiantes, cedula):
        for estudiante in lista_estudiantes:
            if estudiante["cedula"] == cedula:
                print(estudiante)
                break
        else:
            print("Estudiante no encontrado.")

def eliminar_estudiante(lista_estudiantes, cedula):
    for estudiante in lista_estudiantes:
        if estudiante["cedula"] == cedula:
            lista_estudiantes.remove(estudiante)
            print("Estudiante eliminado correctamente.")
            break
    else:
        print("Estudiante no encontrado.")

def consultar_nota_global(lista_estudiantes, cedula):
    for estudiante in lista_estudiantes:
        if estudiante["cedula"] == cedula:
            print(f"La nota global del estudiante es: {estudiante['notaGlobal']}")
            break
    else:
        print("Estudiante no encontrado.")

def promedio_nota_global(lista_estudiantes):
    acumulador = 0
    for estudiante in lista_estudiantes:
        acumulador += estudiante["notaGlobal"]

    promedio = acumulador / len(lista_estudiantes)
    print(f"El promedio de nota global de los estudiantes es: {promedio}")

def mostrar_estudiantes(lista_estudiantes):
    print(lista_estudiantes)

controlador = True

while controlador:
    opcion = menu()

    match opcion:
        case 1:
            añadir_estudiante(lista_estudiantes)
        case 2:
            cedula_a_buscar = (input("Ingrese la cédula del estudiante a buscar: "))
            consultar_estudiante(lista_estudiantes, cedula_a_buscar)
        case 3:
            cedula_a_buscar = (input("Ingrese la cédula del estudiante a buscar: "))
            eliminar_estudiante(lista_estudiantes, cedula_a_buscar)
        case 4:
            cedula_a_buscar = (input("Ingrese la cédula del estudiante a buscar: "))
            consultar_nota_global(lista_estudiantes, cedula_a_buscar)
        case 5:
            promedio_nota_global(lista_estudiantes)
        case 6:
            mostrar_estudiantes(lista_estudiantes)
        case 7:
            controlador = False
            print("Muchas gracias por utilizar el programa.")
        case _:
            print("Opción inválida. Intente nuevamente.")