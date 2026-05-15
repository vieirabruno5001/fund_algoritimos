def maximo(x, y, imprime=False):
    maior = x if x > y else y
    if imprime:
        print(maior)
    return maior
print(maximo(5, 2))