#Lista de productos
#productos = []
productos = ['Coca','Cigarrillos','Mentas'] #productos ejemplo

#Booleanos para los bucles
menu_activo = True


#Bucle para opciones (menu)
while (menu_activo):
    en_agregar = True
    print("\n---------------------")
    print("1.Agregar productos")
    print("2.Verificar productos")
    print("3.Mostrar productos")
    print("0.Salir")
    print("---------------------")
    opcion = input("Ingrese una opción: ")
    
    #Condicional para la opcion
    #Agregar productos
    if(opcion == '1'):
        #Bucle para agregar
        while(en_agregar):
            print("\n-----------------")
            print("1.Agregar productos")
            print("2.Volver")
            print("-------------------")
            opcion_agregar = input("Ingrese una opcion: ")
            #Condicional para el menu
            if(opcion_agregar == '1'):
                producto = input("\n\tIngrese nombre del producto: ")
            #Verificamos
                if producto in productos:
                    print("\tEl producto ya está en la lista.")
                else:
                    productos.append(producto)
                    print("\tProducto agregado con éxito!")
            elif(opcion_agregar == '2'):
                print("Volviendo...")
                en_agregar = False
            else:print("Ingrese una opción valida.")
                
    #Verificar productos
    elif(opcion == '2'):
        productoVerifi = input("\n\tIngrese el nombre del producto: ")
        #Verificamos
        if productoVerifi in productos:
            print(f"\tEl producto {productoVerifi} esta en la posicion {productos.index(productoVerifi)}")
        else: print("\tEl producto no se encuentra en la lista.")
    #Mostrar productos
    elif(opcion == '3'):
        print("\n\tProductos -->")
        for i in range(len(productos)):
            print(f"\t{i + 1}",productos[i])
    #Salir
    elif(opcion == '0'):
        print("Saliendo...")
        menu_activo = False
    else: print("Ingrese una opción valida.")