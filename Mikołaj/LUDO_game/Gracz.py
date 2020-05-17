import pygame, sys, os

import random

import time

from LUDO_nagrody import krolik
from LUDO_nagrody import swMikolaj
from LUDO_nagrody import kotek

from LUDO_pytania import wilk
from LUDO_pytania import krasnoludek
from LUDO_pytania import niedzwiedz


class Gracz():
    # palety kolorow:
    kolor_paleta = ((20, 250, 3), (148, 27, 3), (0, 100, 255), (255, 227, 18))  # 1_green 2_red  3_blue 4_yellow

    kolor = (0, 0, 255)

    ilosc = 0

    pancerz = 1

    suma_oczek = [0, 0, 0, 0]

    numer = 0  # numer gracza

    # 1 - w bazie
    # 2 - w polu gry
    # 3 - w  chodniku do domku
    # 4 - w domku

    pionki_stan = [1, 1, 1, 1]

    mapa_pozycji_domek = [51, 12, 25, 38]  # to sa wspolrzedne na jakiej zaczynaja sie domki

    mapa_pozycji_domek_chodnik = [53, 59, 65, 71]  # to sa wspolrzedne (suma_pionek) na jakiej juz sa pierwsze wspolrzedne domkow

    domek_wejscie = 51

    domek_wejscie_chodnik = 53

    pozycje_startowe = (0, 13, 26, 39)

    # pozycja pionka (absolutna) zalezna od mapy_pozycji
    pozycja = [[0, 0], [0, 0], [0, 0], [0, 0]]

    # pozycje pionkow w bazie (relatywne)
    pozycjaPionkiBaza = [[0, 0], [48 * 2, 0], [0, 48 * 2], [48 * 2, 48 * 2]]

    # mapa pozycji (absolutna) #4 ostanie linijki to rozpisane pozycje pol w domkach
    mapa_pozycji = [[72, 312], [120, 312], [168, 312], [216, 312], [264, 312], [312, 264], [312, 216], [312, 168], [312, 120], [312, 72], [312, 24], [360, 24], [408, 24], [408, 72], [408, 120],
                    [408, 168], [408, 216], [408, 264], [456, 312], [504, 312], [552, 312], [600, 312], [648, 312], [696, 312], [696, 360], [696, 408], [648, 408], [600, 408], [552, 408], [504, 408],
                    [456, 408], [408, 456], [408, 504], [408, 552], [408, 600], [408, 648], [408, 696], [360, 696], [312, 696], [312, 648], [312, 600], [312, 552], [312, 504], [312, 456], [264, 408],
                    [216, 408], [168, 408], [120, 408], [72, 408], [24, 408], [24, 360], [24, 312], [72, 360], [120, 360], [168, 360], [216, 360], [264, 360], [312, 360], [360, 72], [360, 120],
                    [360, 168], [360, 216], [360, 264], [360, 312], [648, 360], [600, 360], [552, 360], [504, 360], [456, 360], [408, 360], [360, 648], [360, 600], [360, 552], [360, 504], [360, 456],
                    [360, 408]]

    # konstruktor ktory w zalezności od numeru (gracza) przypozadkuje( wiem ze z bledem napisane) odpowiedni kolor i bazowa pozycje
    def __init__(self, screen, numer):
        self.screen = screen
        self.okno = screen

        if numer == 1:

            self.pozycja = [[96 + self.pozycjaPionkiBaza[0][0], 96 + self.pozycjaPionkiBaza[0][1]], [96 + self.pozycjaPionkiBaza[1][0], 96 + self.pozycjaPionkiBaza[1][1]],
                            [96 + self.pozycjaPionkiBaza[2][0], 96 + self.pozycjaPionkiBaza[2][1]], [96 + self.pozycjaPionkiBaza[3][0], 96 + self.pozycjaPionkiBaza[3][1]]]

            self.kolor = self.kolor_paleta[0]

            self.suma_oczek = [0, 0, 0, 0]

            self.numer = 1  # moglem dać na ońcu tylko numer = self.numer ale nie chcialem

            self.domek_wejscie = self.mapa_pozycji_domek[0]

            self.domek_wejscie_chodnik = self.mapa_pozycji_domek_chodnik[0]



        elif numer == 2:
            self.pozycja = [[528 + self.pozycjaPionkiBaza[0][0], 96 + self.pozycjaPionkiBaza[0][1]], [528 + self.pozycjaPionkiBaza[1][0], 96 + self.pozycjaPionkiBaza[1][1]],
                            [528 + self.pozycjaPionkiBaza[2][0], 96 + self.pozycjaPionkiBaza[2][1]], [528 + self.pozycjaPionkiBaza[3][0], 96 + self.pozycjaPionkiBaza[3][1]]]

            self.kolor = self.kolor_paleta[1]

            self.suma_oczek = [13, 13, 13, 13]

            self.numer = 2

            self.domek_wejscie = self.mapa_pozycji_domek[1]

            self.domek_wejscie_chodnik = self.mapa_pozycji_domek_chodnik[1]

        elif numer == 3:
            self.pozycja = [[528 + self.pozycjaPionkiBaza[0][0], 528 + self.pozycjaPionkiBaza[0][1]], [528 + self.pozycjaPionkiBaza[1][0], 528 + self.pozycjaPionkiBaza[1][1]],
                            [528 + self.pozycjaPionkiBaza[2][0], 528 + self.pozycjaPionkiBaza[2][1]], [528 + self.pozycjaPionkiBaza[3][0], 528 + self.pozycjaPionkiBaza[3][1]]]

            self.kolor = self.kolor_paleta[2]

            self.suma_oczek = [26, 26, 26, 26]

            self.numer = 3

            self.domek_wejscie = self.mapa_pozycji_domek[2]

            self.domek_wejscie_chodnik = self.mapa_pozycji_domek_chodnik[2]

        elif numer == 4:
            self.pozycja = [[96 + self.pozycjaPionkiBaza[0][0], 528 + self.pozycjaPionkiBaza[0][1]], [96 + self.pozycjaPionkiBaza[1][0], 528 + self.pozycjaPionkiBaza[1][1]],
                            [96 + self.pozycjaPionkiBaza[2][0], 528 + self.pozycjaPionkiBaza[2][1]], [96 + self.pozycjaPionkiBaza[3][0], 528 + self.pozycjaPionkiBaza[3][1]]]

            self.kolor = self.kolor_paleta[3]

            self.suma_oczek = [39, 39, 39, 39]

            self.numer = 4

            self.domek_wejscie = self.mapa_pozycji_domek[3]

            self.domek_wejscie_chodnik = self.mapa_pozycji_domek_chodnik[3]

        else:
            pass

        self.pionki_stan = [1, 1, 1, 1]

        self.pozycja_poczatkowa = self.pozycja

        self.suma_oczek_poczatkowa = self.suma_oczek

        print("Gracz nr.", self.numer, " uruchomiony.")

    def circle(self, i):

        pygame.draw.circle(self.screen, self.kolor, (self.pozycja[i][0], self.pozycja[i][1]), 15)

    # tymczasowa funkcja na ruch
    def losowyRuchTest(self, pionek, oczka, player_1, player_2, player_3, player_4):
        # pass

        if self.pionki_stan[pionek - 1] == 1:
            self.pionki_stan[pionek - 1] = 2

        if self.pionki_stan[pionek - 1] == 2:

            if (self.suma_oczek[pionek - 1] + oczka > 52) and self.kolor != self.kolor_paleta[0]:  # to dziala dla wszystkich oprocz zielonych (gracza nr.1)
                oczka = oczka - (52 - self.suma_oczek[pionek - 1])
                self.suma_oczek[pionek - 1] = 0

                self.suma_oczek[pionek - 1] += oczka

            elif (self.suma_oczek[pionek - 1] + oczka > 51) and self.kolor == self.kolor_paleta[0]:  # to dziala tylko dla zielonych (gracza nr.1))
                oczka = oczka - (51 - self.suma_oczek[pionek - 1])
                self.suma_oczek[pionek - 1] = 51 + oczka
                self.pionki_stan[pionek - 1] = 3



            elif self.suma_oczek[pionek - 1] + int(oczka) == self.domek_wejscie:
                pass

            # to musi oznaczać tylko ze jesteśmy kilka pol przed wejściem do domku
            elif ((self.suma_oczek[pionek - 1] + oczka) > self.domek_wejscie) and (self.suma_oczek[pionek - 1] < self.domek_wejscie) and self.kolor != self.kolor_paleta[0]:

                oczka = oczka - (self.domek_wejscie - self.suma_oczek[pionek - 1])
                self.suma_oczek[pionek - 1] = self.domek_wejscie_chodnik - 1 + oczka  # + oczka ,powinno być ale ...

                self.pionki_stan[pionek - 1] = 3



            else:
                self.suma_oczek[pionek - 1] += oczka


        elif self.pionki_stan[pionek - 1] == 3:
            self.suma_oczek[pionek - 1] += oczka

            # elif self.suma_oczek[pionek - 1] < (self.domek_wejscie + 6):  # self.suma_oczek[pionek - 1] += oczka

        if self.suma_oczek[pionek - 1] > (self.domek_wejscie_chodnik + 5):
            self.suma_oczek[pionek - 1] = (self.domek_wejscie_chodnik + 5)
        elif self.suma_oczek[pionek - 1] == (self.domek_wejscie_chodnik + 5):
            self.suma_oczek[pionek - 1] = (self.domek_wejscie_chodnik + 5)

        self.pozycja[pionek - 1] = (self.mapa_pozycji[self.suma_oczek[pionek - 1] - 1][0], self.mapa_pozycji[self.suma_oczek[pionek - 1] - 1][1])
        print("suma oczek: ", self.suma_oczek[pionek - 1])

        if self.kolor == self.kolor_paleta[0]:
            czyja_kolej = 1
        elif self.kolor == self.kolor_paleta[1]:
            czyja_kolej = 2
        elif self.kolor == self.kolor_paleta[2]:
            czyja_kolej = 3
        elif self.kolor == self.kolor_paleta[3]:
            czyja_kolej = 4

        player_1.bicie(player_1, player_2, player_3, player_4, czyja_kolej, pionek)

        if self.pionki_stan[pionek - 1] == 3:
            if self.suma_oczek[pionek - 1] == (self.domek_wejscie_chodnik + 5):
                self.pionki_stan[pionek - 1] = 4

        self.circle(pionek - 1)

        self.board_draw()
        for i in range(4):
            player_1.draw(i)
            player_2.draw(i)
            player_3.draw(i)
            player_4.draw(i)
        pygame.display.update()

        if (self.suma_oczek[pionek - 1] == 5 or self.suma_oczek[pionek - 1] == 6 or self.suma_oczek[pionek - 1] == 16 or self.suma_oczek[pionek - 1] == 21 or self.suma_oczek[pionek - 1] == 31 or
                self.suma_oczek[pionek - 1] == 39 or self.suma_oczek[pionek - 1] == 43):
            if isinstance(self, UserAI):
                print("Bot nie bedzie mial nagrody ani przeszkody")
            elif isinstance(self, User):
                self.nagroda(pionek)

        if (self.suma_oczek[pionek - 1] == 4 or self.suma_oczek[pionek - 1] == 8 or self.suma_oczek[pionek - 1] == 13 or self.suma_oczek[pionek - 1] == 19 or self.suma_oczek[pionek - 1] == 28 or
                self.suma_oczek[pionek - 1] == 33 or self.suma_oczek[pionek - 1] == 37 or self.suma_oczek[pionek - 1] == 42 or self.suma_oczek[pionek - 1] == 47):
            if isinstance(self, UserAI):
                print("Bot nie bedzie mial nagrody ani przeszkody")
            elif isinstance(self, User):
                self.przeszkoda(pionek)

        self.circle(pionek - 1)

        if self.pionki_stan == [4, 4, 4, 4]:

            """
            self.board_draw()
            self.circle(0)
            self.circle(1)
            self.circle(2)
            self.circle(3)
            """

            os.system("cls")
            print("Wygranko, wygranko wygranko, gratulacje...")

            if self.kolor == self.kolor_paleta[0]:
                print("gracz nr 1")
            elif self.kolor == self.kolor_paleta[1]:
                print("gracz nr 2")
            elif self.kolor == self.kolor_paleta[2]:
                print("gracz nr 3")
            elif self.kolor == self.kolor_paleta[3]:
                print("gracz nr 4")

            while True:
                event = pygame.event.wait()
                if (event.type == pygame.KEYDOWN and (event.key == pygame.K_ESCAPE)) or event.type == pygame.QUIT:
                    break
            if event.type == pygame.QUIT:
                print("Wyjście")
                os.system("cls")
                sys.exit(0)
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    print("Wyjście")
                    os.system("cls")
                    sys.exit(0)

    # metoda losujaca jak koska, (w przyszlości wyświetli liczbe oczek)
    def losowanie(self):
        oczka = random.randint(1, 6)
        return oczka

    # bedzie urzywane w losowyRuchTest bo tak bedzie najwygodniej
    # samo wyzwolenie tej cześci bedzie w losowyRuchTest
    def nagroda(self, pionek):
        obiekt = random.randint(1, 3)
        nagroda = 0

        if obiekt == 1:
            nagroda = krolik.nagroda_krolika()
        elif obiekt == 2:
            nagroda = swMikolaj.nagroda_swMikolaja()
        elif obiekt == 3:
            nagroda = kotek.nagroda_kota()

        # rozpiska nagrod:
        # 1 +1 pole
        # 2 +2 pola
        # 3 +3 pola
        # 4 +4 pola
        # 5 +5 pol
        # 6 +6 pol
        # 7 pionek z bazy wychodzi #to musze jeszcze bardzije przemyśleć ale powinno sie latwo dać
        # 8 dodatkowy rzut kostka do tego pionka co sie nim wlaśnie ruszyleś

        if nagroda >= 1 and nagroda <= 6:
            self.losowyRuchTest(pionek, nagroda)

        elif nagroda == 7:
            if self.pionki_stan[0] == 1:
                self.losowyRuchTest(1, 1)
            elif self.pionki_stan[1] == 1:
                self.losowyRuchTest(2, 1)
            elif self.pionki_stan[2] == 1:
                self.losowyRuchTest(3, 1)
            elif self.pionki_stan[3] == 1:
                self.losowyRuchTest(4, 1)

        elif nagroda == 8:
            self.losowyRuchTest(pionek, self.losowanie())

        """
        elif nagroda == 2:
            pass
        elif nagroda == 3 :
            pass
        elif nagroda == 4 :
            pass
        elif nagroda == 5 :
            pass
        elif nagroda == 6 :
            pass
        """

    def przeszkoda(self, pionek):
        obiekt = random.randint(1, 3)
        przeszkoda = 0

        if obiekt == 1:
            przeszkoda = wilk.pytanie_wilka()
        elif obiekt == 2:
            przeszkoda = krasnoludek.pytanie_krasnala()
        elif obiekt == 3:
            przeszkoda = niedzwiedz.pytanie_niedzwiedzia()

        if przeszkoda == 1:
            print("Przezyleś spotkanie, ufff....")
        elif przeszkoda == 0:
            self.pozycja[pionek - 1] = self.pozycja_poczatkowa[pionek - 1]
            self.pionki_stan[pionek - 1] = 1
            self.suma_oczek[pionek - 1] = self.suma_oczek_poczatkowa[pionek - 1]
            print("Polegleś!!!!")

    # takie sa poczatkowe zasady tej gry
    def gra_poczatkowe_losowanie(self, p_1, p_2, p_3, p_4):

        oczka = 0
        numer = 0

        while True:
            os.system("cls")
            print("Zaczyna gracz nr: 1")
            oczka = p_1.losowanie()
            if oczka == 6:
                numer = 1
                print("Kostka wylosowala: ", oczka)
                break

            os.system("cls")
            print("Zaczyna gracz nr: 2")
            oczka = p_2.losowanie()
            if oczka == 6:
                numer = 2
                print("Kostka wylosowala: ", oczka)
                break

            os.system("cls")
            print("Zaczyna gracz nr: 3")
            oczka = p_3.losowanie()
            if oczka == 6:
                numer = 3
                print("Kostka wylosowala: ", oczka)
                break

            os.system("cls")
            print("Zaczyna gracz nr: 4")
            oczka = p_4.losowanie()
            if oczka == 6:
                numer = 4
                print("Kostka wylosowala: ", oczka)
                break

            # os.system("cls")

        return numer

    def gra_poczatkowa(self, p_1, p_2, p_3, p_4):

        first = self.gra_poczatkowe_losowanie(p_1, p_2, p_3, p_4)

        # tutaj wybrany pionek idzie na pole startu
        print("Tura gracza nr: ", first)
        if first == 1:
            print("Wybierz pionek z bazy: ")
            pionek = p_1.wyborPionka()
            p_1.losowyRuchTest(pionek, 1, p_1, p_2, p_3, p_4)
            print("Przesunieto pionek nr. ", pionek, " na pole startowe ")
        elif first == 2:
            print("Wybierz pionek z bazy: ")
            pionek = p_2.wyborPionka()
            p_2.losowyRuchTest(pionek, 1, p_1, p_2, p_3, p_4)
            print("Przesunieto pionek nr. ", pionek, " na pole startowe ")
        elif first == 3:
            print("Wybierz pionek z bazy: ")
            pionek = p_3.wyborPionka()
            p_3.losowyRuchTest(pionek, 1, p_1, p_2, p_3, p_4)
            print("Przesunieto pionek nr. ", pionek, " na pole startowe ")
        elif first == 4:
            print("Wybierz pionek z bazy: ")
            pionek = p_4.wyborPionka()
            p_4.losowyRuchTest(pionek, 1, p_1, p_2, p_3, p_4)
            print("Przesunieto pionek nr. ", pionek, " na pole startowe ")
        else:
            pass

        return first

    def logika_gry(self, player_1, player_2, player_3, player_4):
        # poczatkowe rozrysowanie
        self.board_draw()
        for i in range(4):
            player_1.draw(i)
            player_2.draw(i)
            player_3.draw(i)
            player_4.draw(i)

        pygame.display.update()

        # to tez wcisne w klase Gracz

        kolejka = 1

        kolejka = player_1.gra_poczatkowa(player_1, player_2, player_3, player_4)

        self.board_draw()
        for i in range(4):
            player_1.draw(i)
            player_2.draw(i)
            player_3.draw(i)
            player_4.draw(i)

        pygame.display.update()

        licznik = 0

        # print("wejscie do petli glownej gry")
        while True:
            licznik = 0

            if kolejka == 5:
                kolejka = 1

            print("Trwa tura gracza nr. ", kolejka)

            ###########################################################
            if kolejka == 1:
                print("pionki stan = ", player_1.pionki_stan)
                print("pionki syma_oczek = ", player_1.suma_oczek)
                print("pionki wejscie_chodnik = ", player_1.domek_wejscie_chodnik)
                print("pionki wejscie_domek = ", player_1.domek_wejscie)
                if player_1.pionki_stan == [1, 1, 1, 1]:
                    max_licznik = 3

                elif (player_1.pionki_stan[0] == 2 or player_1.pionki_stan[1] == 2 or player_1.pionki_stan[2] == 2 or player_1.pionki_stan[3] == 2):
                    max_licznik = 1


            elif kolejka == 2:
                print("pionki stan = ", player_2.pionki_stan)
                print("pionki syma_oczek = ", player_2.suma_oczek)
                print("pionki wejscie_chodnik = ", player_2.domek_wejscie_chodnik)
                print("pionki wejscie_domek = ", player_2.domek_wejscie)
                if player_2.pionki_stan == [1, 1, 1, 1]:
                    max_licznik = 3

                elif (player_2.pionki_stan[0] == 2 or player_2.pionki_stan[1] == 2 or player_2.pionki_stan[2] == 2 or player_2.pionki_stan[3] == 2):
                    max_licznik = 1


            elif kolejka == 3:
                print("pionki stan = ", player_3.pionki_stan)
                print("pionki syma_oczek = ", player_3.suma_oczek)
                print("pionki wejscie_chodnik = ", player_3.domek_wejscie_chodnik)
                print("pionki wejscie_domek = ", player_3.domek_wejscie)
                if player_3.pionki_stan == [1, 1, 1, 1]:
                    max_licznik = 3

                elif (player_3.pionki_stan[0] == 2 or player_3.pionki_stan[1] == 2 or player_3.pionki_stan[2] == 2 or player_3.pionki_stan[3] == 2):
                    max_licznik = 1

            elif kolejka == 4:
                print("pionki stan = ", player_4.pionki_stan)
                print("pionki syma_oczek = ", player_4.suma_oczek)
                print("pionki wejscie_chodnik = ", player_4.domek_wejscie_chodnik)
                print("pionki wejscie_domek = ", player_4.domek_wejscie)
                if player_4.pionki_stan == [1, 1, 1, 1]:
                    max_licznik = 3

                elif (player_4.pionki_stan[0] == 2 or player_4.pionki_stan[1] == 2 or player_4.pionki_stan[2] == 2 or player_4.pionki_stan[3] == 2):
                    max_licznik = 1

            # print("stan max_licznik = ", max_licznik)

            ###########################################################
            # print("wejscie do petli gracza")
            while True:

                # print("1licznik = ", licznik)
                if licznik == max_licznik:
                    # print("BREAK zadzialal")
                    break

                oczka = player_1.losowanie()  # to tylko metoda nie robiaca nic z wartościami obiektow

                print("Kostka wylosowala: ", oczka)

                if oczka == 6:

                    # print("1oczka = ", oczka)

                    ###########################################################

                    # print("1kolejka = ", kolejka)

                    if kolejka == 1:

                        while True:
                            pionek = player_1.wyborPionka()  # to tylko metoda nie robiaca nic z wartościami obiektow
                            if player_1.pionki_stan[pionek - 1] == 1:
                                player_1.losowyRuchTest(pionek, 1, player_1, player_2, player_3, player_4)  # tu daje pionek na start

                                break
                            elif player_1.pionki_stan[pionek - 1] == 2:
                                player_1.losowyRuchTest(pionek, oczka, player_1, player_2, player_3, player_4)  # tu sie ruszam pionkiem
                                break

                            elif player_1.pionki_stan[pionek - 1] == 3:
                                """
                                if (player_1.suma_oczek[pionek - 1] + oczka) > (player_1.domek_wejscie_chodnik + 5):
                                    print("Niedobry ruch")
                                """
                                player_1.losowyRuchTest(pionek, oczka, player_1, player_2, player_3, player_4)  # tu sie ruszam pionkiem
                                break



                    elif kolejka == 2:

                        while True:
                            pionek = player_2.wyborPionka()  # to tylko metoda nie robiaca nic z wartościami obiektow
                            if player_2.pionki_stan[pionek - 1] == 1:
                                player_2.losowyRuchTest(pionek, 1, player_1, player_2, player_3, player_4)  # tu daje pionek na start
                                break
                            elif player_2.pionki_stan[pionek - 1] == 2:
                                player_2.losowyRuchTest(pionek, oczka, player_1, player_2, player_3, player_4)  # tu sie ruszam pionkiem
                                break

                            elif player_2.pionki_stan[pionek - 1] == 3:
                                player_2.losowyRuchTest(pionek, oczka, player_1, player_2, player_3, player_4)  # tu sie ruszam pionkiem
                                break
                                """
                                if (player_2.suma_oczek[pionek - 1] + oczka) > (player_2.domek_wejscie_chodnik + 5):
                                    print("Niedobry ruch")
                                """


                    elif kolejka == 3:
                        while True:
                            pionek = player_3.wyborPionka()  # to tylko metoda nie robiaca nic z wartościami obiektow
                            if player_3.pionki_stan[pionek - 1] == 1:
                                player_3.losowyRuchTest(pionek, 1, player_1, player_2, player_3, player_4)  # tu daje pionek na start
                                break
                            elif player_3.pionki_stan[pionek - 1] == 2:
                                player_3.losowyRuchTest(pionek, oczka, player_1, player_2, player_3, player_4)  # tu sie ruszam pionkiem
                                break

                            elif player_3.pionki_stan[pionek - 1] == 3:
                                player_3.losowyRuchTest(pionek, oczka, player_1, player_2, player_3, player_4)  # tu sie ruszam pionkiem
                                break
                                """
                                if (player_3.suma_oczek[pionek - 1] + oczka) > (player_3.domek_wejscie_chodnik + 5):
                                    print("Niedobry ruch")
                                """


                    elif kolejka == 4:
                        while True:
                            pionek = player_4.wyborPionka()  # to tylko metoda nie robiaca nic z wartościami obiektow
                            if player_4.pionki_stan[pionek - 1] == 1:
                                player_4.losowyRuchTest(pionek, 1, player_1, player_2, player_3, player_4)  # tu daje pionek na start
                                break
                            elif player_4.pionki_stan[pionek - 1] == 2:
                                player_4.losowyRuchTest(pionek, oczka, player_1, player_2, player_3, player_4)  # tu sie ruszam pionkiem
                                break

                            elif player_4.pionki_stan[pionek - 1] == 3:
                                player_4.losowyRuchTest(pionek, oczka, player_1, player_2, player_3, player_4)  # tu sie ruszam pionkiem
                                break
                                """
                                if (player_4.suma_oczek[pionek - 1] + oczka) > (player_4.domek_wejscie_chodnik + 5):
                                    print("Niedobry ruch")
                                """

                    licznik = 0

                    ###########################################################

                    self.board_draw()
                    for i in range(4):
                        player_1.draw(i)
                        player_2.draw(i)
                        player_3.draw(i)
                        player_4.draw(i)
                    pygame.display.update()

                elif oczka != 6:

                    # print("2oczka = ", oczka)
                    # print("2kolejka = ",kolejka)

                    if kolejka == 1:
                        if player_1.pionki_stan == [1, 1, 1, 1]:
                            licznik += 1

                        # warunek taki ze mamy za duzo oczek dla pionka o stusie 3 ale nie ma zadnego pionka coby mozna siebylo nim ruszzyć, ten warunek nalezy skopiować dla kazdego
                        # edit: juz go nie ma

                        elif (player_1.pionki_stan[0] == 2 or player_1.pionki_stan[1] == 2 or player_1.pionki_stan[2] == 2 or player_1.pionki_stan[3] == 2 or player_1.pionki_stan[0] == 3 or
                              player_1.pionki_stan[1] == 3 or player_1.pionki_stan[2] == 3 or player_1.pionki_stan[3] == 3):
                            licznik = max_licznik
                            print("wybierz pionek (ale nie z bazy): ")
                            while True:
                                pionek = player_1.wyborPionka()
                                if player_1.pionki_stan[pionek - 1] == 2:
                                    player_1.losowyRuchTest(pionek, oczka, player_1, player_2, player_3, player_4)
                                    break
                                elif player_1.pionki_stan[pionek - 1] == 3:
                                    """
                                    if (player_1.suma_oczek[pionek - 1] + oczka) > (player_1.domek_wejscie_chodnik + 5):
                                        print("Niedobry ruch")

                                    else:
                                        player_1.losowyRuchTest(pionek, oczka)
                                        break
                                    """
                                    player_1.losowyRuchTest(pionek, oczka, player_1, player_2, player_3, player_4)
                                    break

                                else:
                                    print("Niedobry ruch")


                    elif kolejka == 2:
                        if player_2.pionki_stan == [1, 1, 1, 1]:
                            licznik += 1

                        # warunek taki ze mamy za duzo oczek dla pionka o stusie 3 ale nie ma zadnego pionka coby mozna siebylo nim ruszzyć, ten warunek nalezy skopiować dla kazdego

                        elif (player_2.pionki_stan[0] == 2 or player_2.pionki_stan[1] == 2 or player_2.pionki_stan[2] == 2 or player_2.pionki_stan[3] == 2 or player_2.pionki_stan[0] == 3 or
                              player_2.pionki_stan[1] == 3 or player_2.pionki_stan[2] == 3 or player_2.pionki_stan[3] == 3):
                            licznik = max_licznik
                            print("wybierz pionek (ale nie z bazy): ")
                            while True:
                                pionek = player_2.wyborPionka()
                                if player_2.pionki_stan[pionek - 1] == 2:
                                    player_2.losowyRuchTest(pionek, oczka, player_1, player_2, player_3, player_4)
                                    break
                                elif player_2.pionki_stan[pionek - 1] == 3:
                                    """
                                    if (player_2.suma_oczek[pionek - 1] + oczka) > (player_2.domek_wejscie_chodnik + 5):
                                        print("Niedobry ruch")
                                    else:
                                        player_2.losowyRuchTest(pionek, oczka)
                                        break
                                    """
                                    player_2.losowyRuchTest(pionek, oczka, player_1, player_2, player_3, player_4)
                                    break
                                else:
                                    print("Niedobry ruch")


                    elif kolejka == 3:
                        if player_3.pionki_stan == [1, 1, 1, 1]:
                            licznik += 1

                        # warunek taki ze mamy za duzo oczek dla pionka o stusie 3 ale nie ma zadnego pionka coby mozna siebylo nim ruszzyć, ten warunek nalezy skopiować dla kazdego

                        elif (player_3.pionki_stan[0] == 2 or player_3.pionki_stan[1] == 2 or player_3.pionki_stan[2] == 2 or player_3.pionki_stan[3] == 2 or player_3.pionki_stan[1] == 3 or
                              player_3.pionki_stan[2] == 3 or player_3.pionki_stan[3] == 3):
                            licznik = max_licznik
                            print("wybierz pionek (ale nie z bazy): ")
                            while True:
                                pionek = player_3.wyborPionka()
                                if player_3.pionki_stan[pionek - 1] == 2:
                                    player_3.losowyRuchTest(pionek, oczka, player_1, player_2, player_3, player_4)
                                    break
                                elif player_3.pionki_stan[pionek - 1] == 3:
                                    """
                                    if (player_3.suma_oczek[pionek - 1] + oczka) > (player_3.domek_wejscie_chodnik + 5):
                                        print("Niedobry ruch")
                                    else:
                                        player_3.losowyRuchTest(pionek, oczka)
                                        break
                                    """
                                    player_3.losowyRuchTest(pionek, oczka, player_1, player_2, player_3, player_4)
                                    break
                                else:
                                    print("Niedobry ruch")

                    elif kolejka == 4:
                        if player_4.pionki_stan == [1, 1, 1, 1]:
                            licznik += 1

                        # warunek taki ze mamy za duzo oczek dla pionka o stusie 3 ale nie ma zadnego pionka coby mozna siebylo nim ruszzyć, ten warunek nalezy skopiować dla kazdego

                        elif (player_4.pionki_stan[0] == 2 or player_4.pionki_stan[1] == 2 or player_4.pionki_stan[2] == 2 or player_4.pionki_stan[3] == 2 or player_4.pionki_stan[0] == 3 or
                              player_4.pionki_stan[1] == 3 or player_4.pionki_stan[2] == 3 or player_4.pionki_stan[3] == 3):
                            licznik = max_licznik
                            print("wybierz pionek (ale nie z bazy): ")
                            while True:
                                pionek = player_4.wyborPionka()
                                if player_4.pionki_stan[pionek - 1] == 2:
                                    player_4.losowyRuchTest(pionek, oczka, player_1, player_2, player_3, player_4)
                                    break
                                elif player_4.pionki_stan[pionek - 1] == 3:
                                    """
                                    if (player_4.suma_oczek[pionek - 1] + oczka) > (player_4.domek_wejscie_chodnik + 5):
                                        print("Niedobry ruch")
                                    else:
                                        player_4.losowyRuchTest(pionek, oczka)
                                        break
                                    """
                                    player_4.losowyRuchTest(pionek, oczka, player_1, player_2, player_3, player_4)
                                    break

                                else:
                                    print("Niedobry ruch")

                    # print("2licznik = ", licznik)

                    self.board_draw()
                    for i in range(4):
                        player_1.draw(i)
                        player_2.draw(i)
                        player_3.draw(i)
                        player_4.draw(i)
                    pygame.display.update()

                self.board_draw()
                for i in range(4):
                    player_1.draw(i)
                    player_2.draw(i)
                    player_3.draw(i)
                    player_4.draw(i)
                pygame.display.update()

            self.board_draw()
            for i in range(4):
                player_1.draw(i)
                player_2.draw(i)
                player_3.draw(i)
                player_4.draw(i)
            pygame.display.update()

            if kolejka == 1:
                print("pionki stan = ", player_1.pionki_stan)
                print("pionki suma_oczek = ", player_1.suma_oczek)
            elif kolejka == 2:
                print("pionki stan = ", player_2.pionki_stan)
                print("pionki suma_oczek = ", player_2.suma_oczek)
            elif kolejka == 3:
                print("pionki stan = ", player_3.pionki_stan)
                print("pionki suma_oczek = ", player_3.suma_oczek)
            elif kolejka == 4:
                print("pionki stan = ", player_4.pionki_stan)
                print("pionki suma_oczek = ", player_4.suma_oczek)

            print("Koniec tury gracza nr. ", kolejka)
            print(" ")
            kolejka += 1
            # os.system("cls")

            # os.system("cls")

            self.board_draw()
            for n in range(4):
                player_1.draw(n)
                player_2.draw(n)
                player_3.draw(n)
                player_4.draw(n)

            pygame.display.update()

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

    def bicie(self, player_1, player_2, player_3, player_4, kolej, pionek):

        # 13 26 39
        """
        for i in range(4):
            if (player_1.suma_oczek[pionek - 1] == player_2.suma_oczek[i]) and player_2.pionki_stan[i]== 2 and player_2.suma_oczek[i]!= 13 :
                player_2.pozycja[i] = [96 + self.pozycjaPionkiBaza[i][0], 96 + self.pozycjaPionkiBaza[i][1]]
                player_2.pionki_stan[i] = 1

            if (player_1.suma_oczek[pionek - 1] == player_2.suma_oczek[i]) and player_2.pionki_stan[i]== 2 and player_2.suma_oczek[i]!= 13 :
                player_2.pozycja[i] = [96 + self.pozycjaPionkiBaza[i][0], 96 + self.pozycjaPionkiBaza[i][1]]
                player_2.pionki_stan[i] = 1

            if (player_1.suma_oczek[pionek - 1] == player_2.suma_oczek[i]) and player_2.pionki_stan[i]== 2 and player_2.suma_oczek[i]!= 13 :
                player_2.pozycja[i] = [96 + self.pozycjaPionkiBaza[i][0], 96 + self.pozycjaPionkiBaza[i][1]]
                player_2.pionki_stan[i] = 1

        """

        if kolej == 1:

            if player_1.pionki_stan[pionek - 1] == 2:

                for i in range(4):
                    if (player_1.suma_oczek[pionek - 1] == player_2.suma_oczek[i]) and player_2.pionki_stan[i] == 2 and player_2.suma_oczek[i] != 14:
                        player_2.pozycja[i] = [528 + self.pozycjaPionkiBaza[i][0], 96 + self.pozycjaPionkiBaza[i][1]]
                        player_2.pionki_stan[i] = 1
                        player_2.suma_oczek[i] = 13

                    if (player_1.suma_oczek[pionek - 1] == player_3.suma_oczek[i]) and player_3.pionki_stan[i] == 2 and player_3.suma_oczek[i] != 27:
                        player_3.pozycja[i] = [528 + self.pozycjaPionkiBaza[i][0], 528 + self.pozycjaPionkiBaza[i][1]]
                        player_3.pionki_stan[i] = 1
                        player_3.suma_oczek[i] = 26

                    if (player_1.suma_oczek[pionek - 1] == player_4.suma_oczek[i]) and player_4.pionki_stan[i] == 2 and player_4.suma_oczek[i] != 40:
                        player_4.pozycja[i] = [96 + self.pozycjaPionkiBaza[i][0], 528 + self.pozycjaPionkiBaza[i][1]]
                        player_4.pionki_stan[i] = 1
                        player_4.suma_oczek[i] = 39

        elif kolej == 2:

            if player_2.pionki_stan[pionek - 1] == 2:

                for i in range(4):
                    if (player_2.suma_oczek[pionek - 1] == player_1.suma_oczek[i]) and player_1.pionki_stan[i] == 2 and player_1.suma_oczek[i] != 1:
                        player_1.pozycja[i] = [96 + self.pozycjaPionkiBaza[i][0], 96 + self.pozycjaPionkiBaza[i][1]]
                        player_1.pionki_stan[i] = 1
                        player_1.suma_oczek[i] = 0

                    if (player_2.suma_oczek[pionek - 1] == player_3.suma_oczek[i]) and player_3.pionki_stan[i] == 2 and player_3.suma_oczek[i] != 27:
                        player_3.pozycja[i] = [528 + self.pozycjaPionkiBaza[i][0], 528 + self.pozycjaPionkiBaza[i][1]]
                        player_3.pionki_stan[i] = 1
                        player_3.suma_oczek[i] = 26

                    if (player_2.suma_oczek[pionek - 1] == player_4.suma_oczek[i]) and player_4.pionki_stan[i] == 2 and player_4.suma_oczek[i] != 40:
                        player_4.pozycja[i] = [96 + self.pozycjaPionkiBaza[i][0], 528 + self.pozycjaPionkiBaza[i][1]]
                        player_4.pionki_stan[i] = 1
                        player_4.suma_oczek[i] = 39

        elif kolej == 3:

            if player_3.pionki_stan[pionek - 1] == 2:

                for i in range(4):
                    if (player_3.suma_oczek[pionek - 1] == player_1.suma_oczek[i]) and player_1.pionki_stan[i] == 2 and player_1.suma_oczek[i] != 1:
                        player_1.pozycja[i] = [96 + self.pozycjaPionkiBaza[i][0], 96 + self.pozycjaPionkiBaza[i][1]]
                        player_1.pionki_stan[i] = 1
                        player_1.suma_oczek[i] = 0

                    if (player_3.suma_oczek[pionek - 1] == player_2.suma_oczek[i]) and player_2.pionki_stan[i] == 2 and player_2.suma_oczek[i] != 14:
                        player_2.pozycja[i] = [528 + self.pozycjaPionkiBaza[i][0], 96 + self.pozycjaPionkiBaza[i][1]]
                        player_2.pionki_stan[i] = 1
                        player_2.suma_oczek[i] = 13

                    if (player_3.suma_oczek[pionek - 1] == player_4.suma_oczek[i]) and player_4.pionki_stan[i] == 2 and player_4.suma_oczek[i] != 40:
                        player_4.pozycja[i] = [96 + self.pozycjaPionkiBaza[i][0], 528 + self.pozycjaPionkiBaza[i][1]]
                        player_4.pionki_stan[i] = 1
                        player_4.suma_oczek[i] = 39

        elif kolej == 4:

            if player_4.pionki_stan[pionek - 1] == 2:

                for i in range(4):
                    if (player_4.suma_oczek[pionek - 1] == player_1.suma_oczek[i]) and player_1.pionki_stan[i] == 2 and player_1.suma_oczek[i] != 1:
                        player_1.pozycja[i] = [96 + self.pozycjaPionkiBaza[i][0], 96 + self.pozycjaPionkiBaza[i][1]]
                        player_1.pionki_stan[i] = 1
                        player_1.suma_oczek[i] = 0

                    if (player_4.suma_oczek[pionek - 1] == player_2.suma_oczek[i]) and player_2.pionki_stan[i] == 2 and player_2.suma_oczek[i] != 14:
                        player_2.pozycja[i] = [528 + self.pozycjaPionkiBaza[i][0], 96 + self.pozycjaPionkiBaza[i][1]]
                        player_2.pionki_stan[i] = 1
                        player_2.suma_oczek[i] = 13

                    if (player_4.suma_oczek[pionek - 1] == player_3.suma_oczek[i]) and player_3.pionki_stan[i] == 2 and player_3.suma_oczek[i] != 27:
                        player_3.pozycja[i] = [528 + self.pozycjaPionkiBaza[i][0], 528 + self.pozycjaPionkiBaza[i][1]]
                        player_3.pionki_stan[i] = 1
                        player_3.suma_oczek[i] = 26


# mechaniki z petli glowej programu dam tutaj
class User(Gracz):

    def draw(self, i):
        self.circle(i)

    def wyborPionka(self):
        while True:
            event = pygame.event.wait()
            if (event.type == pygame.KEYDOWN and (
                    event.key == pygame.K_ESCAPE or event.key == pygame.K_1 or event.key == pygame.K_2 or event.key == pygame.K_3 or event.key == pygame.K_4)) or event.type == pygame.QUIT:
                break
        if event.type == pygame.QUIT:
            print("Wyjście")
            os.system("cls")
            sys.exit(0)
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                print("Wyjście")
                os.system("cls")
                sys.exit(0)
            elif event.key == pygame.K_1:
                print("pionek_1")
                return 1
            elif event.key == pygame.K_2:
                print("pionek_2")
                return 2
            elif event.key == pygame.K_3:
                print("pionek_3")
                return 3
            elif event.key == pygame.K_4:
                print("pionek_4")
                return 4
            else:
                print("klawisz_inny")
        else:
            print("inna akcja")


class UserAI(Gracz):

    def draw(self, i):
        self.circle(i)

    def wyborPionka(self):
        for i in range(4):
            if self.pionki_stan[i] == 3:
                print("pionek_", i + 1)
                return i + 1
            elif self.pionki_stan[i] == 2:
                print("pionek_", i + 1)
                return i + 1
            elif self.pionki_stan[i] == 1:
                print("pionek_", i + 1)
                return i + 1
            else:
                pass

# komentarze:
# w przyszlej wersji nie bedzie wymagane podawanie numeru gracza