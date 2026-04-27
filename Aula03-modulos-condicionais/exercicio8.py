salario = float(input("Qual a quantia de seu salário? "))

if salario <= 280:
    percentual = 0.20
elif salario <= 700:
    percentual = 0.15
elif salario <= 1500:
    percentual = 0.10
else:
    percentual = 0.05

aumento_valor = salario * percentual
salario_final = salario + aumento_valor

print(f"O salário antes do reajuste: R$ {salario:.2f}")
print(f"Percentual de aumento aplicado: {percentual * 100:.0f}%")
print(f"O valor do aumento: R$ {aumento_valor:.2f}")
print(f"O novo salário, após o aumento: R$ {salario_final:.2f}")