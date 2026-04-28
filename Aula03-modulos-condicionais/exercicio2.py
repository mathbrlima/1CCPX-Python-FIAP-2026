numero = int(input("Digite um número: "))

if numero % 2 == 0:
# numero % 2 calcula o resto da divisão por 2
# 0 "%" pega dois números e devolve o que sobra depois da divisão inteira.

    print("O número é par.")
else:
    print("O número é ímpar.")

# Se o resto da divisão por 2 for 0, significa que o número divide certinho por 2 → par
# Se o resto for 1, sobra alguma coisa → ímpar