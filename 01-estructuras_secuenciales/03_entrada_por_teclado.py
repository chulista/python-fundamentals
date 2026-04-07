while True:

    nombre = input("Ingrese su nombre: ").strip().capitalize()
    if nombre.isalpha():
        break
    else:
        print("NOMBRE IVALIDO")

while True:
    
    edad = input("Ingrese su edad como numero entero: ").strip()
    if edad.isdigit() and len(edad) <= 2:
        break
    else:
        print("EDAD INVALIDA O MAYOR A 2 DIGITOS")

print(f"Nombre: {nombre}")
print(f"Edad: {edad}")