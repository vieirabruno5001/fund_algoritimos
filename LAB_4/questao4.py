valor = input("Digite o valor da compra: ")
qparcela = input("Digite a quantidade de parcelas: ")
x = float
n = float
desconto = valor * x * n

if qparcela == 1:
    x = 0.10
if qparcela == 2 or 3:
    x = 0.05
if qparcela >= 4:
    x = 0
if valor > 5000:
    n = 0.05
else:
    n = 0

valorfinal = valor - desconto
valorparcela = valorfinal / qparcela

print(f"Desconto total: {desconto}")
print(f"Valor final da compra com desconto: {valorfinal}")
print(f"Cada parcela será de: {valorparcela}")