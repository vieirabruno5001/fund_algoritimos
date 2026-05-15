def media(n1, n2, n3, letra):
    if letra =="A":
        return (n1 + n2 + n3) / 3
    elif letra == "P":
            return (5*n1 + 3*n2 + 2*n3) / 10
    else:
         return None
print(media(2,3,4,'A'))