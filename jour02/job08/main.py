def triangle(a, b, c):

        
    if a + b > c and a + c > b and b + c > a:
        if a == b == c:
            return "Il s'agit d'un triangle équilatéral"
        elif a == b or a == c or b == c and a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2:  
            return "Il s'agit d'un triangle rectangle isocèle"
        elif a == b or a == c or b == c:
            return "Il s'agit d'un triangle isocèle"
        elif a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2:
            return "Il s'agit d'un triangle rectangle"
        elif a != b != c:
            return "Il s'agit d'un triangle scalène"
    else: 
        return "Il ne s'agit pas d'un triangle car la somme des deux côtés les plus courts est inférieure au troisième côté"

a = float(input("Longueur de a : "))
b = float(input("Longueur de b : "))
c = float(input("Longueur de c : "))

resultat = triangle(a, b, c)
print(resultat)



        