n = int(input("Digite o tamanho da cruz: "))
if n < 1 or n > 10 :
    print("Número inválido!")
else:
    tamanho = 2 * 

    for i in range(tamanho):
        for j in range(tamanho):
            if i == n - 1 or j == n - 1:
                print("#", end=' ')
            else:
                print(" ", end=' ')
        print()