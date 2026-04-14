def quadrado(num):
    return num*num
lista = [1,2,3,4,5]
lista_ao_quadrado = []
for i in range (len(lista)):
    lista_ao_quadrado.append(quadrado(lista[i]))

print(lista)
print(lista_ao_quadrado)
print(list(map(quadrado, lista)))