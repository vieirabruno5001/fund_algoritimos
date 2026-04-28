numeros = [ x for x in range (1000)]


arquivo_par = open('pares.txt','w')
arquivo_impar = open('impares.txt','w')
for x in numeros:
    if x % 2 == 0:
        arquivo_par.write(f'{x}\n')
    else:
        arquivo_impar.write(f'{x}\n')

arquivo_par.close()
arquivo_impar.close()
