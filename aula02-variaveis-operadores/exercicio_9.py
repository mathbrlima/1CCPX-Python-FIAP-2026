#Crie um programa que receba o valor do produto e valor pago.
#Calcule o troco a ser pago.
#O valor do troco deve ser exibido no terminal.

valor_pago = float(input("Digite o valor pago pelo cliente: "))
valor_produto = 12.50

if valor_pago >= valor_produto:
    troco = valor_pago - valor_produto
    print(f"Devolver R${troco}")

else:
    pendente = valor_produto - valor_pago
    print(f"Cobrar mais R${pendente}")