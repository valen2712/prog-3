def imprimir_rectangulo(ancho, alto, caracter):
    for i in range(ancho):
        print(caracter * alto)

def main():
    ancho = int(input("Ancho: "))
    alto = int(input("Alto: "))
    caracter = input("Caracter: ")

    imprimir_rectangulo(ancho, alto, caracter)

if __name__ == "__main__":
    main()