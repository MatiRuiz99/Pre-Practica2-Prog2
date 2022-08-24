#Crear un programa que permita al usuario ingresar una lista de numeros. De esa lista de numeros almacenar en otra lista los numeros impares.

#El programa debe de mostrar por pantalla la lista de numeros originales y la lista de numeros impares.

#INICIO
i = 0
lista = []
listaimpar = []

for i in range(4):
    lista.append(int(input("Ingrese un numero: ")))
    if lista[i] % 2 != 0:
        listaimpar.append(lista[i])

print(lista)
print(listaimpar)
#FIN