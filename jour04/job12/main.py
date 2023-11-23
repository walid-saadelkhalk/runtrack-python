L = [8, 24, 27, 48, 2, 16, 9, 102, 7, 84, 91]

def tri(L):
    n = 0
    for nombre in L:
        n += 1

        for i in range(n):
            for j in range(0, n - i - 1):
                if L[j] > L[j + 1]:
                    temp = L[j]
                    L[j] = L[j + 1]
                    L[j + 1] = temp
    
tri(L)
print(L)


