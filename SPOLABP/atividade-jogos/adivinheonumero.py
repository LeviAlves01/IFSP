import random

numero = random.randint(1, 100)
tentativas = 9

while tentativas>0:
    print("Adivinhe o número!\n")
    print("Você tem", tentativas, "chances de acertar o número escolhido de 1 a 100!")

    chute = int(input("Digite seu chute:"))
    diferenca = abs(numero - chute)

    if(chute==numero):
        print("Parabéns! Você acertou!")
        break
    elif(diferenca<=10):
        print("Wow! Seu chute foi muito próximo, continue assim!\n \n \n")
    elif(10<diferenca<50):
        print("É... foi mais ou menos. Tenta de novo!\n \n \n")
    elif(diferenca>=50):
        print("Eita, foi longe, pensa melhor\n \n \n")
        continue

    tentativas -= 1

else:
    print("Suas chances acabaram :(\n O número era:", numero)
    print("\n Quem sabe na próxima!")