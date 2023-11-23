L = [10,20,30,20,10,50,60,40,80,50,40]

def deleted(L):
    nombre_unique = []

    for nombre in L:
        if nombre not in nombre_unique:
            nombre_unique += [nombre]
    return nombre_unique
final = deleted(L)
print(final)
