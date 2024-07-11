import random as random




def figureSexuality():
    chanceOfBeinAroAce = random.randint(0, 101)
    if chanceOfBeinAroAce == 1:
        return "AroAce"
    

    chanceOfBeingGay = random.randint(0, 101)
    if chanceOfBeingGay > 6:
        return "Heterosexual"
    
    
    chanceOfBeingBiOrHomo = random.randint(0, 101)
    if chanceOfBeingBiOrHomo < 80:
        return "Bisexual"

    chanceOfBeingGayOrLesbian = random.randint(0, 101)
    if chanceOfBeingGayOrLesbian < 70:
        return "Gay"
    else:
        return "Lesbian"




def aPeople():
    chancesOfBeingAsexual = random.randint(0, 101)
    if chancesOfBeingAsexual == 1:
        return figureSexuality() + f" [ASexual]"
    elif chancesOfBeingAsexual == 2:
        return figureSexuality() + f" [ARomantical]"
    else:
        return figureSexuality()
    