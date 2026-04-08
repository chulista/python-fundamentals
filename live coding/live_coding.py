# el usuario tiene que ingresar por pantall 2 numeros y los que tiene que el programa tiene que hacer por pantalla 
#if numero 1 es mayor que numero 2, print numero 1 or numero 2 es mayor que numero 1, print numero 2
#else numero 1 == numero 2, print ambos numeros ingresados son iguales

'''
num1 = input("Ingrese un numero entero: ")
num2 = input("Ingrese otro numero entero: ")


if num1.isdigit() and num2.isdigit():
    print(f"Los numeros ingresados son {num1} y {num2}")   
    numero1=int(num1)
    numero2=int(num2)
    
    if numero1 > numero2:
        print("El mayor numero ingresado es", numero1)
    elif numero2 > numero1:
        print("El mayor numero ingresado es:", numero2)
    else:
        print("Ambos numeros ingresados son iguales")

else:
    print("ERROR, Ingrese un numero valido.")
'''

   
'''  
while True:
    ingreso = input("Ingrese su nombre:")
    print(ingreso)
    
    seguir = input("Desea continuar? (S/N)").strip().lower()
    if seguir != "s":
        break
'''

while True:
    num1 = input("Ingrese un numero entero: ").strip()
    num2 = input("Ingrese otro numero entero: ").strip()

    if num1.isdigit() and num2.isdigit():
        print(f"Los numeros ingresados son {num1} y {num2}")   
        numero1=int(num1)
        numero2=int(num2)
        if numero1 > numero2:
            print("El mayor numero ingresado es", numero1)
        elif numero2 > numero1:
            print("El mayor numero ingresado es:", numero2)
        else:
            print("Ambos numeros ingresados son iguales")

        seguir = input("Desea continuar? (S/N)").strip().lower()
        if seguir != "s":
            print("El programa a dejado de ejecutarse.")
            break

    else:
        print("ERROR, Ingrese un numero valido.")
            