# Soma de uma progressão aritmética
# Validação da entrada
n = -1  # valor inicial inválido

while n <= 0:
    n = int(input("Digite um número inteiro positivo: "))
    if n <= 0:
        print("Valor inválido! Digite apenas números positivos.")

# Cálculo da soma
soma = 0
for i in range(1, n + 1):
    soma += i

# Saída
print(f"A soma de 1 até {n} é: {soma}")