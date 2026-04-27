maior = None

for i in range(1, 6):
    valor = float(input(f"{i}º valor: "))

    if maior is None or valor > maior:
        maior = valor

print(f"O maior valor digitado foi: {maior}")