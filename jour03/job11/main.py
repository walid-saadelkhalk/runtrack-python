def time_to_text(timer):
    if timer>=0:
        heure = timer // 60
        minutes = timer % 60
        print(heure, "heures", minutes, "minutes")
    else:
        print("Vous ne pouvez pas remonter le temps")



time_to_text(140)
time_to_text(30)
time_to_text(-20)

# autre façon de faire
def temps(minute):
    envoi=0
    heure = -1
    while envoi < minute:
        envoi +=60
        heure +=1
    time = envoi - minute
    minute = 60 - time
    print(heure, "heure", minute, "minutes")

temps(50)

# autre façon de faire
def temps(minute):
    heure = 0
    
    while minute >=60:
        minute -=60
        heure +=1

    print(heure, "heure", minute, "minutes")

temps(50)
temps(140)
temps(230)