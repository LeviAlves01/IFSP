import random

palavras = ["Esmalte", "Caneta", "Caixa", "Borracha"]
palavra_forca = random.choice(palavras)
caracteres = list(palavra_forca)
chutes = []
tentativa = 0

while True:
    print("Jogo da forca!\n")
    print("O tema é: objetos!\n")

    exibicao = ""
    for char in caracteres:
        if char.lower() in chutes:
            exibicao += char + " "
        else:
            exibicao += "_ "
        
    print("Palavra: ", exibicao.strip())
    
    char_user = input("Digite uma letra: ").lower()
    
    if not char_user.isalpha() or len(char_user) != 1:
        print("Por favor, digite uma letra\n \n")
        continue
    
    if char_user in chutes:
        print("Você já digitou essa letra\n \n")
        continue

    chutes.append(char_user)
    tentativa += 1
        
    if all(char.lower() in chutes for char in caracteres):
        print("\nParabéns! Você acertou! A palavra é:", palavra_forca)
        break