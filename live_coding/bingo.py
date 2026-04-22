import random

from unittest import case
# 1. Ingresar carton de bingo
tamanio_carton = 25
carton = [] #25 elementos porque el carton es de 5x5

# 2. Cargar el bolillero
tamanio_bolillero = 75
bolillero = []
for i in range (1, tamanio_bolillero+1):
    bolillero.append(i)

# 3. estado del juego. Definido por la cantidad de Aciertos en el Carton
hits_count = 0
#hay_ganador = False

print("Bolillero Cargado Listo para jugar al Bingo!")

# 1. Cargar carton
# 2. Jugar al bingo
# 3. Salir
opcion = ""
while opcion != "6":
    print("Elija una opcion: ")
    print("1. Inicializar carton")
    print("2. Cargar carton")
    print("3. Jugar al bingo")
    print("4. Mostrar Carton")
    print("5. Cargar Carton Automatico")
    print("6. Salir")

    opcion = input("Ingrese una opcion: ")
    match opcion:
        case "1":
            print("\tInicializar carton")
            for i in range (0,tamanio_carton):
                carton.append(0)
            print(f"\t==> tamaño del carton {len(carton)}")

            ##Mostrar Carton 5x5
            for i in range(0,5):
                print('\t\t', carton[i * 5], " | ", carton[i * 5 + 1], " | ", carton[i * 5 + 2], " | ",
                      carton[i * 5 + 3], " | ", carton[i * 5 + 4])
        case "2":
            print("\tCargar carton")
            cant_numeros_ingresados = 0
            while cant_numeros_ingresados < tamanio_carton:
                #TODO: agregar validacion de numero valido
                #TODO: validar numero mayor a cero y que no sea letra
                numero = int(input("Ingrese un numero: "))
                if numero not in carton:
                    print(f"\tNumero {cant_numeros_ingresados+1}/{tamanio_carton} Ingresado")
                    carton[cant_numeros_ingresados] = numero
                    cant_numeros_ingresados += 1
                else:
                    print("\t\t ERROR: numero ya ingresado")
            ##Mostrar Carton 5x5
            for i in range(0,5):
                print('\t\t', carton[i * 5], " | ", carton[i * 5 + 1], " | ", carton[i * 5 + 2], " | ",
                      carton[i * 5 + 3], " | ", carton[i * 5 + 4])
        case "3":
            print("\tJugar al bingo")
            ## Me aseguro de que NO se intente sacar mas de 1 vez el mismo numero
            bolilla = 0
            bolilla_en_bolillero = False
            while not bolilla_en_bolillero:
                bolilla = random.randint(1, tamanio_bolillero) ## saca 1 bolilla aleatoria del 1 al 75
                if bolilla in bolillero:
                    print(f"\t\tbolilla sacada ({bolilla})")
                    bolilla_en_bolillero = True

            bolillero.remove(bolilla)

            
            if "X" in carton[0] and "X" in carton[1] and "X" in carton[2] and "X" in carton[3] and "X" in carton[4]:
                print("Ganaste por fila 1!")
            elif "X" in carton[5] and "X" in carton[6] and "X" in carton[7] and "X" in carton[8] and "X" in carton[9]:
                print("Ganaste por fila 2!")
            elif "X" in carton[10] and "X" in carton[11] and "X" in carton[12] and "X" in carton[13] and "X" in carton[14]:
                print("Ganaste por fila 3!")
            elif "X" in carton[15] and "X" in carton[16] and "X" in carton[17] and "X" in carton[18] and "X" in carton[19]:
                print("Ganaste por fila 4!")
            elif "X" in carton[20] and "X" in carton[21] and "X" in carton[22] and "X" in carton[23] and "X" in carton[24]:
                print("Ganaste por fila 5!")

            elif "X" in carton[0] and "X" in carton[5] and "X" in carton[10] and "X" in carton[15] and "X" in carton[20]:
                print("Ganaste por columna 1!")
            elif "X" in carton[1] and "X" in carton[6] and "X" in carton[11] and "X" in carton[16] and "X" in carton[21]:
                print("Ganaste por columna 2!")
            elif "X" in carton[2] and "X" in carton[7] and "X" in carton[12] and "X" in carton[17] and "X" in carton[22]:
                print("Ganaste por columna 3!")
            elif "X" in carton[3] and "X" in carton[8] and "X" in carton[13] and "X" in carton[18] and "X" in carton[23]:
                print("Ganaste por columna 4!")
            elif "X" in carton[4] and "X" in carton[9] and "X" in carton[14] and "X" in carton[19] and "X" in carton[24]:
                print("Ganaste por columna 5!")

            elif "X" in carton[0] and "X" in carton[6] and "X" in carton[12] and "X" in carton[18] and "X" in carton[24]:
                print("Ganaste por diagonal principal!")
            elif "X" in carton[4] and "X" in carton[8] and "X" in carton[12] and "X" in carton[16] and "X" in carton[20]:
                print("Ganaste por diagonal inversa!")

            if bolilla in carton:
                print(f"\t\t\tla bolilla ({bolilla}) ESTÁ en el cartón")
                indice = carton.index(bolilla) ## en que posicion está este numero?
                carton[indice] = str(carton[indice]) + '✅'
                hits_count += 1
            if hits_count == tamanio_carton:
                #hay_ganador = True
                print("\tHas ganado!!!")

        case "4":
            print("\tMostrar Carton")
            for i in range(0,5):
                print('\t\t', carton[i * 5], " | ", carton[i * 5 + 1], " | ", carton[i * 5 + 2], " | ",
                      carton[i * 5 + 3], " | ", carton[i * 5 + 4])
        case "5":
            print("\tCargar Carton Automatico")
            carton_cargado = False
            numeros_cargados = 0
            while not carton_cargado:
                numero_aleatorio = random.randint(1, tamanio_bolillero)
                if numero_aleatorio not in carton:
                    carton[numeros_cargados] = numero_aleatorio
                    numeros_cargados += 1

                if numeros_cargados == tamanio_carton:
                    carton_cargado = True

            for i in range(0,5):
                print('\t\t', carton[i * 5], " | ", carton[i * 5 + 1], " | ", carton[i * 5 + 2], " | ",
                      carton[i * 5 + 3], " | ", carton[i * 5 + 4])
        case "6":
            print("\tSalir")
        case _: # Default
            print("\tOpcion invalida")