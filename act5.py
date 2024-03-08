def palind(palabra):
   
    palabra = palabra.lower()
    
   
    if palabra == palabra[::-1]:
        return True
    else:
        return False


if __name__ == "__main__":
    palabra_1 = "neuquen"
    palabra_2 = "jovenes"

    print(f"¿'{palabra_1}' es un palíndromo?: {palind(palabra_1)}")
    print(f"¿'{palabra_2}' es un palíndromo?: {palind(palabra_2)}")