def ler_lista():
    S = int(input("Digite a quantidade de números: "))
    lista = []
    for i in range(S):
        valor = int(input(f"digite o {i+1}º número: "))
        lista.append(valor)
    print(f"Lista: {lista}\nminimo: {min(lista)}\nmaximo: {max(lista)}")
ler_lista()