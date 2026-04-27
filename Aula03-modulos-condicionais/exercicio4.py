nota1 = float(input("1º nota: "))
nota2 = float(input("2º nota: "))
nota3 = float(input("3º nota: "))
nota4 = float(input("4º nota: "))
media = (nota1 + nota2 + nota3 + nota4) / 4

if media >= 7:
    print("Aprovado")
elif 5 <= media < 7:
    print("Em recuperação")
elif media < 5:
    print("Reprovado")  



