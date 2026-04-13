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