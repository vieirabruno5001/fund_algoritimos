qtd = int(input("Entre com a quantidade de números que serão digitados: "))
maior = None

for i in range(1, qtd + 1):
    num = int(input(f"número {i}: "))   
  
    if maior is None or num > maior:
        maior = num
        
print(f"Maior número digitado: {maior}")
    