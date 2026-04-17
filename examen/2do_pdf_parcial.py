#Caso del hotel, habitaciones y estado (0 = libre / 1 = ocupada)

habitaciones = []
estados = []

while True:
    print("""    =========MENU DEL HOTEL=========
    1. Ingresar números de habitación
    2. Ingresar estados (0/1) paralelos
    3. Mostrar estado general  
    4. Consultar estado de una habitación
    5. Listar ocupadas o libres (según lo que se pida)
    6. Agregar habitación
    7. Cambiar estado
    8. Salir  
    """)

    opcion = input("Ingrese la opcion que desee: ")

    match opcion:
        case "1":

            while True:
                cantidad = input("Ingrese la cantidad de habitaciones que desee añadir: ").strip()
                if not cantidad.isdigit():
                    print("Solo se pueden ingresar numeros")
                    continue
                elif cantidad == "0":
                    print("No puede ingresar '0' habitaciones")
                    continue
                cantidad = int(cantidad)
            
                for i in range(cantidad):
                    while True:
                        habitacion = input(f"Ingrese la habitacion numero {i+1}: ")
                        if not habitacion.isdigit():
                            print("Solo puede ingresar numeros mayores 100")
                            continue
                        elif int(habitacion) <= 100:
                            print("Solo puede ingresar numeros mayores 100")
                            continue
                        
                        habitacion = int(habitacion)

                        if habitacion in habitaciones:
                            print("Esa habitacion ya esta ingresada")
                            continue

                        habitaciones.append(habitacion)
                        estados.append("ocupada")
                        
                        break
                print("Habitaciones agregadas correctamente")
                break
                    
        case "2":

            if not habitaciones:
                print("Todavia no hay habitaciones ingresadas")
                continue
            for i in range(len(habitaciones)):
                while True:
                    estado = input(f"""Ingrese el estado de la habitacion {habitaciones[i]}: 
                            0. Libre
                            1. Ocupada
                            """).strip().lower()
                    if estado == "libre":
                        estados[i] = "libre"
                        print("Estado de habitaciones actualizado correctamente")
                        break
                    elif estado == "ocupada":
                        estados[i] = "ocupada"
                        print("Estado de habitaciones actualizado correctamente")
                        break
                    else:
                        print("Opcion incorrecta...")
                
        case "3":

            if not habitaciones:
                print("Todavia no hay habitaciones ingresadas")
                continue
            else:
                for i in range(len(habitaciones)):
                    print(f"Habitacion {habitaciones[i]}: {estados[i]}")
                          
        case "4":
            
            if not habitaciones:
                    print("Todavia no hay habitaciones ingresadas")
                    continue

            while True:
                    consulta = input("Ingrese la habitacion que desee: ").strip()
                    if not consulta.isdigit():
                        print("Solo puede ingresar numeros")
                        continue
        
                    consulta = int(consulta)
        
                    if consulta in habitaciones:
                        i = habitaciones.index(consulta)
                        print(f"Habitacion {habitaciones[i]}: {estados[i]}")
                    else:
                        print("La habitacion no existe")
                    break

        case "5":
            pass
        case "6":
            pass
        case "7":
            pass
        case "8":
            break
        case _:
            print("Ingrese una opcion valida")
            continue
            