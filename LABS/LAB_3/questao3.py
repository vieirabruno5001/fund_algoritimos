import math
tipo = input("Você deseja calcular o volume do dodecaedro ou icosaedro: ")
a = float(input("Digite o valor da aresta a em metros: "))
if tipo == "dodecaedro":
    V = ((15 + 7 * math.sqrt(5)) / 4) * (a ** 3)
    print(f"O volume de um dodecaedro regular com {a:.2f} de aresta é: {V:.2f}")
elif tipo == "icosaedro":
    B = (5/12 * (3 + math.sqrt(5))) * (a ** 3)
    print(f"O volume de um icosaedro regular com {a:.2f} de aresta é: {B:.2f}")