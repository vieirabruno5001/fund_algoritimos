modelos = []
consumos = []

for i in range(5):
    modelos.append(input())

for i in range(5):
    consumos.append(int(input()))

maior_consumo = max(consumos)
indice = consumos.index(maior_consumo)

print(modelos[indice])

for consumo in consumos:
    litros = 1000 / consumo
    print(round(litros))