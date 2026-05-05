n = int(input("Digite um número de 1 a 10: "))
if n < 1 or n >= 10 :
    print("Número inválido!")
else:  
    for i in range(n):
        for j in range(n):
            if i == j or i + j == n - 1:
                print("#", end='')
            else:
                print(" ", end='')
        print()