# inferencia de tipos de datos
num1 = 40
num2 = 100.99
# suma de 2 tipos diferentes (int y float)
num3 = num1 + num2

print(num1, '\t-> ', type(num1))
print(num2, '\t-> ', type(num2))
print(num3, '\t-> ', type(num3))

# casteado de tipos
## (int -> float)
print(float(num1), '\t-> ', float(num2))
## (float -> int)
print(int(num1), '\t-> ', int(num2))
