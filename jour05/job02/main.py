def rectangle( longueur, largeur ):
    for i in range(largeur):
        for j in range(longueur):
            if (i == 0 or i == largeur - 1) and (j == 0 or j == longueur - 1):
                print("|", end=" ")
            elif (i == 0 or i == largeur - 1):
                print("-", end=" ")
            elif j == 0 or j == longueur - 1:
                print("|", end=" ")
            else:
                print(" ", end=" ")
        print()

longueur = int(input("Entrez la longueur: "))
largeur = int(input("Entrez la largeur: "))
rectangle(longueur, largeur)