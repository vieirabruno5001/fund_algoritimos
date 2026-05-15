import math
def caular_hip(p,s):
    return math.sqrt(p**2 + s**2)

p = int(input("Digite o primeiro lado do triângulo: "))
s = int(input("Digite o segundo lado do triângulo: "))

hip = caular_hip(p, s)
print(f"Hipotenusa: {hip:.2f}")