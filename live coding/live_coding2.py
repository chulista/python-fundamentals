while True:
    ingreso = input("Ingrese su nombre:")
    print(ingreso)
    
    seguir = input("Desea continuar? (S/N)").strip().lower()
    if seguir != "s":
        break

