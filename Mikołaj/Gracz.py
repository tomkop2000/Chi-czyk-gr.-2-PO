import pygame, sys

import random

class Gracz():

    kolor_paleta = ( (20, 150, 3),(255, 227, 18), (0, 0, 255),(148, 27, 3))  # green yellow blue red

    kolor = (0,0,255)

    ilosc = 0

    pancerz = 1

    suma_oczek = 0

    #pozycja pionka (absolutna) zależna od mapy_pozycji
    pozycja=[[0,0],[0,0],[0,0],[0,0]]

    # pozycje pionków (relatywne)
    pozycjaPionkiBaza = [[0, 0], [48 * 2, 0], [0, 48 * 2], [48 * 2, 48 * 2]]


    # mapa pozycji (absolutna)
    mapa_pozycji = [[72,312],[120,312],[168,312],[216,312],[264,312],[312,264],[312,216],[312,168],[312,120],[312,72],
                    [312,24],[360,24],[408,24],[408,72],[408,120],[408,168],[408,216],[408,264],[456,312],
                    [504,312],[552,312],[600,312],[648,312],[696,312],[696,360],[696,408],[648,408],[600,408],[552,408],
                    [504,408],[456,408],[408,456],[408,504],[408,552],[408,600],[408,648],[408,696],[360,696],[312,696],
                    [312,648],[312,600],[312,552],[312,504],[312,456],[264,408],[216,408],[168,408],[120,408],[72,408],
                    [24,408],[24,360],[24,312]]

    def __init__(self, screen,numer):
        self.screen = screen

        if numer== 1:

            self.pozycja = [[96 + self.pozycjaPionkiBaza[0][0], 96 + self.pozycjaPionkiBaza[0][1]],
                            [96 + self.pozycjaPionkiBaza[1][0], 96 + self.pozycjaPionkiBaza[1][1]],
                            [96 + self.pozycjaPionkiBaza[2][0], 96 + self.pozycjaPionkiBaza[2][1]],
                            [96 + self.pozycjaPionkiBaza[3][0], 96 + self.pozycjaPionkiBaza[3][1]]]

            self.kolor= self.kolor_paleta[0]


        elif numer == 2:
            self.pozycja = [[528 + self.pozycjaPionkiBaza[0][0], 96 + self.pozycjaPionkiBaza[0][1]],
                            [528 + self.pozycjaPionkiBaza[1][0], 96 + self.pozycjaPionkiBaza[1][1]],
                            [528 + self.pozycjaPionkiBaza[2][0], 96 + self.pozycjaPionkiBaza[2][1]],
                            [528 + self.pozycjaPionkiBaza[3][0], 96 + self.pozycjaPionkiBaza[3][1]]]

            self.kolor = self.kolor_paleta[1]

        elif numer == 3:
            self.pozycja = [[528 + self.pozycjaPionkiBaza[0][0], 528 + self.pozycjaPionkiBaza[0][1]],
                            [528 + self.pozycjaPionkiBaza[1][0], 528 + self.pozycjaPionkiBaza[1][1]],
                            [528 + self.pozycjaPionkiBaza[2][0], 528 + self.pozycjaPionkiBaza[2][1]],
                            [528 + self.pozycjaPionkiBaza[3][0], 528 + self.pozycjaPionkiBaza[3][1]]]

            self.kolor = self.kolor_paleta[2]

        elif numer == 4:
            self.pozycja = [[96 + self.pozycjaPionkiBaza[0][0], 528 + self.pozycjaPionkiBaza[0][1]],
                            [96 + self.pozycjaPionkiBaza[1][0], 528 + self.pozycjaPionkiBaza[1][1]],
                            [96 + self.pozycjaPionkiBaza[2][0], 528 + self.pozycjaPionkiBaza[2][1]],
                            [96 + self.pozycjaPionkiBaza[3][0], 528 + self.pozycjaPionkiBaza[3][1]]]

            self.kolor = self.kolor_paleta[3]

        else:
            pass

        print("Gracz nr.", numer, " uruchomiony.")



    def circle(self,i):

        pygame.draw.circle(self.screen, self.kolor, (self.pozycja[i][0],self.pozycja[i][1]), 15 )

    def sprRuch(self, a, b ,c ,d,oczka,pionek):
        for x in range(4):
            if (a.pozycja[pionek-1]+oczka)!=b.pozycja[x]:
                print("nowa pozycja")
                return 1

            if (a.pozycja[pionek-1]+oczka)!=c.pozycja[x]:
                print("nowa pozycja")
                return 1

            if (a.pozycja[pionek-1]+oczka)!=d.pozycja[x]:
                print("nowa pozycja")
                return 1

            else:
                print("stara pozycja")
                return 0

    def sprWygrana(self):
        pass

    def prostyRuch(self):
        self.pozycja = [[self.pozycja[0][0]+1,self.pozycja[0][1]+1],[self.pozycja[1][0]+1,self.pozycja[1][1]+1],[self.pozycja[2][0]+1,self.pozycja[2][1]+1],[self.pozycja[3][0]+1,self.pozycja[3][1]+1]]

    def losowyRuchTest(self,numer,pionek,oczka):
        #pass
        if self.suma_oczek + oczka > 52:
            self.suma_oczek=0

        self.suma_oczek+=oczka


        self.pozycja[pionek-1] = (self.mapa_pozycji[self.suma_oczek-1][0], self.mapa_pozycji[self.suma_oczek-1][1])
        print("suma oczek: ",self.suma_oczek)

    def losowanie(self):
        oczka = random.randint(1, 6)
        return oczka

    def key_check(self):
        while True:
            event = pygame.event.wait()
            if (event.type == pygame.KEYDOWN and (
                    event.key == pygame.K_ESCAPE or event.key == pygame.K_1 or event.key == pygame.K_2 or event.key == pygame.K_3 or event.key == pygame.K_4)) or event.type == pygame.QUIT:
                break
        if event.type == pygame.QUIT:
            print("Wyjście")
            sys.exit(0)
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                print("Wyjście")
                sys.exit(0)
            elif event.key == pygame.K_1:
                print("klawisz_1")
                return 1
            elif event.key == pygame.K_2:
                print("klawisz_2")
                return 2
            elif event.key == pygame.K_3:
                print("klawisz_3")
                return 3
            elif event.key == pygame.K_4:
                print("klawisz_4")
                return 4
            else:
                print("klawisz_inny")
        else:
            print("inna akcja")


class User(Gracz):


    def tick(self):
        self.wyborPionka()

    def draw(self,i):
        self.circle(i)

    def wyborPionka(self):
        pass
