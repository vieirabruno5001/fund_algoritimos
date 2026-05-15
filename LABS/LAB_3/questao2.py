primeiro = int(input("Digite o valor do primeiro produto: "))
segundo = int(input("Digite o valor do segundo produto: "))
terceiro = int(input("Digite o valor do terceiro produto: "))
total = (primeiro + segundo + terceiro)
if total >= 500:
    print(f"Desconto: {total * 0.20:.2f}")
else:
    print(f"Desconto: {total * 0.10:.2f}")