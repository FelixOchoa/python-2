# Un bucle para garantizar que el mes introducido es correcto

# mes = int(input("Introduzca el mes del año (entre 1 y 12): "))
#
# while mes > 12 or mes < 1:
#     print("Mes introducido incorrecto. Inténtelo de nuevo.")
#     mes = int(input("Introduzca el mes del año (entre 1 y 12):"))
#
# print(f'El mes {mes} es válido.')


# Un bucle para garantizar que el mes introducido es correcto. Versión alternativa.

mes_correcto = False
while not mes_correcto:
    mes = int(input("Introduzca el mes del año (entre 1 y 12):"))
     if mes > 12 or mes < 1:
         print("Mes introducido incorrecto. Inténtelo de nuevo")
     else:
        mes_correcto = True

print(f'El mes {mes} es válido.')
#
#
# Bucle controlado por un contador que suma un determinado conjunto de reales. (Versión 1)
#
# contador = int(input('Diga cuantos números reales quiere sumar: '))
#
# suma = 0.0
# ## Ciclo While

# # contador = 1
# #
# # while contador <= 5:
# #     print(contador)
# #     contador += 1   # contador = contador + 1  # Incrementa el valor del contador en 1

# # Un bucle para garantizar que el mes introducido es correcto

# # mes = int(input("Introduzca el mes del año (entre 1 y 12): "))
# #
# # while mes > 12 or mes < 1:
# #     print("Mes introducido incorrecto. Inténtelo de nuevo.")
# #     mes = int(input("Introduzca el mes del año (entre 1 y 12):"))
# #
# # print(f'El mes {mes} es válido.')


# # Un bucle para garantizar que el mes introducido es correcto. Versión alternativa.

# # mes_correcto = False
# # while not mes_correcto:
# #     mes = int(input("Introduzca el mes del año (entre 1 y 12):"))
# #     if mes > 12 or mes < 1:
# #         print("Mes introducido incorrecto. Inténtelo de nuevo")
# #     else:
# #         mes_correcto = True
# #
# # print(f'El mes {mes} es válido.')
# #
# #
# # Bucle controlado por un contador que suma un determinado conjunto de reales. (Versión 1)
# #
# # contador = int(input('Diga cuantos números reales quiere sumar: '))
# #
# # suma = 0.0
# # while contador > 0:
# #     valor = float(input('Dame un valor real: '))
# #     suma += valor                                       # Equivalente a suma = suma + valor
# #     contador = contador - 1                             # Se podría usar: contador -= 1
# #
# # print("La suma de los números introducidos es", suma)
# # #
# # Bucle controlado por un contador que suma un determinado conjunto de reales. (Versión 2)
# #
# # num_valores = int(input("Diga cuantos números reales quiere sumar: "))
# #
# # suma = 0.0
# # contador = 0
# # while contador < num_valores:
# #     valor = float(input("Deme el valor real {} a sumar: ".format(contador+1)))
# #     suma += valor
# #     contador += 1
# #
# # if num_valores > 0:
# #     print("La suma de los {} números introducidos es {}".format(num_valores, suma))
# # else:
# #     print("El usuario no introdujo ningún valor.")


# # Ciclo For
# #
# # Iterar sobre una lista

# # frutas = ["manzana", "banana", "cereza"]
# #
# # for fruta in frutas:
# #     print(fruta)


# # # Iterar sobre una cadena de texto
# #
# # mensaje = "Hola"
# #
# # for letra in mensaje:
# #     print(letra)
# #
# # Iterar sobre un rango de números

# # for i in range(5):
# #     print(i)

# # Iterar sobre un rango de números con un inicio y un fin

# # for i in range(2, 5):
# #     print(i)

# # Iterar sobre un rango de números con un inicio, un fin y un incremento
# # for i in range(0, 10, 2):
# #     print(i)

# # # Iterar sobre una lista de números
# # numeros = [1, 2, 3, 4, 5]
# #
# # for numero in numeros:
# #     print(numero)
# #
# # # Iterar sobre una lista de números con un índice
# #
# # numeros = [1, 2, 3, 4, 5, 9, 20, 19, 90]
# #
# # for i in range(len(numeros)):
# #     print(f'El número en la posición {i} es {numeros[i]}')
# #
# # print('El tamaño de la lista es:', len(numeros))

# # Iterar sobre una lista de números con un índice y un valor
# #
# # numeros = [9, 32, 33, 1, 0]
# #
# # for i, numero in enumerate(numeros):
# #     print(f'El número en la posición {i} es {numero}')
