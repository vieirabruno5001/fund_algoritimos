cruz = int(input("Digite o tamanho da cruz: "))
if cruz < 1 or cruz > 10 :
    print("Número inválido!")
else:
    tamanho = 2 * cruz - 1

    for i in range(tamanho):
        for j in range(tamanho):
            if i == cruz - 1 or j == cruz - 1:
                print("+", end=' ')
            else:
                print(" ", end=' ')
        print()