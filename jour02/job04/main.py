
n = int(input("Entrez un nombre : "))

for i in range(1,n+1):
    print("")
    print("")
    print("Table de multiplication de", i, ":")
    print("")
    for j in range(1,11):
        produit = j*i
        print(j, "x", i, "=", produit)

