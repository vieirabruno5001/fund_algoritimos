x = input()
form = {
    "janeiro" : "31 dias",
    "fevereiro" : "28 ou 29 dias",
    "março" : "31 dias",
    "abril" : "30 dias",
    "maio" : "31 dias",
    "junho" : "30  dias",
    "julho" : "31 dias"
}

if x in form:
    print(f"{form[x]}")
