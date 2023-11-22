def difference(nombre):
    if nombre > 0:
        return 'positif'
    elif nombre < 0:
        return 'negatif'
    else:
        return 'nul'

print(difference(4))
print(difference(-6))
print(difference(0))