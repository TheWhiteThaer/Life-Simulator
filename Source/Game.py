import pygame

class Game():
    
    restart = False

    direction = 0

    #Selecting Modes
    curSelected = 0


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
                        self.curSelected -= 1
                                        
                        if self.curSelected < 0:
                            self.curSelected = len(self.Sexualities) - 1
                    elif event.key == pygame.K_RIGHT:                        
                        self.curSelected += 1
                        if self.curSelected > len(self.Sexualities) - 1:
                                self.curSelected = 0
                       
            self.displaysurface.fill((255, 255, 255))
            self.update()
            pygame.display.update()
            self.FramePerSec.tick(self.FPS)

    def update(self):
        pass

    def create(self):
        pass
