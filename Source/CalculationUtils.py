import math
def Calculate_Radius_Based_On_Number(number):
    base_radius = 20  # Base radius size
    scaling_factor = 1.15  # Adjust this factor to get the desired size range
    return base_radius / math.log(number + 1, scaling_factor)

#TODO: fix it
def Calculate_Distance_Based_On_Number(width, number):
    base_radius = 20  # Base radius size
    scaling_factor = width * width * width  # Adjust this factor to get the desired size range
    return base_radius / math.log(number + 1, scaling_factor)

def People_Counter_Based_On_Sexuality(Human, Counter):
    for i in range(0, len(Human)):
        if Human[i].sexuality in Counter:
            Counter[Human[i].sexuality] += 1
