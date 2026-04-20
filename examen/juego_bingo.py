import random

'''
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
        break
'''
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

"""
lista = []

for i in range(1, 6):
    lista.append(i)
print(lista)



bolilla = random.randint(1, 5)
lista.remove(bolilla)
print(f"El numero eliminado es {bolilla}")
print(f"Su nueva lista es {lista}")
"""