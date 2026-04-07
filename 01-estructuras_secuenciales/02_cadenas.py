## strings
print("abcdefg")

## substrings
print("abcdefg"[0:5])
## de inicio hasta la posicion 2
print("abcdefg"[:3]) ## abc
## desde la posicion 3 hasta el final
print("abcdefg"[3:]) ## desde la posicion 3 en adelante

## uso de comillas simples y dobles
cadena = "hola 'carola'"
print(cadena)
cadena2 = 'hola "carola"'
print(cadena2)

## concatenacion
nombre = "ivan"
apellido = "moreno"
print(nombre + " " + apellido)

letra = 'a '
print(letra * 5)

## print de datos NO compatibles
# print( 1 + 'a') ## ERROR: unsupported operand type(s) for +: 'int' and 'str'
print( str(1) + ' a')

## formato de cadenas
# Minusculas
cadena3 = 'HoLa CoMO Va?'
print('original -> ', cadena3)
print('minuscula -> ', cadena3.lower())
# Mayusculas
print('mayuscula -> ', cadena3.upper())
## Capitalize
print('capitalize -> ', cadena3.capitalize())
## Title
print('title -> ', cadena3.title())
## Swapcase
print('title -> ', cadena3.swapcase())