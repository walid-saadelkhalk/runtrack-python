def agricole( type, saison):
    if type == "fruit":
        if saison == "hiver":
            return "orange, mandarine et kiwi"
        elif saison == "ete":
            return "Poire, fraise, cassis"
    elif type == "legume":
        if saison == "hiver":
            return "carotte, topinambour, endive"
        elif saison == "ete":
            return "artichaut, aubergine, navet"
        else:
            return "Mangez cinq fruits et légumes par jour"

print(agricole("fruit", "hiver"))
print(agricole("fruit", "ete"))
print(agricole("legume", "hiver"))
print(agricole("legume", "ete"))
print(agricole("legume", "printemps"))

      