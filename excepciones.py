# try:
#     numerador = float(input('Numerador: '))
#     denominador = float(input('Denominador: '))
#     cociente = numerador / denominador
# except ZeroDivisionError:
#     print('Error: el denominador es nulo')
# except ValueError:
#     print('Error: el valor introducido no es un número válido')
# else:
#     print(f'{numerador}/{denominador} = {cociente}')
# finally:
#     print('\nFin del programa.')
#


num1 = (input("Digita el primer número: "))

if ( num1 == ""):
    print("No has digitado ningún número.")
    exit()

num2 = float(input("Digita el segundo número: "))
num3 = float(input("Digita el tercer número: "))

lista = [num1, num2, num3]

try:
    division = lista[0] / lista[2]
except:
    print('Error: ocurrió un error al momento de ejecutar la divisón.')
else:
    print('La división es: ', division)
finally:
    print('Fin del programa.')


