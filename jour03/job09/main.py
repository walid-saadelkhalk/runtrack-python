def moyenne(maths, physique, sport):
    moyenne_etudiant = round((maths + physique + sport) / 3)

    if moyenne_etudiant >= 15 and moyenne_etudiant <= 20:
        print("Très bon élève") 
    elif moyenne_etudiant >= 11 and moyenne_etudiant <= 14:
        print("Bon eleve") 
    elif moyenne_etudiant >= 8 and moyenne_etudiant <= 10:
        print("Élève moyen") 
    elif moyenne_etudiant >= 0 and moyenne_etudiant <= 7:
        print("Élève devant faire des efforts") 
    else:
        print("Moyenne non valide") 
    return moyenne_etudiant    

maths = float(input("Note en Maths: "))
physique = float(input("Note en Physique: "))
sport = float(input("Note en Sport: "))

print("moyenne de l'étudiant: ", moyenne(maths, physique, sport))

