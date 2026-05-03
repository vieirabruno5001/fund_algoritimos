n = int(input())
total = 0
coelhos = 0
ratos = 0
sapos = 0

for i in range(n):
    quantia = int(input())
    tipo = input().strip().upper()
    total += quantia

    if tipo == 'C':
        coelhos += quantia
    elif tipo == 'R':
        ratos += quantia
    elif tipo == 'S':
        sapos += quantia

pcoelhos = (coelhos/total)*100
pratos = (ratos/total)*100
psapos = (sapos/total)*100

print(f"Total: {total} cobaias")
print(f"Total de coelhos: {coelhos}")
print(f"Total de ratos: {ratos}")
print(f"Total de sapos: {sapos}")
print(f"Percentual de coelhos: {pcoelhos:.2f} %")
print(f"Percentual de ratos: {pratos:.2f} %")
print(f"Percentual de sapos: {psapos:.2f} %")