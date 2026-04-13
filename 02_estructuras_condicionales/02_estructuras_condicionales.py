#Ejercicio 1

'''
letra = input("Ingrese una letra: ").upper()

if letra in ["A", "E", "I", "O", "U"]:
    print("Es vocal")
else:
    print("No es vocal")
'''

#Ejercicio 2

'''
numero = int(input("Ingrese un numero entero: "))

if numero >= 0:
    valor_absoluto = numero
else: 
    valor_absoluto = numero * -1

print("El valor absoluto es:", valor_absoluto)
'''

#Ejercicio 3

'''
palabra1 = input("Ingrese la palabra 1: ").lower()
palabra2 = input("Ingrese la palabra 2: ").lower()

if palabra1[-3:] == palabra2[-3:]:
    print("Riman")
elif palabra1[-2:] == palabra2[-3:]:
    print("Riman poco")
else:
    print("No riman")
'''

#Ejercicio 4

'''
candidato = input("""    ===Candidatos===
                  
    Candidato A: Partido rojo
    Candidato B: Partido verde 
    Candidato C: Partido azul
    
    Elija su candidato: """).upper()

if candidato == "A":
    print("Usted ha votado por el partido rojo")
elif candidato == "B": 
    print("Usted ha votado por el partido verde")
elif candidato == "C":
    print("Usted ha votado por el partido azul")
else:
    print("Ha ingresado una opcion incorrecta")
    '''