print("Calculadora\nSoma: +\nSubtração: -\nMultiplicação: *\nDivisão: /")

num1 = int(input("1º valor: "))
num2 = int(input("2º valor: "))

operacao = input("Digite o caractere da operação matemática que deseja. ")

if operacao == "+":
    resultado = num1 + num2
elif operacao == "-":
    resultado = num1 - num2
elif operacao == "*":
    resultado = num1 * num2
elif operacao == "/":
    resultado = num1 / num2

print(f"Resultado: {resultado:.0f}")