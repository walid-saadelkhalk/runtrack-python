L = [22.4, 4.0, 16.22, 9.10, 11.00, 12.22, 14.20, 5.20, 17.50]


intervalle = [nombre // 1 for nombre in L]
print(intervalle)


def tri(intervalle):
    n = 0
    for nombre in intervalle:
        n += 1

        for i in range(n):
            for j in range(0, n - i - 1):
                if intervalle[j] > intervalle[j + 1]:
                    temp = intervalle[j]
                    intervalle[j] = intervalle[j + 1]
                    intervalle[j + 1] = temp
    
tri(intervalle)
print(intervalle)

