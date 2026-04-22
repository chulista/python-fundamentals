from unittest import case

# 1. Ingresar carton de bingo
carton = [] #25 elementos porque el carton es de 5x5

# 1. Cargar carton
# 2. Jugar al bingo
# 3. Salir
opcion = 3
while opcion != "3":
    print("Elija una opcion: ")
    print("1. Cargar carton")
    print("2. Jugar al bingo")
    print("3. Salir")

    opcion = input("Ingrese una opcion: ")
    match opcion:
        case "1":
            print("\tCargar carton")
        case "2":
            print("\tJugar al bingo")
        case "3":
            print("\tSalir")
        case _: # Default
            print("\tOpcion invalida")