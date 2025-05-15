
precioTomate = 20
precioLechuga = 30

isTomate = input("¿Hay tomate (s/n)? ")
isLechuga = input("¿Hay lechuga (s/n)? ")

if isTomate == "s" : 
    cantTomate = float(input("Cuantos kilos de tomate quiere? "))
    precioTomate = cantTomate * 20
else : 
    cantTomate = 0 
    precioTomate = 0

if isLechuga == "s" :
    cantLechuga = float(input("Cuantas plantas de lechuga quiere? "))
    precioLechuga = cantLechuga * 30
else:
    cantLechuga = 0    
    precioLechuga = 0
total = precioTomate + precioLechuga
print("----------- VERDULERIA -----------")
print("")
print("Tomate  x",cantTomate,"------------- $",precioTomate)
print("")
print("Lechuga x",cantLechuga,"------------- $",precioLechuga)
print("")
print("----------------------------------")
print("Total --------------------- $", total)
print("  ")

print("EL PROFE SE PODRÁ HACER UNA ENSALADA?")
if isTomate == "s" and isLechuga == "s":
    print("-> SI")
else: 
    print("-> NO")
    

