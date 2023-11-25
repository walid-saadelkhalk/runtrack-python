def diagonale(n):
    for i in range(n+1):
        for j in range(n+1):
            if i == n - j - 1:
                print("#", end=" ")
            else:
                print("#", end="")
        print()
diagonale(10)