from random import randint, random
inteiros = [randint(0,100) for x in range(10)]
print(inteiros)

reais = [random () * 100 for x in range (5)]
print(reais)

palavras = ['murilo','bruno','lets get it']
print(palavras)

completa = []
completa.append(inteiros.copy())
completa.append(reais.copy())
completa.append(palavras.copy())
print(completa)

inteiros.clear()
reais.clear()
palavras.clear()

for i in range(len(completa)):
    for j in range (len(completa[i])):
     print(completa[i][j])