ordenes = []
horas = []

while True:
    print("""\n===MENU DEL TALLER===

1: Ingrese ordenes.
2: Ingresar horas estimadas por orden.
3: Mostrar agenda del taller.
4: Consultar horas por orden.
5: Listar ordenes con 0 horas
6: Agregar orden.
7: Actualizar horas.
8: Salir.""")
    
    opcion = input("\nIngrese la opcion que desee: ")

    match opcion:
        
        case "1":

            while True: 
                cantidad = input("Ingrese la cantidad ordenes que desea ingresar: ")
                if not cantidad.isdigit():
                    print("Debe ingresar numeros mayores a '0'")
                    continue
                elif cantidad == "0":
                    print("Debe ingresar numeros mayores a '0'")
                    continue
                cantidad = int(cantidad)
                break
                
            for i in range(cantidad):
                while True:
                    numero_orden = input(f"Ingrese el numero de orden {i+1}: ")
                    if not numero_orden.isdigit():
                        print("Debe ingresar numeros mayores a '0'")
                        continue
                    elif numero_orden == "0":
                        print("Debe ingresar numeros mayores a '0'")
                        continue
                    elif f"ORD-{numero_orden}" in ordenes:
                        print("Esa orden ya esta ingresada")
                    else:
                        ordenes.append(f"ORD-{numero_orden}")
                        horas.append(0)
                        print("Ordenes creadas correctamente")
                        break
                              
        case "2":

            if not ordenes:
                print("No hay ordenes ingresadas")
                continue
            for i in range(len(ordenes)):
                while True:
                    ingreso_horas = input(f"Ingrese la cantidad de horas para {ordenes[i]}: ")
                    if not ingreso_horas.isdigit():
                        print("Debe ingresar numeros enteros mayores a '0'")
                        continue
                    elif ingreso_horas == "0":
                        print("Debe ingresar numeros enteros mayores a '0'")
                        continue
                    ingreso_horas = float(ingreso_horas)
                    
                    horas[i] = ingreso_horas
                    print("Horas agregadas correctamente")
                    break

        case "3":

            if not ordenes:
                print("No hay ordenes ingresadas")
                continue
            print("===AGENDA DEL TALLER===")
            for i in range(len(ordenes)):
                print(f"La {ordenes[i]} tiene {horas[i]} horas")
  
        case "4":

            if not ordenes:
                print("No hay ordenes ingresadas")
                continue
            consulta = input("Ingrese la orden que desee consultar, ej; ORD-numero: ").strip()
            if consulta not in ordenes:
                print("La orden no existe")
            else:
                i = ordenes.index(consulta)
                print(f"Orden {ordenes[i]} | Tiempo estimado {horas[i]}")

        case "5":

            if not ordenes:
                print("No hay ordenes ingresadas")
                continue
            print("\n===ORDENES PENDIENTE DE DIAGNOSTICO===")
            encontradas = False
            for i in range(len(horas)):
                if horas[i] == 0:
                    print(f"{ordenes[i]} | Pendiente de diagnostico")
                    encontradas = True
            
            if not encontradas:
                print("No hay pendientes de diagnostico")    
            
        case "6":

            while True:
                una_orden = input("Ingrese una nueva orden: ")
                if not una_orden.isdigit():
                    print("Debe ingresar numeros mayores a '0'")
                elif una_orden == "0":
                    print("Debe ingresar numeros mayores a '0'")
                elif f"ORD-{una_orden}" in ordenes:
                    print("Esa orden ya existe")
                else:
                    ordenes.append(f"ORD-{una_orden}")
                    horas.append(0)
                    break
            
            while True:
                horas_uno = input(f"\nIngrese la cantidad de horas que desee para ORD-{una_orden}: ")
                if not horas_uno.isdigit():
                    print("Debe ingresar numeros enteros...")
                    continue
                horas[-1] = int(horas_uno)
                print(f"\nORD-{una_orden} ingresada correctamente con {horas_uno} horas")
                break

        case "7":
            pass
        case "8":
            print("Saliendo de la aplicacion...")
            break
        case _:
            print("Opcion incorrecta...")


    
