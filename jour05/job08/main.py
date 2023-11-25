L = [42, 24, -12, 13, -95, -16, 112, 11, 22]
tri = 0
def my_sort(L, tri = 0):
    for i in range (len(L) - 1):
        element = L[i]
        element_suivant =  L[i + 1]
        tri += 1
        if element > element_suivant:
            L[i] = element_suivant
            L[i + 1] = element
            my_sort(L)
    return L, tri 

liste_triee, tri = my_sort(L)

print("Nombre de coups nécessaire pour trier la liste :", tri)
print("Liste triée :", liste_triee)