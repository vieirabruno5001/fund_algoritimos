hI = int(input("Digite a hora inicial: "))
mI = int(input("Digite o minuto inicial:"))
hF = int(input("Digite a hora final: "))
mF = int(input("Digite o minuto final: "))
inicio = hI * 60 + mI
final = hF * 60 + mF
duracao = final - inicio 
if duracao <= 0:
    duracao += 24 * 60

horas = duracao // 60
minutos = duracao % 60
print(f"O jogo durou {horas} hora(s) e {minutos} minutos(s)")