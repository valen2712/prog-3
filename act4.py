def orden_mayor_menor(mi_lista):
    lista_ord = sorted(mi_lista, reverse=True)
    return lista_ord

if __name__ == "__main__":

    numeros = [8, 4 ,3 ,9 ,0 ,5 ,6 ,2 ,1]

    numeros_ord = orden_mayor_menor(numeros)
    print("la lista ordenada de mayor a menor es:", numeros_ord)