data_nascimento = int(input("Digite o ano de nascimento: "))
idade = 2026 - data_nascimento

if idade >= 18:
    print("Voto obrigatório")
elif 16 <= idade < 18:
    print("Voto opcional")
else:
    print("Voto proibido")