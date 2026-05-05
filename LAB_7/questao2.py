x = 5
def f1():
    global x
    x = 4
def f2(a,b):
    x = 3
    return a + b + x
f1()
total = f2(1,2)
print(total)