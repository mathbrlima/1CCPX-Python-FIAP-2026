estado = int(input("Digite o código do estado (1 a 5): "))
peso_ton = float(input("Digite o peso da carga (em toneladas): "))
codigo_carga = int(input("Digite o código da carga (10 a 40): "))

peso_kg = peso_ton * 1000

if 10 <= codigo_carga <= 20:
    preco_kg = 100
elif 21 <= codigo_carga <= 30:
    preco_kg = 250
elif 31 <= codigo_carga <= 40:
    preco_kg = 340

preco_carga = peso_kg * preco_kg

if estado == 1:
    imposto = 0.35
elif estado == 2:
    imposto = 0.25
elif estado == 3:
    imposto = 0.15
elif estado == 4:
    imposto = 0.05
elif estado == 5:
    imposto = 0

valor_imposto = preco_carga * imposto
valor_total = preco_carga + valor_imposto

print(f"Peso da carga em kg: {peso_kg:.2f}")
print(f"Preço da carga: R$ {preco_carga:.2f}")
print(f"Valor do imposto: R$ {valor_imposto:.2f}")
print(f"Valor total (com imposto): R$ {valor_total:.2f}")