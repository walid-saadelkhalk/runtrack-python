import random
alphabet = "abcdefghijklmnopqrstuvwxyz" 

lettres = list(alphabet)
random.shuffle(lettres)
print(lettres)

lettres.sort()
print(lettres)