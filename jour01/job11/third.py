import random
alphabet = "abcdefghijklmnopqrstuvwxyz" 

lettres = list(alphabet)
random.shuffle(lettres)
print("alphabet dans le désordre", lettres)

ascii = [ord(lettre) for lettre in alphabet]

print("l'alphabet en ascii", ascii)
ascii.sort()
print("l'alphabet en ascii dans l'ordre", ascii)

alphabet_ascii = [chr(code) for code in ascii]
print("l'alphabet en ascii dans l'ordre", alphabet_ascii)

final_alphabet= "".join(alphabet_ascii)
print("l'alphabet dans l'ordre", final_alphabet)