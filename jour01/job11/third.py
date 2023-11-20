import random
alphabet = "abcdefghijklmnopqrstuvwxyz" 

lettres = list(alphabet)
random.shuffle(lettres)
print("alphabet dans le désordre", lettres)

lettres.sort()
print("alphabet dans l'ordre", lettres)

alphabet_string = "".join(lettres)
print("l'alphabet à nouveau dans une string:", alphabet_string)