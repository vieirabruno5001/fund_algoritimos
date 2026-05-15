pp = input("Primeira palavra: ")
sp = input("Segunda palavra: ")
tp = input("Terceira palavra: ")
if sp == 'inseto':
    if tp == 'hematofago':
        print("pulga")
    elif tp == 'herbivoro':
        print('lagarta')

if sp == 'anelideo':
    if tp == 'hematofago':
        print('sanguessuga')
    elif tp == 'onivoro':
        print('minhoca')

if sp == 'mamifero':
    if tp == 'herbivoro':
        print('vaca')
    elif tp == 'onivoro':
        print('homem')

if sp == 'ave':
    if tp == 'carnivoro':
        print('aguia')
    elif tp == 'onivoro':
        print('pomba')