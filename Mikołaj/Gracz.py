import pygame

class Gracz(object):
    kolor = ( (20, 150, 3),(255, 227, 18), (0, 0, 255),(148, 27, 3))  # red green yellow blue

    ilosc = 0

    pancerz = 1






    def circle(self,number):

        pozycjaPionkiBaza = ((0, 0), (self.game.resolution[1] / 15*2, 0), (0, self.game.resolution[1] / 15*2),(self.game.resolution[1] / 15*2, self.game.resolution[1] / 15*2))  # domyslne pozycje


        if number ==1:
            pozycja= ((self.game.resolution[0]-self.game.resolution[1])/2+self.game.resolution[1]/15*(2),self.game.resolution[1]/15*2)

        if number ==2:
            pozycja= ((self.game.resolution[0]-self.game.resolution[1])/2+self.game.resolution[1]/15*(2)+9*self.game.resolution[1]/15,self.game.resolution[1]/15*2)

        if number ==3:
            pozycja= ((self.game.resolution[0]-self.game.resolution[1])/2+self.game.resolution[1]/15*(2)+9*self.game.resolution[1]/15,self.game.resolution[1]/15*2+9*self.game.resolution[1]/15)

        if number ==4:
            pozycja= ((self.game.resolution[0]-self.game.resolution[1])/2+self.game.resolution[1]/15*(2),self.game.resolution[1]/15*2+9*self.game.resolution[1]/15)

        for i in range(4):
            pygame.draw.circle(self.game.screen, self.kolor[number-1], (int(pozycjaPionkiBaza[i][0]+int(pozycja[0])), int(pozycjaPionkiBaza[i][1]+int(pozycja[1]))), int(self.game.resolution[1]/15/2) )
            print(pozycja[0],pozycja[1])

    def sprRuch(self):
        pass

    def sprWygrana(self):
        pass

class User(Gracz):

    def __init__(self, game):
        self.game = game

    def tick(self):
        pass

    def draw(self,number):
        self.circle(number)

    def wyborPionka(self):
        pionek = input("Jaki pionek:\n")
        print("Wybrano pionek nr. " + pionek)
        return pionek
