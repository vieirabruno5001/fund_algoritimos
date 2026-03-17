n = int(input("digite N: "))

total_primo = 0 

for i in range(n):
    x = int(input("digite x: "))
    if x > 1:
     primo = 1
    for j in range(2,x):
        if x % j == 0:
            primo = 0
            break
        total_primo += primo
print(f"total primos = {total_primo}")