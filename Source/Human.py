import Sexuality
import random
from threading import Timer
import pygame
import Window
import json
class Human():

    def __init__(self) -> None:
        FileContent = open("Data/Humans.json")
        jsonFile = json.load(FileContent)
        randomProp = random.randint(0, len(jsonFile) - 1)
        self.Name = jsonFile[randomProp]["name"]
        self.Age = jsonFile[randomProp]["age"]
        self.SkinColor = jsonFile[randomProp]["skin_color"]
        self.EyeColor = jsonFile[randomProp]["eye_color"]
        self.Gender = jsonFile[randomProp]["gender"]
        self.Religion = "Muslim" #For Now
        self.Sexuality = Sexuality.aPeople(jsonFile[randomProp]["gender"])

        self.x = 0
        self.y = 0


        # self.XDirection = 1
        # self.YDirection = 1

        # self.Move = random.choice([True, False])
        # self.MoveDown = random.choice([True, False])

        # self.MovingX = random.randint(0, 2)
        # self.MovingY = random.random()





        colorsFile = open("Data/SexualitiesColor.json")
        colors = json.load(colorsFile)

        self.color = (255, 255, 255)
        
        if "ASexual" in self.Sexuality:
            self.color = colors["Asexual"]['rgb']
        
        if "ARomantical" in self.Sexuality:
            self.color = colors["Aromantic"]['rgb']


        if self.Sexuality in colors:
            self.color = colors[self.Sexuality]['rgb']
        


    # #NOT READY TODO: FIX IT
    # def AI(self):

    #     #Random Timer Between 0, 10 Before Starting

    #     if self.Move == False:
    #         return


    #     if self.x >= Window.WIDTH or self.x <= 0:
    #         #Stop For 0, 5 Seconds
    #         self.XDirection = -self.XDirection

    #     if self.y >= Window.HEIGHT or self.y <= 0:
    #         self.YDirection = -self.YDirection

        
    #     #Random Timer Between 0, 20 Stopping For A While Then Complete
    #     if self.MoveDown:
    #         self.y += self.MovingY * self.YDirection
        
    #     self.x += self.MovingX * self.XDirection
