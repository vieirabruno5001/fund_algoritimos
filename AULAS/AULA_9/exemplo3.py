def starts_with_a(word):
    return word[0] == 'a'

lista = ['abacate','abacaxi','laranja','limao','amora']

print(list(filter(starts_with_a, lista)))
