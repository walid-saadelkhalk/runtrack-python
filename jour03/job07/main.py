def developpeur(langage):
    if langage == 'Javascript':
        return 'Tu es un developpeur web'
    elif langage == 'Python':
        return 'Tu es un developpeur IA'
    elif langage == 'Java':
        return 'Tu es un developpeur logiciel'
    elif langage == 'reactjs':
        return 'Tu es un developpeur mobile'
    else:
        return 'Un jour je serai le meilleur developpeur'

print(developpeur('Javascript'))
print(developpeur('Python'))
print(developpeur('Java'))
print(developpeur('reactjs'))
print(developpeur('C++'))

