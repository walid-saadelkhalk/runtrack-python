L = [8, 24, 27, 48, 2, 16, 9, 102, 7, 84, 91]

intervalle = [nombre for nombre in L if nombre >=25 and nombre <=90]

multiplication = 1 

for nombre in intervalle:
    multiplication *= nombre
print(multiplication)
    
