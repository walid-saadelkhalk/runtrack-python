note = int(input("Entrez votre note: "))
muliple_5 = ((note +4)// 5) * 5

def moyenne(note):    
    if note < 40:
        print ("Echec")
        return note
    elif note > 40:
        print ("Reussite")
        if muliple_5 - note < 3:
            return muliple_5 
        else:
            return note
    else:
        print ("Recommencez le test")
        return note
print(moyenne(note))