valor = float(input("Digite o valor da compra: "))
qparcela = int(input("Digite a quantidade de parcelas: "))



if qparcela == 1:
    x = 0.10
elif qparcela == 2 or 3:
    x = 0.05
else:
    x = 0


desconto = valor * x

if valor > 5000 and qparcela <= 3:
    n = 0.05
else:
    n = 0

desconto_extra = valor * n
descontototal = desconto + desconto_extra

valorfinal = valor - descontototal
valorparcela = valorfinal / qparcela

print(f"Desconto total: {descontototal:.2f}")
print(f"Valor final da compra com desconto: {valorfinal:.2f}")
print(f"Cada parcela será de: {valorparcela:.2f}")