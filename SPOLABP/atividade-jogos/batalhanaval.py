import random

tabuleiro = [["~" for _ in range(5)] for _ in range(5)]

def mostrar_tabuleiro():
    print("  0 1 2 3 4")
    for i, linha in enumerate(tabuleiro):
        print(f"{i} " + " ".join(linha))

linha_navio = random.randint(0, 4)
coluna_navio = random.randint(0, 4)

tentativas = 5

print("Batalha Naval - Ache o navio escondido!")
mostrar_tabuleiro()

for tentativa in range(1, tentativas + 1):
    print(f"\nTentativa {tentativa} de {tentativas}")

    try:
        linha = int(input("Escolha a linha (0 a 4): "))
        coluna = int(input("Escolha a coluna (0 a 4): "))
    except ValueError:
        print("Entrada inválida. Use apenas números.")
        continue

    if linha < 0 or linha > 4 or coluna < 0 or coluna > 4:
        print("Posição fora do tabuleiro!")
        continue

    if tabuleiro[linha][coluna] == "X":
        print("Você já tentou essa posição!")
        continue

    # Verifica se acertou o navio
    if linha == linha_navio and coluna == coluna_navio:
        print("Parabéns! Você acertou o navio!")
        tabuleiro[linha][coluna] = "N"
        mostrar_tabuleiro()
        break
    else:
        print("Errou... tente de novo!")
        tabuleiro[linha][coluna] = "X"
        mostrar_tabuleiro()
else:
    print("\nSuas tentativas acabaram.")
    print(f"O navio estava na posição: ({linha_navio}, {coluna_navio})")
