import pygame

class Game():
    
    #Restarting
    restart = False

    #Selecting Modes
    curSexuality = 0

    curHuman = 0

    #Id Stuff
    canShowID = False

    #Increase
    AddedHumans = {
        "Increase" : 0,
        "Decrease": 0
    }

    AddingOrNot = ""


    def __init__(self, width, height, FPS, title) -> None:
        self.width = width
        self.height = height
        self.FPS = FPS
        self.title = title
        
        # Starting the game
        pygame.init()
        
        # Creating a clock object to control the frame rate
        self.FramePerSec = pygame.time.Clock()
        
        # Setting up the display surface
        self.displaysurface = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption(self.title)

    def run(self):
        self.create()
        while True:
            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    pygame.quit()
                    return
               
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_F5:
                        self.restart = True

                    if event.key == pygame.K_LEFT:
                        self.changeSexuality(-1)
                                        
                      
                    elif event.key == pygame.K_RIGHT:
                        self.changeSexuality(1)



                    if event.key == pygame.K_d:
                        self.changeHuman(1)
                      
                    elif event.key == pygame.K_a:                 
                        self.changeHuman(-1)



                    if event.key == pygame.K_h:
                        self.canShowID = not self.canShowID
                    
                    if event.key == pygame.K_EQUALS:
                        self.AddedHumans["Increase"] += 1
                        self.AddingOrNot = "Increase"
                    elif event.key == pygame.K_MINUS:
                        self.AddedHumans["Decrease"] += 1 * -1
                        self.AddingOrNot = "Decrease"

                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_MINUS:
                        self.AddedHumans["Decrease"] = 0
                    elif event.key == pygame.K_EQUALS:
                        self.AddedHumans["Increase"] = 0
                       
            self.displaysurface.fill((255, 255, 255))
            self.update()
            pygame.display.update()
            self.FramePerSec.tick(self.FPS)

    def update(self):
        pass

    def create(self):
        pass


    def changeSexuality(self, huh):
        self.curSexuality += huh

        if self.curSexuality > len(self.Sexualities) - 1:
                self.curSexuality = 0
        if self.curSexuality < 0:
                self.curSexuality = len(self.Sexualities) - 1


    def changeHuman(self, huh):
        self.curHuman += huh

        if self.curHuman > len(self.Humans) - 1:
                self.curHuman = 0
        if self.curHuman < 0:
                self.curHuman = len(self.Humans) - 1