# Ejemplos de condicionales en Python
# 1. Se determina qué número es mayor de dos números dados.

# num1 = float(input("Digita el primer número: "))
# num2 = float(input("Digita el segundo número: "))
#
# if ( num1 > num2 ):
#    print("El número mayor es: ", num1)
# else:
#    print("El número mayor es: ", num2)


# 2. Se determina la edad de una persona en diferentes grupos etarios.
# Nota: Los grupos etarios son los siguientes:
# 0-12 años: Niño
# 13-18 años: Adolescente
# 19-30 años: Joven
# 31-64 años: Adulto

# edad = int(input("Digita tu edad: "))
# if ( edad >= 0 and edad <= 12 ):
#    print("Eres un niño.")
# elif ( edad >= 13 and edad <= 18 ):
#    print("Eres un adolescente.")
# elif ( edad >= 19 and edad <= 30 ):
#    print("Eres un joven.")
# elif ( edad >= 31 and edad <= 64 ):
#    print("Eres un adulto.")
#
# else:
#    print("Eres un adulto mayor.")


# edad = int(input("Digita tu edad: "))
#
# match edad:
#     case edad if edad >= 0 and edad <= 12:
#         print("Eres un niño.")
#     case edad if edad >= 13 and edad <= 18:
#         print("Eres un adolescente.")
#     case edad if edad >= 19 and edad <= 30:
#         print("Eres un joven.")
#     case edad if edad >= 31 and edad <= 64:
#         print("Eres un adulto.")
#     case 80:
#         print("Eres un adulto mayor. Que tiene 80 años")
#     case _:
#         print("Eres un adulto mayor.")

# Ejercicios

# 1. Escribe un programa que determine si un número dado es par o impar.

#num = int(input("Digita un número entero para saber si es par o impar: "))

#if ( num % 2 == 0 ):
#    print(num % 2)
#    print("El número es par.")
#else:
#    print(num % 2)
#    print("El número es impar.") 

# 2. Escribe un programa que compare tres números y determine cuál es el mayor.

#num1 = float(input("Digita el primer número: "))
#num2 = float(input("Digita el segundo número: "))
#num3 = float(input("Digita el tercer número: "))

#if ( num1 > num2 and num1 > num3):
#    print("El número mayor es: ", num1)
#elif ( num2 > num1 and num2 > num3 ):
#    print("El número mayor es: ", num2)
#else:
#    print("El número mayor es: ", num3)

# 3. Escribe un programa que asigne una calificación basada en una puntuación numérica.

# puntuacion = int(input("Digita la puntuación: "))
#
# if ( puntuacion >= 90 and puntuacion <= 100 ):
#     print("La calificación es: A")
# elif ( puntuacion >= 80 and puntuacion <= 89 ):
#     print("La calificación es: B")
# elif ( puntuacion >= 70 and puntuacion <= 79 ):
#     print("La calificación es: C")
# elif ( puntuacion >= 60 and puntuacion <= 69 ):
#     print("La calificación es: D")
# elif ( puntuacion >= 0 and puntuacion <= 59 ):
#     print("La calificación es: F")
# else:
#     print("El número ingresado no corresponde al rango de (0 - 100)")
