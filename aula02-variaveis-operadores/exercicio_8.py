#Neste problema, deve-se ler o nome de uma peça que chamaremos de peça1, o número de peças1 que o usuário quer, o valor unitário de cada peça1, o nome de uma peça2, o número de peças2 e o valor unitário de cada peça2. Após, calcule e mostre o valor a ser pago.

print("Calculador de pedidos")

nome1 = print("Peça1")
numero_pecas1 = int(input("Informe quantas peças1 você deseja: "))
valor_cada_peca1 = 325.5
valor_total_peca1 = numero_pecas1 * valor_cada_peca1
print(f"peça1\nNúmero de peças solicitadas: {numero_pecas1} peças1\nPreço por cada peça1: R${valor_cada_peca1}\n Valor total das peças2: R${valor_total_peca1}")


nome2 = print("Peça2")
numero_pecas2 = int(input("Informe quantas peças2 você deseja: "))
valor_cada_peca2 = 685.5
valor_total_peca2 = numero_pecas2 * valor_cada_peca2
print(f"peça2\nNúmero de peças solicitadas: {numero_pecas2} peças2\nPreço por cada peça2: R${valor_cada_peca2}\n Valor total das peças2: R${valor_total_peca2}")

valor_compra_conjunta = valor_total_peca1 + valor_total_peca2

print(f"Total a pagar pelas peças: R${valor_compra_conjunta}")
