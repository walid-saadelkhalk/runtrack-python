alphabet = "abcdefghijklmnopqrstuvwxyz"*10
for i in range (27):
    pyramide = ''.join(alphabet[j] for j in range(i + 1))
    if len(pyramide) % 2 != 0:
        print(pyramide)

















