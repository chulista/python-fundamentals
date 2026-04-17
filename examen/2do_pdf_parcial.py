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
                        estados.append("libre")
                        
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
                            • Libre
                            • Ocupada
                            """).strip().lower()
                    if estado == "libre" or estado == "0":
                        estados[i] = "libre"
                        print("Estado de habitaciones actualizado correctamente")
                        break
                    elif estado == "ocupada" or estado == "1":
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

            if not habitaciones:
                print("Todavia no hay habitaciones ingresadas")
                continue
            while True:
                ver_estados = input(f"""Ingrese el tipo de estado que desea ver:
                                • Libres
                                • Ocupadas
                                """).strip().lower()
                if ver_estados == "libres" or ver_estados == "0":
                    pass
                elif ver_estados == "ocupadas" or ver_estados == "1":
                    pass
                else:
                    print("Opcion incorrecta")

        case "6":
            
            numero_habitacion = input("Ingrese el numero de la nueva habitacion: ").strip()
    
            if numero_habitacion == "":
                print("Debe ingresar datos. Volviendo al menu...")
                continue
            if not numero_habitacion.isdigit():
                print("La habitacion a ingresar debe ser numerica. Volviendo al menu...")
                continue
            numero_habitacion = int(numero_habitacion)
            if numero_habitacion <= 100:
                print("La habitacion a ingresar debe ser mayor a '100'")
                continue
            if numero_habitacion in habitaciones:
                print("La habitacion ya esta ingresada. Volviendo al menu...")
                continue

            while True:
                nueva_estado = input(f"""Ingrese el esatdo de la habitacion {numero_habitacion}:
                                    • Libre
                                    • Ocupada 
                                    """).strip().lower()
                if nueva_estado == "libre":
                    habitaciones.append(numero_habitacion)
                    estados.append(nueva_estado)
                    print("Habitacion agregada correctamente")
                elif nueva_estado == "ocupada":
                    habitaciones.append(numero_habitacion)
                    estados.append(nueva_estado)
                    print("Habitacion agregada correctamente")
                else:
                    print("Opcion incorrecta...")
                break

        case "7":

            if not habitaciones:
                print("Todavia no hay habitaciones ingresadas")
                continue
            while True:
                cambiar = input("Ingrese la habitacion que desea cambiar el estado: ")
                
                if not cambiar.isdigit():
                    print("Debe ingresar numeros")
                    continue

                cambiar = int(cambiar)

                if cambiar not in habitaciones:
                    print("La habitacion no existe")
                    continue

                while True:
                    opcion_cambiar = input(f"""Ingrese el nuevo estado de {cambiar}:    
                                        • Libre
                                        • Ocupada 
                                        """).strip().lower()
                    if opcion_cambiar == "libre":
                        pass
                    elif opcion_cambiar == "ocupada":
                        pass
                    else:
                        print("Opcion incorrecta...")
                        continue
                    break
                
        case "8":
            print("Saliendo de la aplicacion...")
            break
        case _:
            print("Ingrese una opcion valida")
            continue
            