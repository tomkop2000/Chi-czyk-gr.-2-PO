import pygame, sys

class Gracz():
    kolor = ( (20, 150, 3),(255, 227, 18), (0, 0, 255),(148, 27, 3))  # red green yellow blue

    ilosc = 0

    pancerz = 1

    def __init__(self, game):
        self.game = game

    pozycja=(0,0,0,0)


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

    def sprRuch(self, a, b ,c ,d,oczka,pionek):
        for x in range(4):
            if (a.pozycja[pionek]+oczka)!=b.pozycja[x]:
                print("nowa pozycja")

            elif (a.pozycja[pionek]+oczka)!=c.pozycja[x]:
                print("nowa pozycja")

            elif (a.pozycja[pionek]+oczka)!=d.pozycja[x]:
                print("nowa pozycja")

            else:
                print("stara pozycja")

    def sprWygrana(self):
        pass

class User(Gracz):


    def tick(self):
        self.wyborPionka()

    def draw(self,number):
        self.circle(number)

    def wyborPionka(self):

        pygame.event.clear()

        print("Jaki pionek:\n")

        event = pygame.event.wait()

        pionek = 0

        if event.type == pygame.KEYDOWN and event.key == pygame.K_1:
            pionek = 1
            print("Wybrano pionek nr. ", pionek)

        elif event.type == pygame.KEYDOWN and event.key == pygame.K_2:
            pionek = 2
            print("Wybrano pionek nr. ", pionek)

        elif event.type == pygame.KEYDOWN and event.key == pygame.K_3:
            pionek = 3
            print("Wybrano pionek nr. ", pionek)

        elif event.type == pygame.KEYDOWN and event.key == pygame.K_4:
            pionek = 4
            print("Wybrano pionek nr. ", pionek)

        elif event.type == pygame.QUIT:
            sys.exit(0)
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            sys.exit(0)

        if pionek>=1 and pionek<=4:
           # print("true")
            return True


        else:
           # print("false")
            return False



        print("Wybrano pionek nr. " + pionek)
        return pionek
