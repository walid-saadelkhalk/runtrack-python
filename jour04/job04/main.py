def liste_fruits(fruits):
    print(fruits)


def ajouter_mangue(liste_fruits):
    liste_fruits.insert(2, "Mangue")
    
fruits = ["pomme", "cerise","orange", "Melon"]
ajouter_mangue(fruits)
print(fruits)