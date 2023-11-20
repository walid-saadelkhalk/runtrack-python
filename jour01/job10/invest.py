montant_init = 3000
taux_de_rendement = 0.1



'''premier gain'''
gain_annuel = montant_init * taux_de_rendement
print( gain_annuel)
'''fin premier gain'''


'''deuxieme gain'''
gain_annuel += 5000
taux_de_rendement += 0.02
new_gain_annuel = (gain_annuel + montant_init) * taux_de_rendement
print(new_gain_annuel)
'''fin deuxieme gain'''


montant_total = montant_init + gain_annuel + new_gain_annuel
retrait = montant_total * 0.1
taux_de_rendement -= 0.01
gain_final = (montant_total - retrait) * taux_de_rendement
print(montant_total)
print(gain_final)