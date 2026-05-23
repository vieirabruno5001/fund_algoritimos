contador = 0
C = []
for i in range(3):
    L = []
    for j in range(3):
        numero = int(input())
        L.append(numero)
        if numero < 0:
            contador += 1
    C.append(L)
print(f"{contador} números negativos")
for i in range(3):
    for j in range(3):
        print(f"{C[i][j]}", end=" ")
    print()
for i in range(3):
    for j in range(3):
        if i == 0 or i == 2 or j == 0 or j == 2:
            print(C[i][j], end=" ")
        else:
            print(" ", end=" ")
    print()