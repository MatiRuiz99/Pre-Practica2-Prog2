#Crear un programa que permita ingresar una lista de numeros al usuario y muestre por pantalla el maximo entre ambos numeros.

#Nota : Hacerlo con la función max(a,b) y luego con una comparación

#INICIO

from traceback import print_tb

i = 0
mayor = 0
lista = []
lista.append(int(input("Ingrese un numero1: ")))
lista.append(int(input("Ingrese un numero2: ")))
lista.append(int(input("Ingrese un numero3: ")))
maximo = max(lista)
print(lista)
print(maximo)

for i in range(3):
    if i == 0:
        mayor = lista[i]
    else:
        if lista[i] > mayor:
            mayor = lista[i]
        
print(mayor)

#FIN