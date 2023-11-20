nom = "places de musée"
prix_unitaire = 10
quantite = 10000
revenu = prix_unitaire * quantite
print("Le revenu de la vente des", quantite, nom, "est de", revenu, "euros.")
new_revenu = (prix_unitaire + prix_unitaire * 0.1) * quantite
print("Le nouveau revenu de la vente des", quantite, nom, "est de", new_revenu, "euros.")