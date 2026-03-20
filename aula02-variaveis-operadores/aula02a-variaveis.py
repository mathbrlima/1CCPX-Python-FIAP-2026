from pyasn1_modules.rfc8418 import dhSinglePass_stdDH_sha256kdf_scheme

print("ola mundo")

print(7 + 4)
print("7 + 4")
print("7" + "4") # CONCATENAÇÂO DE STRINGS

# Comentários de 1 linha
'''
    Comentários de 
    múltiplas linhas
'''

# VARIÁVEIS
nome = "Matheus" # str
idade = 26 # int
peso = 70.2 # float

print(nome, idade, peso)
print(f"Oiii, {nome}!!!!")

# INPUTS - SIMULAÇÂO DE FORMS NO CMD
nome = input("Disite o seu nome: ")
idade = int(input("Digite sua idade: "))

nova_idade = idade + 1

print(nome, idade)
print(nova_idade)

# atividade 1

nome = input("Informe se nome: ")
print(f"Seja bem vindo, {nome}.")