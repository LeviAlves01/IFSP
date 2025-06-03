import random

palavras = ["Arroz", "João", "Brasília", "Borracha"]
caracteres = []

while True:
    palavra_forca = random.choice(palavras)

    for char in palavra_forca:
        caracteres.append(char)

    char_user = input("Digite uma letra: ")

    if char_user in caracteres:
        print()