L = [4, "Un test de primalité est un algorithme permettant de savoir si un nombre entier est premier."]



def longueur_mot(mot):
    longueur = 0
    for _ in mot:
        longueur += 1
    return longueur

def my_long_word(longueur_minimale, phrase):
    mot_actuel = ""
    resultat = ""
    en_mot = False

    for letter in phrase:
        # if letter.isalpha():
        separators = " \t\r\n.,;:!?-()[]{}'"
        if not letter in separators:
            mot_actuel += letter
            en_mot = True
        elif en_mot:
            if longueur_mot(mot_actuel) > longueur_minimale:
                resultat += mot_actuel + " "
            mot_actuel = ""
            en_mot = False

    if longueur_mot(mot_actuel) > longueur_minimale:
        resultat += mot_actuel

    return resultat

longueur_minimale = 4
phrase = "Un test de primalité est un algorithme permettant de savoir si un nombre entier est premier."

resultat = my_long_word(longueur_minimale, phrase)
print("Output:", resultat)