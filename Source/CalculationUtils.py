import math
import Window
import random
def Calculate_Radius_Based_On_Number(number):
    return Window.WIDTH / number

#TODO: fix it
def Calculate_Number_Of_People_On_A_COLUM(circleR, number):
    for i in range(0, number):
        S = circleR * (circleR *(3/4)) * math.pi * i
        if S >= Window.HEIGHT:
            return i


def Calculate_Number_Of_People_On_A_Row(circleR, number):
    for i in range(0, number):
        S = circleR * 1.5 * math.pi * i
        if S >= Window.WIDTH:
            return i
        

def People_Counter_Based_On_Sexuality(Human, Counter:map):
    #First One To Rest
    for i in range(0, len(Human)):
        Counter[Human[i].Sexuality] = 0
    #Second One To Assign
    for i in range(0, len(Human)):
        if Human[i].Sexuality in Counter:
            Counter[Human[i].Sexuality] += 1
                    
def check_collision(circle1, circle2, radius):
        # Get the center positions of the circles
        x1, y1 = circle1.center
        x2, y2 = circle2.center

        # Calculate the distance between the centers
        distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

        # Check if the distance is less than the sum of the radii
        return distance < 2 * radius
    

def resolve_collision(human1, human2, radius):
    # Move humans away from each other
    x1, y1 = human1.Position.x, human1.Position.y
    x2, y2 = human2.Position.x, human2.Position.y

    # Calculate the direction to move the humans
    dx, dy = x2 - x1, y2 - y1
    distance = math.sqrt(dx ** 2 + dy ** 2)

    if distance == 0:  # To prevent division by zero
        angle = random.uniform(0, 2 * math.pi)
        dx, dy = math.cos(angle), math.sin(angle)
    else:
        dx, dy = dx / distance, dy / distance

    # Move each human away from the collision point
    move_distance = radius - distance / 2
    human1.Position.x -= dx * move_distance
    human1.Position.y -= dy * move_distance
    human2.Position.x += dx * move_distance
    human2.Position.y += dy * move_distance
