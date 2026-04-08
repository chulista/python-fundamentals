#Ejercicio 1 de Mostrar datos por pantalla

vocal = input("Ingrese una vocal en minuscula: ")
letra_m = input("Ingrese una letra en mayuscuala: ")

paso_ma = vocal.upper()
paso_mi = letra_m.lower()

mostrar = paso_ma + " " + paso_mi

print(mostrar)

print("=============================")

#Ejercicio 2 

nombre = input("Ingrese su nombre: ").strip().capitalize()
edad = int(input("Ingrese su edad: "))
genero = input("Ingrese su sexo: ").strip().capitalize()
print()

print("Te llamas:",nombre,"\n")
print("Tu edad es:", edad,"\n")
print("Eres:", genero)

print()