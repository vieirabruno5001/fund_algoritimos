def analise(lista):
    if len(lista) == 0:
    
        raise ValueError("valor invalido")
    
    media = sum(lista) / len(lista)

    l_ordenada = sorted(lista)
    n = len(l_ordenada)
    meio = n // 2

    if n % 2 == 1:
        mediana = l_ordenada[meio]
    else:
        mediana = int((l_ordenada[meio - 1] + l_ordenada[meio]) / 2)

    minimo = min(lista)
    maximo = max(lista)

    return media, mediana, minimo, maximo

print(analise([1,6,8,10]))