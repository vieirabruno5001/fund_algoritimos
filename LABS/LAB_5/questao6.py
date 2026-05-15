ano = int(input("Digite o ano desejado: "))
salario = 5000
percentual = 1.5/100

salario += salario * percentual

for i in range(2007, ano + 1):
    percentual *= 2
    salario += salario * percentual

print(f"Salário de {ano}: R$ {salario:.2f}")