#Ejercicio 1 de Entradas por teclado

a = float(input("Inresa un valor a 'a': "))
b = float(input("Inresa un valor a 'b': "))
c = float(input("Inresa un valor a 'c': "))

resolucion = b ** 2 - 4 * a * c

print(resolucion)

#Hasta ahi me quede

print("============================")

#Ejercicio 2

notatp1 = float(input("Ingrese la nota del TP1: "))
notatp2 = float(input("Ingrese la nota del TP2: "))
notatp3 = float(input("Ingrese la nota del TP3: "))
ep = float(input("Ingrese la nota del Examen Parcial: "))
ef = float(input("Ingrese la nota del Examen Final: "))

nota_promedio_tps = (notatp1 + notatp2 + notatp3) / 3
promedio = (nota_promedio_tps + ep + ef) / 3

print("Su promedio es:",promedio)
