from datetime import datetime

#Creamos lista de usuarios
usuarios = []

while True:
    #Mostramos menu principal con 3 opciones
    print("\n\t--- MENÚ PRINCIPAL ---")
    print("\t1.Registrar nuevo usuario")
    print("\t2.Ingresar")
    print("\t3.Salir")
    opcion = input("\tSeleccione una opción: ")

    #Acciones del menu
        #Registramos usuario
    if(opcion == '1'):
        usuario = input("\n\tIngrese un nombre de usuario: ")

        #Verificamos que el usuario no fue ingresado anteriormente
        if usuario in usuarios:
            print("\t 🟡 El usuario ya esta registrado.")

        else:
            usuarios.append(usuario)
            print("\t🟢 Usuario registrado con éxito.")

        #Verifica si el usuario existe en la lista y si es asi, ingresa al programa principal
    elif(opcion == '2'):
        usuarioLogin = input("\n\tIngrese su nombre de usuario: ")
        if usuarioLogin in usuarios:
            print(f"\t🟢 Bienvenido {usuarioLogin}!")
            
            #Bucle del programa principal
            while True:
                print("\n\t--- PROGRAMA PRINCIPAL ---")
                print("\t1.Ver hora actual")
                print("\t2.Volver")
                opcion2 = input("\tSeleccione una opción: ")

                #Acciones de las opciones
                if(opcion2 == '1'):
                    ahora = datetime.now()
                    hora_actual = ahora.strftime("%H:%M:%S")
                    print(f"\n\t🕓 La hora actual es: {hora_actual}")

                elif(opcion2 == '2'):
                    print("\tVolviendo...")
                    break
                else: print("\t❌ Ingrese una opción valida.")
        else: print(f"\t❌ El usuario {usuarioLogin} es incorrecto.")

        #Sale del programa 
    elif(opcion == '3'):
        print("\tSaliendo...")
        break
    else: print("\t❌ Ingrese una opción valida.")

