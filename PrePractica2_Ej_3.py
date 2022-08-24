#Crear un programa que utilice la estructura try - catch. El usuario debe de ingresar dos numeros y mostrar por pantalla
#el resultado de la división entre ambos numeros. 

#En caso de que el divisor sea 0 utilizar la excepción ZeroDivisionError y mostrar el error por pantalla.


#INICIO



num1 = int(input("Ingrese un numero 1: "))
num2 = int(input("Ingrese un numero 2: "))

try:
        a = num1 / num2 
        print(a)
except ZeroDivisionError as exception:
    print(f"Ha ocurrido un error | {exception}")


#FIN