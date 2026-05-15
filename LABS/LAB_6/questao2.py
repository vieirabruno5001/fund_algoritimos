n = int(input("Digite um número de 1 a 10: "))
if n < 1 or n >= 10:
    print("Número inválido!")
else:
    for i in range(1, n+1):
        for j in range(1, n+1):
            print(f"Par ({i}, {j}) - Soma: {i + j}")