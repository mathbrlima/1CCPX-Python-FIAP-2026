idade = int(input("Informe sua idade: "))

if idade < 16:
    print("Voto NEGADO")
elif 16 <= idade < 18 or idade >= 70:
    print("Voto OPCIONAL")
else:
    print("Voto OBRIGATÓRIO")