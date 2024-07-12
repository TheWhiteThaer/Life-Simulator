import random as random



def figureSexuality(gender):
    # Determine heterosexuality
    if random.randint(0, 100) > 20:
        return "Heterosexual"
    
    # Determine AroAce
    if random.randint(0, 200) == 1:
        return "AroAce"

    # Determine bisexuality
    if random.randint(0, 100) < 60:
        return "Bisexual"

    # Determine gay or lesbian based on gender
    if gender == "male":
        return "Gay"
    
    elif gender == "female":
        return "Lesbian"
    else:
        return "Gay"
   



def aPeople(gender):
    chancesOfBeingAsexual = random.randint(0, 101)
    if chancesOfBeingAsexual == 1:
        return figureSexuality(gender) + f" [ASexual]"
    elif chancesOfBeingAsexual == 2:
        return figureSexuality(gender) + f" [ARomantical]"
    else:
        return figureSexuality(gender)
    