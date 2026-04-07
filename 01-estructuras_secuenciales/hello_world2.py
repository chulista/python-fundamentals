import sys

def main():
    # Validar cantidad de argumentos
    if len(sys.argv) != 4:
        print("Uso: python main.py <nombre> <edad> <profesion>")
        return

    nombre = sys.argv[1]
    edad = sys.argv[2]
    profesion = sys.argv[3]

    print(f"Hola, mi nombre es {nombre}, tengo {edad} años y soy {profesion}.")


if __name__ == "__main__":
    main()