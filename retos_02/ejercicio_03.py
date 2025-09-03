frase = input("Ingrese una frase: ")

lista_palabras = frase.split()
frase = frase.lower()
contar = (
    frase.count("a")
    + frase.count("e")
    + frase.count("i")
    + frase.count("o")
    + frase.count("u")
)

frase_reves = frase[::-1]

print("Cantidad de palabras: ", len(lista_palabras))
print("Cantidad de vocales: ", contar)
print("Es palindromo: ", frase.replace(" ", "") == frase_reves.replace(" ", ""))
