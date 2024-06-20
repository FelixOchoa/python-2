
MiLista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print("El estado inicial de mi lista es: ", MiLista)

MiLista.append(5)
MiLista.append(89)
MiLista.append(375)

print("El estado actual de mi lista es: ", MiLista)

MiLista[3] = 90
MiLista[4] = 89
MiLista[5] = 90
MiLista[6] = 91

print("La lista después de modificación es: ", MiLista)

ValorExtraid = MiLista.pop(9)

print("La lista después de eliminar un elemento con pop es: ", MiLista)
print("El valor extraído es: ", ValorExtraid)

MiLista.remove(90)

print("La lista después de eliminar un elemento con remove es: ", MiLista)

MiLista.insert(3, 100)

print("La lista después de insertar un elemento es: ", MiLista)



