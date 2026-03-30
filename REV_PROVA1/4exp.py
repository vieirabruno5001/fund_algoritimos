valor_hora = float(input("digite o valor da hora de trabalho:"))
hora_trabalhada = float(input("digite o numero de horas trabalhadas no mes:"))
bruto = valor_hora * hora_trabalhada
ir = bruto * 0.11
inss = bruto * 0.08
sindicato = bruto * 0.05
salario = bruto - (ir + inss + sindicato)
print (f"+ Salario bruto: {bruto}")
print (f"- IR (11%): {ir}")
print (f"- INSS (8%): {inss}")
print (f"- Sindicato: {sindicato}")
print (f"+ salario liquido: {salario}")