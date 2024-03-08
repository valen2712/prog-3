def año_bisiesto(ano):
    if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
        return True
    else: 
        return False
if __name__ == "__main__":
    try:
        año=int(input("ingresa un año: "))

        if año_bisiesto:
            print(f"el año es bisiesto")
        else:
            print(f"el año no es bisiesto")
    except:
        ValueError