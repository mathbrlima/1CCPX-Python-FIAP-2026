matriz = []

for linha in range(4):
    linha_matriz = []
    for coluna in range(5):
        valor = linha * 5 + coluna + 1
        linha_matriz.append(valor)
    matriz.append(linha_matriz)

for linha in matriz:
    for valor in linha:
        print(f"{valor:2}", end=" ")
    print()