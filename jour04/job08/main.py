L = [8, 24, 27, 48, 2, 16, 9, 7, 84, 91]

def add(L):
    paire = [ nombre for nombre in L if nombre % 2 == 0 ]
    return sum(paire)
    
print(add(L))