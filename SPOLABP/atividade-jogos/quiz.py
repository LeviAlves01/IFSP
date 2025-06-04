perguntas = {
    "Qual o maior planeta do Sistema Solar?\n A - Vênus\n B - Júpiter\n C - Saturno": "B", 
    "A capital do Belém é Pará?\n Verdadeiro\n Falso": "V", 
    "Quem criou a Apple?\n A - Mark Zuckerberg\n B - Elon Musk\n C - Steve Jobs": "C"
}

valores = list(perguntas.keys())
respostas = list(perguntas.values())

i = 0
pontos = 0

while i < len(valores):
    print(valores[i])
    chute = input("Digite a resposta: ").upper()

    if (chute == respostas[i]):
        print("Parabéns! Você acertou!\n Vamos para a próxima")
        pontos += 1
        print("Pontos:", pontos, "\n \n")
    elif not chute.isalpha():
        print("Por favor, digite a resposta\n \n")
    else:
        print("Putz... Você errou, vamos para a próxima\n \n")

    i += 1

print("Fim de jogo!\n Sua pontuação foi:", pontos)