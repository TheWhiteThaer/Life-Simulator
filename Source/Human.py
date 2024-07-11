import Sexuality
import random
import time
import pygame
class Human():
    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age
        self.sexuality = Sexuality.aPeople()
        self.x = 100
        self.y = 100

        
        if self.sexuality == "Gay":
            self.color = (135, 206, 235)
        elif self.sexuality == "Lesbian":
            self.color = (255, 0, 255)
        elif self.sexuality == "Bisexual":
            self.color = (128,0,128)
        elif self.sexuality == "AroAce":
            self.color = (90, 255, 0)
        else:
            self.color = (0, 0, 0)


    def AI(self):
        pass
            
    def a(self):
        print("stmh")