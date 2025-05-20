import re

correo = input('Ingrese su correo: ')

if '@gmail.com' in correo:
    print('\t\nEl correo es valido')
else:
    print('\t\nEl correo no es valido')
            

exit = False
cadenaDesafio = 'antidisestablishmentarianism'
contadorDesafio = 0

for i in cadenaDesafio:
        if(i == 'a'):
            contadorDesafio = contadorDesafio + 1
            
while (exit == False):
    
    print(" ")
    cadena = input("Ingrese una frase: ")
    cantCaracteres = len(cadena)
    contadorCaracteres = 0;
    
    for i in range(cantCaracteres):
        contadorCaracteres = contadorCaracteres + 1 
        
    if (cadena == "Programacion"):
        inputDesafio = int(input("\n\tIngrese la cantidad de vocales 'a' de '"+ cadenaDesafio + "': "))
        if(inputDesafio == 4):
            print("\n\t->Saliendo...")
            print(" ")
            exit = True
        else:
            print("\n\t-> No puede salir :(")
    elif(cadena == ""):
        print('\n\tIngrese un caracter no nulo')
        
    elif(contadorCaracteres >= 10):
        print("\n\tEl numero de caracteres de la cadena '" + cadena + "' es de: " + str(contadorCaracteres))
    elif(contadorCaracteres < 10):
        cadena = "" 
    
