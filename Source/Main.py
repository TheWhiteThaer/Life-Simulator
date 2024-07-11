import pygame #type: ignore
from pygame.locals import * # type: ignore
import Human as Human
import random as random 
import Game as Game
import CalculationUtils


class Main(Game.Game):

    # Humans #
    HumansNumber = None
    Humans = None
    

    #TODO: Make The Names, Age, ... etc in a json file
    NAMES = None


    # Counter #
    Counter = None
    Sexualities = None
    calculated = False



    # Positions #
    XAdd = 50
    YAdd = 50

    # Multiplayers #
    RadiusMultiplayer = 15

    #Temps
    done = False


    # Text
    font = None
    CounterText = None



    def __init__(self, width, height, FPS, title):
        self.init_variables()
        self.addHumans(self.HumansNumber, self.NAMES, 0, 51, self.Humans)
        super().__init__(width, height, FPS, title)

    def init_variables(self):
        # Humans #
        self.HumansNumber = 100

        self.Humans = []
        

        #TODO: Make The Names, Age, ... etc in a json file
        self.NAMES = [
            "Alex",
            "Maria",
            "Mary",
            "Hot Dog",
            "Max",
            "David",
            "Sara"
        ]


        # Counter #
        self.Counter = {
            'Heterosexual': 0,
            'Gay': 0,
            'Lesbian': 0,
            'Bisexual': 0,
            'AroAce': 0
        }

        # Counter #
        self.Sexualities = [
            'Heterosexual',
            'Gay',
            'Lesbian',
            'Bisexual',
            'AroAce'
        ]

    def addHumans(self, numberOfPoeple, Names, MinAge, MaxAge, List):
        for i in range(0, numberOfPoeple):
            newHuman = Human.Human(random.choice(Names), random.randint(MinAge, MaxAge))
            List.append(newHuman)
        
    
    def restartSimulation(self):
        self.Humans = []
        self.init_variables()
        self.addHumans(self.HumansNumber, self.NAMES, 0, 51, self.Humans)
        CalculationUtils.People_Counter_Based_On_Sexuality(self.Humans, self.Counter)
        self.calculated = False
        self.restart = False

    def create(self):
        self.font = pygame.font.Font('freesansbold.ttf', 32)
        CalculationUtils.People_Counter_Based_On_Sexuality(self.Humans, self.Counter)
        return super().create()
    

    def update(self):
        
        HumanYPosition = 0
        HumanXPosition = 0
        
        #Calculating The Max Circ Border
        radius = CalculationUtils.Calculate_Radius_Based_On_Number(self.HumansNumber) * self.RadiusMultiplayer

        diameter = 2 * radius
        
        num_circles_per_row = int(self.width // diameter)
        
        
        for i in range(len(self.Humans)):
            # Move to the next row every 15 humans
            # r = 9.085046112998343
            # w = 1280
            #
            if i % 15 == 0:
                HumanYPosition += 50 * ((radius / self.RadiusMultiplayer) / 1.5)
                HumanXPosition = 0

            HumanXPosition += self.XAdd * ((radius / self.RadiusMultiplayer)  + 0.01)

            # Update the x position for the next human in the row
            # Draw the circle
            self.Humans[i].AI()
            pygame.draw.circle(self.displaysurface, self.Humans[i].color, (HumanXPosition, HumanYPosition), int(radius))
            self.CounterText = self.font.render(
                f'The Number Of {self.Sexualities[self.curSelected]} People Is {self.Counter[self.Sexualities[self.curSelected]]}', 
                True, 
                (0, 0, 0)
            )
        self.displaysurface.blit(self.CounterText ,(0, 680))
        
        if self.restart:
            self.restartSimulation()
            
        if not self.done:
            for i in range(0, len(self.Humans)):
                if self.Humans[i].sexuality in self.Counter:
                    pass
            self.done = True


        super().update()
    


if __name__ == "__main__":
    game = Main(1280, 720, 60, "Game")
    game.run()