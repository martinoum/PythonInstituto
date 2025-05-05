import pygame

print("*** CALCULADORA ***")
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
        pygame.mixer.init()#Inicializa el mezclador de Pygame
        pygame.mixer.music.load('confeti.mp3') #Cargamos el archivo
        pygame.mixer.music.play()
        pygame.mixer.music.set_volume(0.2)
    elif (opcion == "2") :
        res = num1 - num2
        print("El resultado es:",res)
        pygame.mixer.init()#Inicializa el mezclador de Pygame
        pygame.mixer.music.load('confeti.mp3') #Cargamos el archivo
        pygame.mixer.music.play()
        pygame.mixer.music.set_volume(0.2)
    elif (opcion == "3") :
        res = num1 * num2 
        print("El resultado es:",res)
        pygame.mixer.init()#Inicializa el mezclador de Pygame
        pygame.mixer.music.load('confeti.mp3') #Cargamos el archivo
        pygame.mixer.music.play()
        pygame.mixer.music.set_volume(0.2)
    elif (opcion == "4") :
        res = num1 / num2
        print("El resultado es:",res)
        pygame.mixer.init()#Inicializa el mezclador de Pygame
        pygame.mixer.music.load('confeti.mp3') #Cargamos el archivo
        pygame.mixer.music.play()
        pygame.mixer.music.set_volume(0.2)
    elif (opcion == "5") :
        res = num1 % num2
        print("El resultado es:",res)
        pygame.mixer.init()#Inicializa el mezclador de Pygame
        pygame.mixer.music.load('confeti.mp3') #Cargamos el archivo
        pygame.mixer.music.play()
        pygame.mixer.music.set_volume(0.2)
    elif (opcion == "0"):
        pygame.mixer.init()#Inicializa el mezclador de Pygame
        pygame.mixer.music.load('triste.mp3') #Cargamos el archivo
        pygame.mixer.music.play()
        pygame.mixer.music.set_volume(0.2)
        print("SALIENDO..")
        isOpcion = False
    else:
        print("Ingrese una opción valida")



