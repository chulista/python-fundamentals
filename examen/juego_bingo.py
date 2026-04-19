numeros = []

print("===BIENVENIDO AL BINGO===")

for i in range(25):
    while True:
        numero = input("Ingrese un numero del 1 al 75: ")
        if not numero.isdigit():
            print("Debe ingresar solo numeros entre el 1 y el 75")
            continue
            
        numero = int(numero)

        if numero < 1 and numero > 75:
            print("Debe ingresar solo numeros entre el 1 y el 75")
            continue
        elif numero in numeros:
            print("Ese numero ya esta")
            continue