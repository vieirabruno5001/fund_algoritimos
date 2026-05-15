n = int(input("Digite o valor de n (entre 1 e 10): "))
if n < 1 or n > 10:
    print("Por favor, insira um número entre 1 e 10.")
else:
    M = []
    for i in range(n):
        linha = []
        for j in range(n):
            linha.append(0)
        M.append(linha)
    print(f"Matriz {n}x{n}: {M}", end=" ")