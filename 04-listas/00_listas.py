## lista con strings
abecedario = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
print(abecedario)

## lista con elementos de tipos multiples
datos = ['a', 1, 'b', 2, 'c', 3, 'd', 4, 'e', 5]
print(datos)

################################################
#### funciones sobre listas
################################################
## LEN : cantidad de elementos de la lista
print('cantidad de letras en el abecedario: ', len(abecedario))
# - imprime la primera letra del abecedario:
print(abecedario[0])
# - imprime segundo dato de la lista
print(datos[1])

### modificar un elemento de una lista
abecedario[0] = 'A'
print(abecedario)
################################################
### Agregar elementos a una lista
## APPEND: agregar elementos a una lista
numeros = [1,2,3,4,5]
print('lista original: ', numeros)
numeros.append(6)
print('nuevo elemento agregado (6): ', numeros)

## INSERT agregar un elemento a la lista en una posición específica
numeros.insert(1, 1.5)
print('elemento agregado en la posicion 1 de la lista (1.5): ', numeros)

################################################
### BÚSQUEDAS
## COUNT: cantidad de ocurrencias de un mismo elemento
numeros = [1,2,3,4,5,1,1,1,1,1]
print('lista original: ', numeros)
print("count(1): ", numeros.count(1))
################################################
## INDEX buscar datos en una lista
print("index(1): ", numeros.index(1)) ##si hay mas de una ocurrencia devuelve el primer indice en donde encuentra ese valor

################################################
### ORDENAR ELEMENTOS
numeros.sort()
print('lista ordenada: ', numeros)

### INVERTIR ORDEN DE LOS ELEMENTOS EN LISTA
numeros.reverse()
print('lista invertida: ', numeros)

################################################
### ELIMINAR ELEMENTOS
## POP: eliminar ultimo elemento de una lista
numeros = [1,2,3,4,5]
print('lista original: \t', numeros)
numeros.pop()
print('lista luego de pop: ', numeros)

## REMOVE: eliminar un elemento particular
numeros.remove(3)
print('lista SIN 3: \t', numeros)
## CLEAR: limpiar una lista
numeros.clear()
print('lista original: \t', numeros)

### UNIR 2 listas
lista1 = [1,2,3,4,5]
lista2 = ['a','b','c','d','e']
lista3 = lista1 + lista2
print(lista1, ' + ', lista2, ' => ', lista3)
