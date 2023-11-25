alphabet = "abcdefghijklmnopqrstuvwxyz"

def encodage(message, decalage):
    message_code = ""
    for lettre in message:
        if lettre in alphabet:
            index = alphabet.index(lettre)
            index = (index + decalage) % 26
            message_code += alphabet[index]
        else:
            message_code += lettre
    return message_code

print(encodage(input("Rentrez votre mot pour l'encoder:"),3))

def decodage(message, decalage):
    message_decode = ""
    for lettre in message:
        if lettre in alphabet:
            index = alphabet.index(lettre)
            index = (index - decalage) % 26
            message_decode += alphabet[index]
        else:
            message_decode += lettre
    return message_decode

print(decodage(input("Rentrez votre mot pour le decoder:"), 3))