def procuraChave(dict,value):
    lista = []
    for chaves in dict.keys():
        if dict[chaves] == value:
            lista.append(chaves)
    return lista

def main():
    dict = {'alpha':1,'bravo':2,'charlie':1,
            'delta':3,'echo':1}
    value = int(input("digite o valor a ser buscado:"))
    print(f"procurando chaves com valor:{value}...")

    chaves_retornadas = procuraChave(dict,value)
    print(chaves_retornadas)
main()