import pygame #type: ignore
from pygame.locals import * # type: ignore
import Human
import random
import Game
import CalculationUtils
import Window
import json
import Sexuality


class Main(Game.Game):

    # Humans #
    HumansNumber = None
    Humans = None
    

    # Counter #
    Counter = None
    Sexualities = None
    calculated = False



    # Fonts
    normalFont = None
    pixelSans = None

    radius = None



    def __init__(self, width, height, FPS, title):
        self.init_variables()
        self.addHumans(self.HumansNumber, self.Humans)
        super().__init__(width, height, FPS, title)

    def init_variables(self):
        # Humans #
        self.HumansNumber = 100
        

        self.Humans = []
    

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

    
    
    def addHumans(self, numberOfPoeple, List):
        for i in range(0, numberOfPoeple):
            # Load human data from JSON file
            with open("Data/Humans.json") as file:
                humans = json.load(file)
            
            human = random.choice(humans)

            newHuman = Human.Human(
                human['name'],
                human['age'],
                human['skin_color'],
                human['eye_color'],
                human['gender'],
                Sexuality.GetSexuality(human['gender']),
                random.choice(["Muslim", "Chrisitain", "Jew"])
            )
            List.append(newHuman)
        
    
    def restartSimulation(self):
        self.Humans = []
        self.init_variables()
        self.addHumans(self.HumansNumber, self.Humans)
        CalculationUtils.People_Counter_Based_On_Sexuality(self.Humans, self.Counter)
        self.calculated = False
        self.restart = False

    def create(self):
        self.normalFont = pygame.font.Font('freesansbold.ttf', 32)
        self.pixelSans = pygame.font.Font('Assets/Fonts/SansPixels.ttf', 22)
        CalculationUtils.People_Counter_Based_On_Sexuality(self.Humans, self.Counter)
        
        return super().create()
    

    

    def HumanManager(self, AIMode = "AI"):
        if AIMode == "Standing Still":
            HumanYPosition = 0
            HumanXPosition = 0
            NumberOfPoepleInARow = CalculationUtils.Calculate_Number_Of_People_On_A_Row(self.radius, self.HumansNumber)
            NumberOfPoepleInAColum = 5
            for i in range(len(self.Humans)):
                if i % NumberOfPoepleInARow == 0:
                    HumanYPosition += (Window.HEIGHT - self.radius * 2) /  NumberOfPoepleInAColum
                    HumanXPosition = 0

                HumanXPosition += (Window.WIDTH - self.radius * 2) /  NumberOfPoepleInARow
                
                pygame.draw.circle(self.displaysurface, self.Humans[i].color, (HumanXPosition, HumanYPosition), int(self.radius))
                self.Humans[i].Position.x = HumanXPosition
                self.Humans[i].Position.y = HumanYPosition
        else:
            for i in range(len(self.Humans)):
                self.Humans[i].AI()
                pygame.draw.circle(self.displaysurface, self.Humans[i].color, (self.Humans[i].Position.x, self.Humans[i].Position.y), int(self.radius))


    def IDInfo(self, IDPosition):
        Texts = [
            ["Name", self.Humans[self.curHuman].Name],
            ["Age", self.Humans[self.curHuman].Age],
            ["Gender", self.Humans[self.curHuman].Gender],
            ["Religion", self.Humans[self.curHuman].Religion],
            ["Skin Color", self.Humans[self.curHuman].SkinColor],
            ["Sexuality", self.Humans[self.curHuman].Sexuality]
        ]

        TextPosition = [IDPosition[0] + 250, 230]
        for i in range(0, len(Texts)):
            TextPosition[1] += 30
            Text = self.pixelSans.render(
                f'{Texts[i][0]} : {Texts[i][1]}', 
                True, 
                (0, 0, 0)
            )
            self.displaysurface.blit(Text, TextPosition)



    def IDLogic(self):
         
        circleSelector = pygame.Surface((Window.WIDTH, Window.HEIGHT))
        circleSelector.set_colorkey((0,0,0))
        circleSelector.set_alpha(128)
        pygame.draw.circle (
            circleSelector, #Surface 
            (0, 1, 0), #Color
            (
                self.Humans[self.curHuman].Position.x, # X Position
                self.Humans[self.curHuman].Position.y  # Y Position
            ),
            int(self.radius) + 3 # Radius
        )
        self.displaysurface.blit(circleSelector, (0, 0))


        ID = pygame.image.load(f"Assets/Images/{str.capitalize(self.Humans[self.curHuman].Gender)}ID.png")
        ID = pygame.transform.scale(ID, (128 * 5, 64 * 5))



        IDPosition = (
            Window.WIDTH / 2 - ID.get_width() / 2, 
            Window.HEIGHT / 2 - ID.get_height() / 2
        )

        

        if not self.canShowID:
            IDPosition = (
                10000,
                10000
            )
        
        self.displaysurface.blit(
            ID,
            IDPosition
        )

        self.IDInfo(IDPosition)

    def update(self):


        #Calculating The Max Circ Border
        self.radius = CalculationUtils.Calculate_Radius_Based_On_Number(self.HumansNumber)

        self.HumanManager("Normal")

        CounterText = self.normalFont.render(
            f'The Number Of {self.Sexualities[self.curSexuality]} People Is {self.Counter[self.Sexualities[self.curSexuality]]}', 
            True, 
            (0, 0, 0)
        )
        self.displaysurface.blit(CounterText, (0, 600))
        
        self.IDLogic()

        if self.restart:
            self.restartSimulation()

        self.Humans[self.curHuman].Position.x = Window.WIDTH / int(self.radius) * 6
        self.Humans[self.curHuman].Position.y = Window.HEIGHT / int(self.radius) * 6

        super().update()
    


if __name__ == "__main__":
    game = Main(Window.WIDTH, Window.HEIGHT, Window.FPS, Window.TITLE)
    game.run()