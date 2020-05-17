# coding=utf-8
import pygame, sys
import os
import pygame.locals
import random

from Gracz import User
from Gracz import UserAI

from LUDO_nagrody import krolik
from LUDO_nagrody import swMikolaj
from LUDO_nagrody import kotek

import time

#
# Bardzo przepraszam za bledy ortograficzne
#


pygame.init()  # funkcja ladujaca moduly pyGame'a odpowiedzialne m.in. za dzwiek czy grafike


class Board(object):
    """
    Plansza do gry. Odpowiada za rysowanie okna gry.
    """
    resolution_x = 720
    resolution_y = 720
    okno = pygame.display.set_mode((resolution_x, resolution_y))

    def __init__(self):
        """
        Konstruktor planszy do gry. Przygotowuje okienko gry.
        """

        pygame.display.set_caption('Chinczyk')

        # tu bedzie inicjalzacja obiektów
        print("Ile zywych graczy?")
        ilosc_graczy = self.key_check()

        if ilosc_graczy == 1:
            player_1 = User(self.okno, 1)
            player_2 = UserAI(self.okno, 2)
            player_3 = UserAI(self.okno, 3)
            player_4 = UserAI(self.okno, 4)
            print("wybrano", ilosc_graczy, " zywych graczy")
        elif ilosc_graczy == 2:
            player_1 = User(self.okno, 1)
            player_2 = UserAI(self.okno, 2)
            player_3 = User(self.okno, 3)
            player_4 = UserAI(self.okno, 4)
            print("wybrano", ilosc_graczy, " zywych graczy")
        elif ilosc_graczy == 3:
            player_1 = User(self.okno, 1)
            player_2 = User(self.okno, 2)
            player_3 = User(self.okno, 3)
            player_4 = UserAI(self.okno, 4)
            print("wybrano", ilosc_graczy, " zywych graczy")
        elif ilosc_graczy == 4:
            player_1 = User(self.okno, 1)
            player_2 = User(self.okno, 2)
            player_3 = User(self.okno, 3)
            player_4 = User(self.okno, 4)
            print("wybrano", ilosc_graczy, " zywych graczy")

        elif ilosc_graczy == 5:
            player_1 = UserAI(self.okno, 1)
            player_2 = UserAI(self.okno, 2)
            player_3 = UserAI(self.okno, 3)
            player_4 = UserAI(self.okno, 4)
            print("wybrano 0 zywych graczy")
        else:
            player_1 = User(self.okno, 1)
            player_2 = User(self.okno, 2)
            player_3 = User(self.okno, 3)
            player_4 = User(self.okno, 4)
            print("wybrano domyślne zywych graczy")

        # numery od 1 do 4 to numer gracza
        # cieakwa opcja bylaby tablica obiektów, zaleta wylaby wygoda w urzywaniu niektórych funcji,
        # wada to bardziej skomplikowana implementacja
        # powyzsze 3 zdania zostawiam ale nie sa aktualne prawdopodobnie

        # tutj zrobie deklaracje obiektów:
        # soby od przeszkód:

        # osoby od nagród:

        event = pygame.event.clear()

        counter = 0

        player_1.logika_gry(player_1, player_2, player_3, player_4)
        # player_1.logika_gry(player_1,player_2,player_3,player_4,wilk, krasnoludek, niedzwiedz,krolik,swMikolaj,kotek)

        """
        # petla gry, nie urzywamy systemu tick i delta time bo klatka gry jest zamrazana wiec jest wydajniej i latwiej
        #jest panować nad tym co sie dzieje w kodzie
        while True:


            self.board_draw()

            for i in range(1,5):
                os.system("cls")
                print("Tura gracza nr: ", i)

        #w pythonie nie ma switcha wiec bedzie tu taki twór:
                if i ==1:
                    oczka = player_1.losowanie()
                    print("Kostka wylosowala: ", oczka )#mozna wrzucić wyświetlenie tego tekstu do medoty ale na razie nie
                    print("Podaj nr. pionka, którym chcesz sie ruszyć.")

                    pionek = player_1.wyborPionka()

                    player_1.losowyRuchTest(pionek, oczka)

                    #print(player_1.pozycja)#metoda debugowa

                elif i == 2:
                    oczka = player_2.losowanie()
                    print("Kostka wylosowala: ", oczka)
                    print("Podaj nr. pionka, którym chcesz sie ruszyć.")

                    pionek = player_2.wyborPionka()

                    player_2.losowyRuchTest(pionek, oczka)

                    #print(player_2.pozycja)#metoda debugowa

                elif i == 3:
                    oczka = player_3.losowanie()
                    print("Kostka wylosowala: ", oczka)
                    print("Podaj nr. pionka, którym chcesz sie ruszyć.")

                    pionek = player_3.wyborPionka()

                    player_3.losowyRuchTest(pionek, oczka)

                    #print(player_2.pozycja)#metoda debugowa

                elif i == 4:
                    oczka = player_4.losowanie()
                    print("Kostka wylosowala: ", oczka)
                    print("Podaj nr. pionka, którym chcesz sie ruszyć.")

                    pionek = player_4.wyborPionka()

                    player_4.losowyRuchTest(pionek, oczka)

                    #print(player_2.pozycja)#metoda debugowa

                self.board_draw()
                # narysowanie wszystkich pozycji pionków
                for n in range(4):
                    player_1.draw(n)

                    player_2.draw(n)
                    player_3.draw(n)
                    player_4.draw(n)
                pygame.display.update()




            #update ekranu jak sie wszystko zrobi co ma sie zrobić
            pygame.display.update()


        """

        # self.key_check()

    def board_draw(self):
        pygame.draw.rect(self.okno, (0, 0, 0), (0, 0, 288, 288))
        pygame.draw.rect(self.okno, (0, 150, 0), (1, 1, 286, 286))
        pygame.draw.rect(self.okno, (0, 0, 0), (49, 49, 190, 190))
        pygame.draw.rect(self.okno, (255, 255, 255), (50, 50, 188, 188))

        pygame.draw.ellipse(self.okno, (0, 150, 0), (52, 52, 90, 90))
        pygame.draw.ellipse(self.okno, (0, 150, 0), (144, 52, 90, 90))
        pygame.draw.ellipse(self.okno, (0, 150, 0), (52, 144, 90, 90))
        pygame.draw.ellipse(self.okno, (0, 150, 0), (144, 144, 90, 90))

        pygame.draw.rect(self.okno, (0, 0, 0), (288, 0, 144, 144))

        pygame.draw.rect(self.okno, (0, 0, 0), (431, 0, 288, 288))
        pygame.draw.rect(self.okno, (255, 0, 0), (432, 1, 286, 286))
        pygame.draw.rect(self.okno, (0, 0, 0), (480, 49, 190, 190))
        pygame.draw.rect(self.okno, (255, 255, 255), (481, 50, 188, 188))

        pygame.draw.ellipse(self.okno, (255, 0, 0), (483, 52, 90, 90))
        pygame.draw.ellipse(self.okno, (255, 0, 0), (575, 52, 90, 90))
        pygame.draw.ellipse(self.okno, (255, 0, 0), (483, 144, 90, 90))
        pygame.draw.ellipse(self.okno, (255, 0, 0), (575, 144, 90, 90))

        pygame.draw.rect(self.okno, (255, 255, 255), (288, 1, 47, 47))
        pygame.draw.rect(self.okno, (255, 255, 255), (336, 1, 47, 47))  # 1
        pygame.draw.rect(self.okno, (255, 255, 255), (384, 1, 47, 47))
        pygame.draw.rect(self.okno, (255, 255, 255), (288, 49, 47, 47))
        pygame.draw.rect(self.okno, (255, 0, 0), (336, 49, 47, 47))  # 2
        pygame.draw.rect(self.okno, (255, 0, 0), (384, 49, 47, 47))
        pygame.draw.rect(self.okno, (255, 255, 255), (288, 97, 47, 47))
        pygame.draw.rect(self.okno, (255, 0, 0), (336, 97, 47, 47))  # 3
        pygame.draw.rect(self.okno, (255, 255, 255), (384, 97, 47, 47))
        pygame.draw.rect(self.okno, (255, 255, 255), (288, 145, 47, 47))
        pygame.draw.rect(self.okno, (255, 0, 0), (336, 145, 47, 47))  # 4
        pygame.draw.rect(self.okno, (255, 255, 255), (384, 145, 47, 47))
        pygame.draw.rect(self.okno, (255, 255, 255), (288, 193, 47, 47))
        pygame.draw.rect(self.okno, (255, 0, 0), (336, 193, 47, 47))  # 5
        pygame.draw.rect(self.okno, (255, 255, 255), (384, 193, 47, 47))
        pygame.draw.rect(self.okno, (255, 255, 255), (288, 241, 47, 47))
        pygame.draw.rect(self.okno, (255, 0, 0), (336, 241, 47, 47))  # 6
        pygame.draw.rect(self.okno, (255, 255, 255), (384, 241, 47, 47))

        pygame.draw.rect(self.okno, (0, 0, 0), (0, 288, 144, 144))

        pygame.draw.rect(self.okno, (255, 255, 255), (1, 288, 47, 47))  ##########
        pygame.draw.rect(self.okno, (0, 150, 0), (49, 288, 47, 47))
        pygame.draw.rect(self.okno, (255, 255, 255), (97, 288, 47, 47))
        pygame.draw.rect(self.okno, (255, 255, 255), (145, 288, 47, 47))  # lewa
        pygame.draw.rect(self.okno, (255, 255, 255), (193, 288, 47, 47))
        pygame.draw.rect(self.okno, (255, 255, 255), (241, 288, 47, 47))  ##########  1
        pygame.draw.rect(self.okno, (255, 255, 255), (431, 288, 47, 47))
        pygame.draw.rect(self.okno, (255, 255, 255), (479, 288, 47, 47))
        pygame.draw.rect(self.okno, (255, 255, 255), (527, 288, 47, 47))  # prawa
        pygame.draw.rect(self.okno, (255, 255, 255), (575, 288, 47, 47))
        pygame.draw.rect(self.okno, (255, 255, 255), (623, 288, 47, 47))
        pygame.draw.rect(self.okno, (255, 255, 255), (671, 288, 47, 47))  ##########

        pygame.draw.rect(self.okno, (255, 255, 255), (1, 336, 47, 47))  ##########
        pygame.draw.rect(self.okno, (0, 150, 0), (49, 336, 47, 47))
        pygame.draw.rect(self.okno, (0, 150, 0), (97, 336, 47, 47))
        pygame.draw.rect(self.okno, (0, 150, 0), (145, 336, 47, 47))  # lewa
        pygame.draw.rect(self.okno, (0, 150, 0), (193, 336, 47, 47))
        pygame.draw.rect(self.okno, (0, 150, 0), (241, 336, 47, 47))  ##########  2
        pygame.draw.rect(self.okno, (0, 0, 255), (431, 336, 47, 47))
        pygame.draw.rect(self.okno, (0, 0, 255), (479, 336, 47, 47))
        pygame.draw.rect(self.okno, (0, 0, 255), (527, 336, 47, 47))  # prawa
        pygame.draw.rect(self.okno, (0, 0, 255), (575, 336, 47, 47))
        pygame.draw.rect(self.okno, (0, 0, 255), (623, 336, 47, 47))
        pygame.draw.rect(self.okno, (255, 255, 255), (671, 336, 47, 47))  ##########

        pygame.draw.rect(self.okno, (255, 255, 255), (1, 384, 47, 47))  ##########
        pygame.draw.rect(self.okno, (255, 255, 255), (49, 384, 47, 47))
        pygame.draw.rect(self.okno, (255, 255, 255), (97, 384, 47, 47))
        pygame.draw.rect(self.okno, (255, 255, 255), (145, 384, 47, 47))  # lewa
        pygame.draw.rect(self.okno, (255, 255, 255), (193, 384, 47, 47))
        pygame.draw.rect(self.okno, (255, 255, 255), (241, 384, 47, 47))  ##########  3
        pygame.draw.rect(self.okno, (255, 255, 255), (431, 384, 47, 47))
        pygame.draw.rect(self.okno, (255, 255, 255), (479, 384, 47, 47))
        pygame.draw.rect(self.okno, (255, 255, 255), (527, 384, 47, 47))  # prawa
        pygame.draw.rect(self.okno, (255, 255, 255), (575, 384, 47, 47))
        pygame.draw.rect(self.okno, (0, 0, 255), (623, 384, 47, 49))
        pygame.draw.rect(self.okno, (255, 255, 255), (671, 384, 47, 47))  ##########

        pygame.draw.rect(self.okno, (0, 0, 0), (0, 431, 288, 288))
        pygame.draw.rect(self.okno, (255, 255, 0), (1, 432, 286, 286))
        pygame.draw.rect(self.okno, (0, 0, 0), (49, 480, 190, 190))
        pygame.draw.rect(self.okno, (255, 255, 255), (50, 481, 188, 188))

        pygame.draw.ellipse(self.okno, (255, 255, 0), (52, 483, 90, 90))
        pygame.draw.ellipse(self.okno, (255, 255, 0), (144, 483, 90, 90))
        pygame.draw.ellipse(self.okno, (255, 255, 0), (52, 575, 90, 90))
        pygame.draw.ellipse(self.okno, (255, 255, 0), (144, 575, 90, 90))

        pygame.draw.rect(self.okno, (0, 0, 0), (431, 431, 288, 288))
        pygame.draw.rect(self.okno, (0, 0, 255), (432, 432, 286, 286))
        pygame.draw.rect(self.okno, (0, 0, 0), (480, 480, 190, 190))
        pygame.draw.rect(self.okno, (255, 255, 255), (481, 481, 188, 188))

        pygame.draw.ellipse(self.okno, (0, 0, 255), (483, 483, 90, 90))
        pygame.draw.ellipse(self.okno, (0, 0, 255), (575, 483, 90, 90))
        pygame.draw.ellipse(self.okno, (0, 0, 255), (483, 575, 90, 90))
        pygame.draw.ellipse(self.okno, (0, 0, 255), (575, 575, 90, 90))

        pygame.draw.rect(self.okno, (255, 255, 255), (288, 431, 47, 47))
        pygame.draw.rect(self.okno, (255, 255, 0), (336, 431, 47, 47))  # 1
        pygame.draw.rect(self.okno, (255, 255, 255), (384, 431, 47, 47))
        pygame.draw.rect(self.okno, (255, 255, 255), (288, 479, 47, 47))
        pygame.draw.rect(self.okno, (255, 255, 0), (336, 479, 47, 47))  # 2
        pygame.draw.rect(self.okno, (255, 255, 255), (384, 479, 47, 47))
        pygame.draw.rect(self.okno, (255, 255, 255), (288, 527, 47, 47))
        pygame.draw.rect(self.okno, (255, 255, 0), (336, 527, 47, 47))  # 3
        pygame.draw.rect(self.okno, (255, 255, 255), (384, 527, 47, 47))
        pygame.draw.rect(self.okno, (255, 255, 255), (288, 575, 47, 47))
        pygame.draw.rect(self.okno, (255, 255, 0), (336, 575, 47, 47))  # 4
        pygame.draw.rect(self.okno, (255, 255, 255), (384, 575, 47, 47))
        pygame.draw.rect(self.okno, (255, 255, 0), (288, 623, 47, 47))
        pygame.draw.rect(self.okno, (255, 255, 0), (336, 623, 47, 47))  # 5
        pygame.draw.rect(self.okno, (255, 255, 255), (384, 623, 47, 47))
        pygame.draw.rect(self.okno, (255, 255, 255), (288, 671, 47, 47))
        pygame.draw.rect(self.okno, (255, 255, 255), (336, 671, 47, 47))  # 6
        pygame.draw.rect(self.okno, (255, 255, 255), (384, 671, 47, 47))

        pygame.draw.rect(self.okno, (0, 0, 0), (288, 288, 144, 144))

        pygame.draw.polygon(self.okno, (255, 255, 0), ((287, 430), (429, 430), (358, 358)))
        pygame.draw.polygon(self.okno, (0, 150, 0), ((289, 430), (289, 288), (358, 358)))
        pygame.draw.polygon(self.okno, (255, 0, 0), ((288, 289), (431, 289), (358, 358)))
        pygame.draw.polygon(self.okno, (0, 0, 255), ((430, 288), (430, 430), (359, 358)))

        pygame.draw.line(self.okno, (150, 0, 150), (389, 6), (424, 41), 2)
        pygame.draw.line(self.okno, (150, 0, 150), (389, 41), (424, 6), 2)
        pygame.draw.line(self.okno, (150, 0, 150), (293, 151), (327, 185), 2)
        pygame.draw.line(self.okno, (150, 0, 150), (293, 185), (327, 151), 2)
        pygame.draw.line(self.okno, (150, 0, 150), (197, 292), (235, 330), 2)
        pygame.draw.line(self.okno, (150, 0, 150), (197, 330), (235, 292), 2)
        pygame.draw.line(self.okno, (150, 0, 150), (437, 293), (472, 328), 2)
        pygame.draw.line(self.okno, (150, 0, 150), (437, 329), (472, 294), 2)
        pygame.draw.line(self.okno, (150, 0, 150), (151, 389), (186, 425), 2)
        pygame.draw.line(self.okno, (150, 0, 150), (152, 425), (186, 389), 2)
        pygame.draw.line(self.okno, (150, 0, 150), (580, 391), (616, 425), 2)
        pygame.draw.line(self.okno, (150, 0, 150), (580, 425), (616, 391), 2)
        pygame.draw.line(self.okno, (150, 0, 150), (389, 485), (424, 520), 2)
        pygame.draw.line(self.okno, (150, 0, 150), (389, 520), (424, 485), 2)
        pygame.draw.line(self.okno, (150, 0, 150), (390, 676), (424, 712), 2)
        pygame.draw.line(self.okno, (150, 0, 150), (390, 712), (424, 676), 2)
        pygame.draw.line(self.okno, (150, 0, 150), (293, 533), (329, 568), 2)
        pygame.draw.line(self.okno, (150, 0, 150), (293, 568), (329, 533), 2)

        pygame.draw.circle(self.okno, (250, 150, 100), (407, 168), 15, 2)
        pygame.draw.circle(self.okno, (250, 150, 100), (311, 264), 15, 2)
        pygame.draw.circle(self.okno, (250, 150, 100), (264, 311), 15, 2)
        pygame.draw.circle(self.okno, (250, 150, 100), (550, 311), 15, 2)
        pygame.draw.circle(self.okno, (250, 150, 100), (454, 407), 15, 2)
        pygame.draw.circle(self.okno, (250, 150, 100), (311, 502), 15, 2)
        pygame.draw.circle(self.okno, (250, 150, 100), (311, 694), 15, 2)

        # print("Plansza narysowana")
        """
        for x in range(15 + 1):
            pygame.draw.line(self.okno, (89, 89, 89),(48*x, 0),(48*x,720), 5)
            pygame.draw.line(self.okno,  (89, 89, 89),(0, 48*x),(720,48*x), 5)
        """

        return 1

    def losowanie(self):
        oczka = random.randint(1, 6)
        print("Kostka: ", oczka)
        return oczka

    # funkcja do sprawdzania kliknietego przycisku (funkcja dziala dopuki nie "kliknie" sie 1, 2, 3, 4, ESC lub przycisku zamkniecia
    # funkcja "zamraza rysowanie klatki zdzieki czemu "oszczedzamy" zasoby
    def key_check(self):
        while True:
            event = pygame.event.wait()
            if (event.type == pygame.KEYDOWN and (
                    event.key == pygame.K_ESCAPE or event.key == pygame.K_1 or event.key == pygame.K_2 or event.key == pygame.K_3 or event.key == pygame.K_4 or event.key == pygame.K_5)) or event.type == pygame.QUIT:
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
            # tylko do debugowania
            elif event.key == pygame.K_5:
                print("klawisz_5")
                return 5
            else:
                print("klawisz_inny")
        else:
            print("inna akcja")


if __name__ == "__main__":
    board = Board()
