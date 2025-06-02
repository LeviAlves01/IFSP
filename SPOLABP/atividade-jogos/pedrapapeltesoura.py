import random


escolha_user = int(input("Digite sua escolha (1 - pedra | 2 - papel | 3 - tesoura): "))

while continuar == "S" or "s":
   opcoes = [1, 2, 3]

   escolha_comp = random.choice(opcoes)
   continuar = str("Deseja continuar? S - Sim | N - Não")

   if (escolha_user == escolha_comp):
       print("Você escolheu:", escolha_user)
       print("O adversário escolheu:", escolha_comp)
       print("\nEmpate!")
   elif(escolha_user == 1) and (escolha_comp == 2):
       print("Você escolheu:", escolha_user, "- Pedra")
       print("O computador escolheu:", escolha_comp, "- Tesoura")
       print("Parabéns! Você ganhou!")
   elif(escolha_user == 2) and (escolha_comp == 1):
       print("Você escolheu:", escolha_user, "- Tesoura\n")
       print("O computador escolheu:", escolha_comp, "- Pedra\n")
       print("Putz! O computador venceu!")
   elif(escolha_user == 2) and (escolha_comp == 3):
       print("Você escolheu:", escolha_user, "- Papel\n")
       print("O computador escolheu:", escolha_comp, "- Tesoura\n")
       print("Putz! O computador venceu!")
   else:
       print("Você escolheu", escolha_user, "- Tesoura\n")
       print("O computador escolheu:", escolha_comp, "- Papel\n")
       print("Parabéns! Você venceu!")
