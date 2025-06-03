import random

continuar = "S" 
while continuar == "S" or continuar == "s":
    escolha_user = int(input("Digite sua escolha (1 - pedra | 2 - papel | 3 - tesoura): "))
    
    opcoes = [1, 2, 3]
    escolha_comp = random.choice(opcoes)

    if escolha_user == escolha_comp:
        print("Você escolheu:", escolha_user)
        print("O adversário escolheu:", escolha_comp)
        print("\nEmpate!")
    elif (escolha_user == 1 and escolha_comp == 2) or (escolha_user == 2 and escolha_comp == 1):
        print("Você escolheu:", escolha_user, "- Pedra")
        print("O computador escolheu:", escolha_comp, "- Papel")
        print("Putz! O computador venceu!")
    elif (escolha_user == 2 and escolha_comp == 3) or (escolha_user == 3 and escolha_comp == 2):
        print("Você escolheu:", escolha_user, "- Papel")
        print("O computador escolheu:", escolha_comp, "- Tesoura")
        print("Putz! O computador venceu!")
    else:
        print("Você escolheu:", escolha_user, "- Tesoura")
        print("O computador escolheu:", escolha_comp, "- Pedra")
        print("Parabéns! Você venceu!")

    continuar = input("Deseja continuar? S - Sim | N - Não: ")