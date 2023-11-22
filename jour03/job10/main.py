def nombre(n):
    if n > 0:
        print('entier positif')
        if n % 2 == 0:
            print('pair')
        else:
            print('impair') 
    elif n < 0:
        print('entier negatif')
    else:
        print('nul')
    
    
nombre(4)
nombre(5)
nombre(-6)
nombre(0)