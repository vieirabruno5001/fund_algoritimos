arquivo = open("teste.txt", "w")

for linha in range(1,101):
    arquivo.write(f"linha{linha}\n")

arquivo.close()