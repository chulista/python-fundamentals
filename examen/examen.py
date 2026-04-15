#############################################
## SISTEMA DE CONTROL DE INVENTARIO
#############################################

### uso de listas
# herramientas[]
# existencias[]

'''
SISTEMA DE CONTROL DE INVENTARIO
1. Carga Inicial de Herramientas
2. Carga de Existencias
3. Visualizacion de Inventario
4. COnsulta de tock
5. Reporte de Agotadas
6. Alta de nuevo producto
7. Actualizacion de Stock (Venta/Ingreso)
8. Salir
'''
herramientas = []
existencias = []

while True:
    print("""
          1. Carga Inicial de Herramientas
          2. Carga de Existencias
          3. Visualización de Inventario
          4. Consulta de Stock
          5. Reporte de Agotados
          6. Alta de Nuevo Producto
          7. Actualización de Stock (Venta/Ingreso)
          8. Salir
          """)
    opcion = input("Ingrese la opcion que desee: ")

    match opcion:
        case "1":
            cantidad = 0
            cantidad_herramientas_ingresadas = 0

            while True: 
                cantidad_herramientas = input("Ingrese la cantidad de herramienta/as que desea ingresar: ")
                
                if not cantidad_herramientas.isdigit():
                    print("Solo se pueden ingresar datos numericos o mayores cero")
                    continue

                cantidad = int(cantidad_herramientas)
                
                if cantidad == 0:
                    print("No se puede ingresar 'cero' herramientas")
                    continue
                break

#Se debe seguir pidiendo herramientas hasta completar la cantidad especificada por el usuario.
            while cantidad_herramientas_ingresadas < cantidad:
                herramienta_ingresada = input(f"Ingrese la herramienta numero {cantidad_herramientas_ingresadas + 1}: ").strip().lower()
                
                if not herramienta_ingresada.isalpha():
                    print("El nombre de la herramienta solo puede contener letras")
                    continue
                elif herramienta_ingresada in herramientas:
                    print("La herramienta ya esta en el inventario")
                else:
                    herramientas.append(herramienta_ingresada)
                    existencias.append(0)
                    cantidad_herramientas_ingresadas += 1  
                    print("Herramienta/as ingresada al inventario correctamente")

        case "2": #El case 2 se encarga de agregar existencias a herramientas ya existentes
            if not herramientas:
                print("No hay herrmientas en el inventario")
                continue
            else:
                for i in range(len(herramientas)):
                    while True:
                        existencia = input(f"Ingrese existencias de '{herramientas[i]}': ")
                        if not existencia.isdigit():
                            print("Solo se pueden ingresar datos numericos")
                            continue
                        if int(existencia) == 0:
                            print("No puede ingresar 0 existencias")
                            continue
                        existencias[i] = int(existencia)
                        break
                print("Se ingresaron las existencias correctamente")  

        case "3": #Muestra el inventario al usuario
            if not herramientas:
                print("No hay herramientas en el inventario")
                continue
            else:
                print("\n--- INVENTARIO ---")
                for i in range(len(herramientas)):
                    print(f"Herramienta: {herramientas[i]} | Existencias: {existencias[i]}")

        case "4": #Consulta de stock
            if not herramientas:
                print("No hay herramientas en el inventario")
                continue
            herramienta_buscar = input("Ingrese la herramienta que desee: ").strip().lower()
            if herramienta_buscar in herramientas:
                i = herramientas.index(herramienta_buscar)
                print(f"Herramienta: {herramientas[i]} | Existencias: {existencias[i]}")
            else:
                print("La herramienta no se encuentra en el inventario")
            
        case "5": #Lista las herramientas con 0 existencias
            if not herramientas:
                print("No hay herramientas en el inventario")
                continue
            print("LISTA DE AGOTADOS")
            for i in range(len(existencias)):
                if existencias[i] == 0:
                    print(f"Herramienta: {herramientas[i]} | Existencias: {existencias[i]}")

        case "6": #Permite agregar UN producto con su stock inicial
            nombre_herramienta = input("Ingrese el nombre de la nueva herramienta: ").strip().lower()
    
            if nombre_herramienta == "":
                print("El nombre no puede estar vacio. Volviendo al menu...")
                continue
            if not nombre_herramienta.isalpha():
                print("El nombre de la herramienta solo puede contener letras. Volviendo al menu...")
                continue
            if nombre_herramienta in herramientas:
                print("La herramienta ya existe en el inventario. Volviendo al menu...")
                continue
    
            while True:
                stock = input(f"Ingrese el stock inicial para '{nombre_herramienta}': ")
                if not stock.isdigit():
                    print("Solo se pueden ingresar datos numericos")
                    continue
                if int(stock) < 0:
                    print("El stock no puede ser negativo")
                    continue
                break
    
            herramientas.append(nombre_herramienta)
            existencias.append(int(stock))
            print("Herramienta agregada correctamente")
           
        case "7": #Actualización de Stock (Venta/Ingreso):
            if not herramientas:
                print("No hay herramientas en el inventario")
                continue
            
            while True:

                opcion_stock = input("""Ingrese la opcion que desee
                            1. Venta
                            2. Ingreso
                                    """).strip().lower()
                
                if opcion_stock == "venta":
                    venta_herramienta = input("Ingrese la herramienta que desee vender: ").strip().lower()
                    
                    if venta_herramienta.isdigit():
                        print("Solo puede ingresar dato de tipo letra")
                        
                    elif venta_herramienta == "":
                        print("No se puede ingresar espacios")

                    elif not venta_herramienta in herramientas:
                        print("La herramienta no se encuentra en el inventario")
                        
                    else:
                        cantidad_vender = input("Ingrese la cantidad de herramientas que desea vender: ")
                        if not cantidad_vender.isdigit():
                            print("Solo se pueden ingresar datos numericos")
                        elif cantidad_vender == "":
                            print("No se puede ingresar espacios")
                        else:
                            i = herramientas.index(venta_herramienta)
                            cantidad = int(cantidad_vender)
                            
                            if existencias[i] >= cantidad:
                                existencias[i] -= cantidad
                                print("Herramientas vendidas correctamente")
                                break
                            else:
                                print("Cantidad insuficiente para vender")


                            
                elif opcion_stock == "ingreso":
                    pass
                else:
                    print("Opcion incorrecta")
                    continue
                
        case "8": #Corta el programa
            print("Se ha cerrado la aplicacion")
            break
        case _:
            print("La opcion ingresada es incorrecta")

####
## FUNCIONALIDADES
    # ----------
    # 1. Carga INICIAL de Herramientas
    ## input: Cantidad de Herramientas
    # persistir la cantidad de herramientas en una variable de tipo int
    # persistir las herramientas en una lista []

    # validaciones:
    # si el usuario ingresar 2 veces 'martillo' se debe checkear que NO esté en la lista que se esta cargando, para evitar DUPLICADOS.
    # se debe seguir pidiendo herramientas hasta completar la cantidad especificada por el usuario.

    # Ejemplo de input: ['martillo', 'taladro', 'destornillador', 'tornillos', 'mechas']

# ----------
# 2. Carga de Existencias
    # Ejemplo de input: [1, 2, 3]
    # Caso 1: NO hay herramientas cargadas -> input: [1, 2, 3]
'''
    Para cargar existencias primero ingrese herramientas
'''
        # Entonces: Informamos el error al usuario
    # Caso 2: Ingresa datos NO numericos -> input: ['uno', 'dos', 'tres']
'''
    Solo se permiten numeros igual o mayores a 1
'''
    # Caso 3: Si hay herramientas cargadas. input: [1, 2, 3, 4, 5]
'''
    martillo: $INPUT -> INPUT numerico 
    taladro: $INPUT
    destornillador: $INPUT
    tornillos: $INPUT
    mechas: $INPUT
'''
        # caso 3 - validaciones: $INPUT >= 1

# ----------
# 3. Visualizacion de Inventario
'''OUTPUT:
    Inventario: 
        martillo: 1 
        taladro: 2
        destornillador: 3
        tornillos: 4
        mechas: 5
'''

# 4: Consultar Stock
    ## INPUT: 'destornillador'
    ## Buscar elemento en la lista de Herramientas
    ## CASO 1: no existe herramienta
''' OUTPUT:
    La herramienta NO se encuentra en el inventario
'''
    ## CASO 2: la herramienta SI existe
    ### index = -1
    ### herramientas: ['martillo', 'taladro', 'destornillador', 'tornillos', 'mechas']
    ### variable index: indica la posicion en donde se encuentre esa herramienta.
    ### existencias: [1, 2, 3, 4, 5]
    ### print existencias[index]
'''OUTPUT:
Ingrese herramienta: $HERRAMIENTA

Unidades Disponibles: $UNIDADES
'''

# 5: Reporte de Agotados
    ### Iterar por toda la lista de Existencias y quedarse con los indices que tengan valor cero [1, 0, 0, 4, 0] -> 1,2,4
    ### Caso 1: Hay herramientas sin STOCK
        ### quedarte con la herramienta en el el indice o indices encontrados iterando sobre la lista de Herramientas[]

#herramientasAgotadas = [] ## camello -> camelCase
#herramientas_agotadas = [] ## vibora -> snack_case

'''OUTPUT:
Herramientas Agotadas: 
- taladro
- destornillador
- mechas
'''
    ### Caso 2: NO hay herramientas Agotadas
'''
   No hay herramientas Agotadas. 
'''

# 6: Alta de Nuevo Producto
''' INPUT:
- Ingrese una herramienta al inventario: $HERRAMIENTA
- Ingrese la cantidad: $UNIDAD
'''
    ### Caso 1: Nombre vacio
    ### Caso 2: Nombre duplicado
    ### Caso 3: Valor de existencia negativo
'''OUTPUT:
    Error: Ha ingresado un dato incorrecto. 
    Volviendo al menu principal...
    
    SISTEMA DE CONTROL DE INVENTARIO
    1. Carga Inicial de Herramientas
    2. Carga de Existencias
    3. Visualizacion de Inventario
    4. COnsulta de tock
    5. Reporte de Agotadas
    6. Alta de nuevo producto
    7. Actualizacion de Stock (Venta/Ingreso)
    8. Salir
'''

# 7. Actualizacion de Stock (Venta/Ingreso)
### Caso Venta
''' INPUT:
- Herramienta: $HERRAMIENTA
- Cantidad: $UNIDAD
'''
    ### Caso 1: NO hay unidades suficientes
'''OUTPUT:
    No hay stock de $HERRAMIENTA
'''
    ### Caso 2: Hay unidades suficientes
'''OUTPUT:
    $HERRAMIENTA vendida
'''
    ### Caso 3: No existe $HERRAMIENTA en el listado
'''OUTPUT:
    $HERRAMIENTA inexistente
'''
    ### Caso 4: Usuario ingresa Unidades negativas o nulas(0) o caracteres (datos no numericos)
'''OUTPUT:
    No se pueden ingresar datos negativos o cero o datos que no sean numericos.
'''
### Caso Ingreso
''' INPUT:
Ingrese la herramienta con Stock a añadir
- Herramienta: $HERRAMIENTA
- Cantidad: $UNIDAD
'''
### Caso 1: No existe $HERRAMIENTA en el listado
'''OUTPUT:
    $HERRAMIENTA inexistente
'''
### Caso 2: Usuario ingresa Unidades negativas, nulas(0) o caracteres (datos no numericos)
'''OUTPUT:
    No se pueden ingresar datos negativos o cero o datos que no sean numericos.
'''

#8. Salir
'''OUTPUT:
    Cerrando la aplicación.
'''