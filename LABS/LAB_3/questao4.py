valor ={1 : 6, 2 : 6.5, 3 : 5, 4 : 3, 5 : 2}
codigo = int(input("Digite o código do produto:"))
quant = int(input("Digite a quantidade do produto:"))
total = valor[codigo] * quant
print(f"Total: R$ {total:.2f}")