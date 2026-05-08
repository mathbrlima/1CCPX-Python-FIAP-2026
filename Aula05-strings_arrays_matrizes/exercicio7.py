import random

matriz = []

for i in range(3): # linha
    linha = []

    for j in range(4): # coluna
        valor = random.randint(1, 100)
        linha.append(valor)

    matriz.append(linha)

print("\nMatriz 3x4:")

for linha in matriz:
    print(linha)