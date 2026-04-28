valores = list(map(float, input("Digite os valores(Ex: 1 2 3): ").split()))
valores.sort(reverse=True)
A, B, C = valores
print(f"A = {A}, B = {B}, C = {C}")

if A >= B + C:
    print("NAO FORMA TRIANGULO")
elif A**2 == B**2 + C**2:
    print("TRIANCULO RETANGULO")
elif A**2 > B**2 + C**2:
    print("TRIANGULO OBTUSANGULO")
elif A**2 < B**2 + C**2:
    print("TRIANGULO ACUTANGULO")



if A == B == C:
    print("TRIANGULO EQUILATERO")
elif A == B or A == C or B == C:
    print ("TRIANGULO ISOSCELES")
