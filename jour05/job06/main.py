marche = int(input("Nombre de marche: "))
hauteur = int(input("Hauteur de marche: "))
distance = marche * hauteur

def denivele(marche, hauteur):
        return ((distance)*70) /100

print(f"pour {marche} marches de {hauteur} cm, le gardien parcourt {denivele(marche, hauteur)} m par semaine.")
 


        
