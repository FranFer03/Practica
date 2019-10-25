def morse():
    cadena = input("Mensaje : ").lower()
    for cad in cadena:
        if "a" == cad:
            print("*- ", end="")
        elif "b" == cad:
            print("-*** ", end="")
        elif "c" == cad:
            print("-*-* ", end="")
        elif "d" == cad:
            print("-** ", end="")
        elif "e" == cad:
            print("* ", end="")
        elif "f" == cad:
            print("**-* ", end="")
        elif "g" == cad:
            print("--* ", end="")
        elif "h" == cad:
            print("**** ", end="")
        elif "i" == cad:
            print("** ", end="")
        elif "j" == cad:
            print("*--- ", end="")
        elif "k" == cad:
            print("-*- ", end="")
        elif "l" == cad:
            print("*-** ", end="")
        elif "m" == cad:
            print("-- ", end="")
        elif "n" == cad:
            print("-* ", end="")
        elif "o" == cad:
            print("--- ", end="")
        elif "p" == cad:
            print("*--* ", end="")
        elif "q" == cad:
            print("--*- ", end="")
        elif "r" == cad:
            print("*-* ", end="")
        elif "s" == cad:
            print("*** ", end="")
        elif "t" == cad:
            print("- ", end="")
        elif "u" == cad:
            print("**- ", end="")
        elif "v" == cad:
            print("***- ", end="")
        elif "w" == cad:
            print("*-- ", end="")
        elif "x" == cad:
            print("-**- ", end="")
        elif "y" == cad:
            print("-*-- ", end="")
        elif "z" == cad:
            print("--** ", end="")
morse()