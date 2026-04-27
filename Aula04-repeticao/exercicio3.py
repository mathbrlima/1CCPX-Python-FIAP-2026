tabuada = int(input("Digite um número para exibir na tabuada: "))
print(f"Tabuada do número {tabuada}")
for valor in range(0, 26, 1):
    print(f"{tabuada} x {valor} = {tabuada * valor}")