# Mostrar todos os números primos de 2 até 2000

for n in range(2, 2001):
    primo = True  # assume que é primo

    for i in range(2, n):
        if n % i == 0:
            primo = False
            break  # já sabemos que não é primo

    if primo:
        print(n)