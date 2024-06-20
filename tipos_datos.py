import math


# 1. Escribe un programa que calcule el área de un círculo dada su radio.
#print("Calcular el área de un círculo")

#radio = float(input("Digita el radio del círculo: "))
#areaCirculo = math.pi * (radio ** 2) 

#print("Pi vale: ", math.pi)
#print("El área del círculo es: ", areaCirculo)


# 2. Escribe un programa que calcule el promedio de tres números dados.

#num1 = float(input("Digita el primer número: "))
#num2 = float(input("Digita el segundo número: "))
#num3 = float(input("Digita el tercer número: "))

#promedio = (num1 + num2 + num3) / 3

#print("El promedio de los tres números es: ", promedio)

# 3. Escribe un programa que convierta una temperatura dada en grados Celsius a grados Fahrenheit.

# celsius = float(input("Digita la temperatura en grados Celsius: "))
#fahrenheit = (celsius * 9/5) + 32

#print("La temperatura en grados Fahrenheit es: ", fahrenheit)



def saludar(nombre):
    saludo = "Hola, " + nombre + "!"
    return saludo

# Llamar a la función
mensaje = saludar("Juan")
print(mensaje)  # Salida: Hola, Juan!


