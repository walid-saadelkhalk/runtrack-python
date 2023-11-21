liste_nombres = list(range(1, 101))

for nombre in liste_nombres:
    
    if nombre % 3 == 0 and nombre % 5 == 0:
        print("FizzBuzz")
    elif nombre % 5 == 0:
        print("Buzz")
    elif nombre % 3 == 0:
        print("Fizz")
    else:
        print(nombre)
  