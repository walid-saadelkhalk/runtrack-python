


def betalpha(alphabet):
  
    betalpha = ""
   
    for lettre in alphabet:
        
        betalpha = lettre + betalpha
    
    return betalpha


alphabet = "abcdefghijklmnopqrstuvwxyz"

print(f"original: {alphabet}")

print(f"inversé: {betalpha(alphabet)}")
