def eh_primo(x):
    if x <= 1:
        return False
    for i in range(2, int(x**0.5) + 1):
        if x % i == 0:
            return False
    return True

# quantidade de números que serão digitados
n = int(input("Quantos números você deseja informar? "))

contador_primos = 0

for i in range(n):
    numero = int(input("Digite um número natural: "))
    if eh_primo(numero):
        contador_primos += 1

print("Quantidade de números primos:", contador_primos)