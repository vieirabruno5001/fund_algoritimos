def media(lista):
    if len(lista) == 0:
        raise ValueError("valor invalido")
    return sum(lista) / len(lista)
print(media([]))