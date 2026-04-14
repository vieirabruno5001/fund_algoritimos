dias = int(input("digite a quantidade de dias:"))
horas = int(input("digite a quantidade de horas:"))
minutos = int(input("digite a quantidade de minutos:"))
segundos = float(input("digite a quantidade de segundos:"))
total = (dias * 86400) + (horas * 3600) + (minutos * 60) + segundos
print (f"tempo total foi de {total:.1f} segundos")