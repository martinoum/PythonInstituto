# Ejercicio 1

numTabla = int(input("Ingrese un numero entero: "))
i = 1
print("")

while(i <= 10 ):
    print("" + str(numTabla) + " x " + str(i) + " = " + str(numTabla * i))
    i = i + 1
print("")

# Ejercicio 2

i = 10
print("*** CONTANDO HACIA ATRAS *** ")
print("")
while(i > 0):
    print(i)
    i = i-1
print("")

# Ejercicio 3

num1 = int(input("Ingrese numero 1: "))
num2 = int(input("Ingrese numero 2: "))

isOpcion = True
while(isOpcion == True) :
    print(" ")
    print("*********************")
    print("****** OPCIONES *****")
    print("***** 1.SUMAR *****")
    print("***** 2.RESTAR *****")
    print("***** 3.MULTIPLICAR *****")
    print("***** 4.DIVIDIR *****")
    print("***** 5.RESTO  *****")
    print("***** 0.SALIR  *****")
    print("*********************")
    print(" ")
    opcion = input("Ingrese una opción: ")

    if (opcion == "1") :
        res = num1 + num2
        print("El resultado es:",res)
    elif (opcion == "2") :
        res = num1 - num2
        print("El resultado es:",res)
    elif (opcion == "3") :
        res = num1 * num2 
        print("El resultado es:",res)
    elif (opcion == "4") :
        res = num1 / num2
        print("El resultado es:",res)
    elif (opcion == "5") :
        res = num1 % num2
        print("El resultado es:",res)
    elif (opcion == "0"):
        print("SALIENDO..")
        isOpcion = False
    else:
        print("Ingrese una opción valida")
