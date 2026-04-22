"""
import random

numeros = []

print("===BIENVENIDO AL BINGO===")

for i in range(25): # Le pide al usuario 25 numeros
    while True:
        numero = input("Ingrese un numero del 1 al 75: ")
        if not numero.isdigit():
            print("Debe ingresar solo numeros entre el 1 y el 75")
            continue
            
        numero = int(numero)

        if numero < 1 or numero > 75:
            print("Debe ingresar solo numeros entre el 1 y el 75")
            continue
        elif numero in numeros:
            print("Ese numero ya esta")
            continue

        numeros.append(numero)


carton = [1, 2, 3]
carton_ordenado = []

cantidad_numeros = 11
bolillero = []

for i in range (1, cantidad_numeros):
            bolillero.append(i)
print(bolillero)

while True:
    extraer_bola = input("Presione para extrar una bola (s/n): ").strip().lower()
    if extraer_bola == "s":
        while True:
                bolilla = random.randint(1, cantidad_numeros)
                if bolilla in bolillero:
                    bolillero.remove(bolilla)
                    print(f"El numero eliminado en la vuelta  es el {bolilla}")
                else:
                    continue
                print(f"Su nueva lista es {bolillero}")
                if not bolillero:
                      print("Se terminaron las bolas, termino el juego...")
                break
    elif extraer_bola == "n":
        print("Dejo de extraer bolas...")
        break
    else:
        print("Opcion incorrecta...")

if not carton == carton_ordenado:
    carton_ordenado.sort()
    if carton == carton_ordenado:
        print("Carton lleno")


lista = []

for i in range(1, 6):
    lista.append(i)
print(lista)



bolilla = random.randint(1, 5)
lista.remove(bolilla)
print(f"El numero eliminado es {bolilla}")
print(f"Su nueva lista es {lista}")
"""

import random

jugar_de_nuevo = "s"

while jugar_de_nuevo == "s":

    # --- Cargar cartón ingresado por el usuario ---
    numeros = []
    print("===BIENVENIDO AL BINGO===")

    while len(numeros) < 25:
        numero = input(f"Ingrese un numero del 1 al 75 ({len(numeros) + 1}/25): ")

        if not numero.isdigit():
            print("Debe ingresar solo numeros entre el 1 y el 75")
            continue

        numero = int(numero)

        if numero < 1 or numero > 75:
            print("Debe ingresar solo numeros entre el 1 y el 75")
            continue
        elif numero in numeros:
            print("Ese numero ya esta")
            continue

        numeros.append(numero)

    # --- Armar cartón 5x5 ---
    carton = []
    for fila in range(5):
        carton.append(numeros[fila * 5 : fila * 5 + 5])

    # --- Mostrar cartón ---
    print("\nTu carton:")
    print("+------" * 5 + "+")
    for fila in carton:
        fila_str = ""
        for celda in fila:
            fila_str += f"|  {celda:2d}  "
        print(fila_str + "|")
        print("+------" * 5 + "+")

    # --- Bolillero ---
    bolillero = list(range(1, 76))
    random.shuffle(bolillero)
    cantados = []
    ganaste = False

    # --- Loop principal ---
    for bola in bolillero:
        input("\nPresione ENTER para extraer una bola...")
        cantados.append(bola)
        print(f"El numero extraido es el {bola}")

        # Avisar si el número está en el cartón
        for fila in carton:
            if bola in fila:
                print(f"¡El {bola} esta en tu carton!")

        # Mostrar cartón actualizado
        print()
        print("+------" * 5 + "+")
        for fila in carton:
            fila_str = ""
            for celda in fila:
                if celda in cantados:
                    fila_str += f"| [{celda:2d}] "
                else:
                    fila_str += f"|  {celda:2d}  "
            print(fila_str + "|")
            print("+------" * 5 + "+")

        # Verificar filas
        for fila in carton:
            fila_completa = True
            for celda in fila:
                if celda not in cantados:
                    fila_completa = False
                    break
            if fila_completa:
                ganaste = True
                break

        # Verificar columnas
        if not ganaste:
            for col in range(5):
                col_completa = True
                for fila in range(5):
                    if carton[fila][col] not in cantados:
                        col_completa = False
                        break
                if col_completa:
                    ganaste = True
                    break

        # Verificar diagonal principal
        if not ganaste:
            diag1 = True
            for i in range(5):
                if carton[i][i] not in cantados:
                    diag1 = False
                    break
            if diag1:
                ganaste = True

        # Verificar diagonal secundaria
        if not ganaste:
            diag2 = True
            for i in range(5):
                if carton[i][4 - i] not in cantados:
                    diag2 = False
                    break
            if diag2:
                ganaste = True

        if ganaste:
            print("\n¡¡¡BINGO!!! ¡Ganaste!")
            break

    if not ganaste:
        print("\nSe terminaron las bolas. ¡Mejor suerte la proxima!")

    jugar_de_nuevo = input("\n¿Desea jugar de nuevo? (s/n): ").strip().lower()

print("\n¡Hasta la proxima!")