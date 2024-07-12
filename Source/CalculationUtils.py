import math
import Window
def Calculate_Radius_Based_On_Number(number):
    return Window.WIDTH / number

#TODO: fix it
def Calculate_Distance_Based_On_Number(number):
    pass


def Calculate_Number_Of_People_On_A_Row(circleR, number):
    for i in range(0, number):
        S = circleR * 1.5 * math.pi * i
        if S >= Window.WIDTH:
            return i
        

def People_Counter_Based_On_Sexuality(Human, Counter):
    for i in range(0, len(Human)):
        if Human[i].Sexuality in Counter:
            Counter[Human[i].Sexuality] += 1
