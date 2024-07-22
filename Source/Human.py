import random
import json
import time
from Vectors import Vector2  # Corrected import
import Sexuality  # Assuming Sexuality.GetSexuality is defined elsewhere
import Window  # Assuming Window has WIDTH and HEIGHT constants

class Human:
    def __init__(self, Name, Age, SkinColor, EyeColor, Gender, Sexuality, Religion) -> None:
        
        self.Name = Name
        self.Age = Age
        self.SkinColor = SkinColor
        self.EyeColor = EyeColor
        self.Gender = Gender
        self.Sexuality = Sexuality
        self.Religion = Religion

        
        self.Position = Vector2(10, 10)
        self.Move = random.choice([True, False])
        self.MoveDown = random.choice([True, False])
        self.MoveOneDirection = random.choice([True, False])
        self.Moves = {'x': random.uniform(0, 1), 'y': random.uniform(0, 1)}
        self.Direction = {'x': 1, 'y': 1}
        self.Sorted = False
        self.StartTimer = time.time()  # Initialize start time
        self.WaitToStart = random.uniform(1, 3)  # Wait time before starting movement
        self.WaitToChangeDirection = random.uniform(1, 3)  # Wait time before changing direction
        self.BorderReachedTime = None  # Time when the border is reached
        self.DelayBeforeDirectionChange = 1  # Delay before changing direction
        self.WaitUntilDone = random.uniform(4, 15)  # Time until movement toggle

        # Load sexuality colors from JSON file
        with open("Data/SexualitiesColor.json") as file:
            colors = json.load(file)
        
        self.color = (255, 255, 255)  # Default color
        
        # Check for specific sexualities and set color
        for key in ["ASexual", "ARomantical"]:
            if key in self.Sexuality:
                self.color = colors.get(key.lower(), {}).get('rgb', self.color)
        
        self.color = colors.get(self.Sexuality, {}).get('rgb', self.color)

    def AI(self):
        if not self.Sorted:
            self.Position.x = random.randint(0, Window.WIDTH)
            self.Position.y = random.randint(0, Window.HEIGHT)
            self.Sorted = True

        elapsed_time = time.time() - self.StartTimer

        if elapsed_time >= self.WaitToStart:
            if not self.Move:
                return

            if self.MoveDown:
                self.Position.y += self.Moves['y'] * self.Direction['y']

            if self.Position.x >= Window.WIDTH or self.Position.x < 0 or self.Position.y >= Window.HEIGHT or self.Position.y < 0:
                if self.BorderReachedTime is None:
                    self.BorderReachedTime = time.time()

                if time.time() - self.BorderReachedTime >= self.DelayBeforeDirectionChange:
                    if self.Position.x >= Window.WIDTH or self.Position.x < 0:
                        if self.MoveOneDirection:
                            self.Direction['y'] = 0
                        else:
                            self.Direction['y'] = 1
                        self.Direction['x'] *= -1

                    if self.Position.y >= Window.HEIGHT or self.Position.y < 0:
                        if self.MoveOneDirection:
                            self.Direction['x'] = 0
                        else:
                            self.Direction['x'] = 1
                        self.Direction['y'] *= -1

                    self.BorderReachedTime = None  # Reset the border reached time

            self.Position.x += self.Moves['x'] * self.Direction['x']

        if elapsed_time >= self.WaitUntilDone:
            self.Move = random.choice([True, True, True, False])
            self.StartTimer = time.time()  # Reset start timer for the next cycle
