def retourner(palindrome):
    retourner = ""
    for lettre in palindrome:
        retourner = lettre + retourner
    return retourner


print(retourner(input("Entrez un palindrome: "))) 

