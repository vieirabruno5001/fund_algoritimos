lista1 = [x for x in range(1,7)]
print(list(filter(lambda x: x % 2 != 0,
                  map(lambda x: x+1, lista1))))