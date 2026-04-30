x = int(input())
form = {
    (3) : 'triângulo',
    (4) : 'quadrado',
    (5) : 'pentágono',
    (6) : 'hexágono',
    (7) : 'heptágono'
}

if x in form:
    print(f"{form[x]}")

if x > 10:
    print('Erro!')

