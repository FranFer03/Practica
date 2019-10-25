def verConsonantes(cad):
    cad2 = cad.lower()
    vocales = "aeiou"
    consonantes = {letra for letra in cad2 if letra not in vocales}
    print("".join(consonantes))


mensaje = input("Mensaje : ")
verConsonantes(mensaje)