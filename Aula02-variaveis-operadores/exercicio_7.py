#Leia 2 valores A e B, que correspondem a 2 notas de um aluno. A seguir calcule e informe a média ponderada do aluno, sabendo que a nota A tem peso 4 e a nota B tem peso 6.   Exemplo: nota a * 4 e nota b * 6.

print("Notas com pesos determinados")
A = float(input("1º nota do bimestre: "))
B = float(input("2º nota do bimestre: "))

peso_notaA = A * 4
peso_notaB = B * 6

media = (peso_notaA + peso_notaB) / 10

print(f"Média do aluno {media} ")