soma = 0

for i in range(1, 6):
    valor = float(input(f"{i}º valor: "))
    soma = soma + valor

print(f"Soma total = {soma:.0f}")