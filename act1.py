def encontrar_indice(lista, elemento):
    try:
        return lista.index(elemento)
    except ValueError:
        return -1

mi_lista = [8, 12, 9, 45]

while True:
    entrada_usuario = input("Ingresa un número para buscar (apreta 'e' si queres salir del programa): ")

    if entrada_usuario.lower() == 'e':
        break

    try:
        numero = int(entrada_usuario)
    except ValueError:
        print("Entrada inválida. Por favor, ingresa un número válido.")
        continue

    indice = encontrar_indice(mi_lista, numero)

    if indice == -1:
        print(f"El número {numero} no se encontró en la lista.")
    else:
        print(f"El número {numero} se encontró en el índice {indice}.")