# coding=utf-8
import pygame, sys
import pygame.locals
import random
from Gracz import User

pygame.init()  # funkcja ładująca moduły pyGame'a odpowiedzialne m.in. za dźwięk czy grafikę


class Board(object):
    """
    Plansza do gry. Odpowiada za rysowanie okna gry.
    """

    def __init__(width, height):
        """
        Konstruktor planszy do gry. Przygotowuje okienko gry.
        """


resolution_x = 720
resolution_y = 720

okno = pygame.display.set_mode((resolution_x, resolution_y))

pygame.display.set_caption('Chińczyk')

#numery od 1 do 4 to numer gracza
player_1 = User(okno,1)
player_2 = User(okno,2)
player_3 = User(okno,3)
player_4 = User(okno,4)





def board_draw():
    pygame.draw.rect(okno, (0, 0, 0), (0, 0, 225, 224))
    pygame.draw.rect(okno, (0, 150, 0), (1, 1, 224, 223))
    pygame.draw.rect(okno, (0, 0, 0), (49, 49, 123, 123))
    pygame.draw.rect(okno, (255, 255, 255), (50, 50, 121, 121))

    pygame.draw.ellipse(okno, (0, 150, 0), (60, 60, 45, 45))
    pygame.draw.ellipse(okno, (0, 150, 0), (115, 60, 45, 45))
    pygame.draw.ellipse(okno, (0, 150, 0), (60, 115, 45, 45))
    pygame.draw.ellipse(okno, (0, 150, 0), (115, 115, 45, 45))

    pygame.draw.rect(okno, (0, 0, 0), (225, 0, 150, 225))

    pygame.draw.rect(okno, (0, 0, 0), (375, 0, 225, 224))
    pygame.draw.rect(okno, (255, 0, 0), (376, 1, 224, 223))
    pygame.draw.rect(okno, (0, 0, 0), (430, 49, 123, 123))
    pygame.draw.rect(okno, (255, 255, 255), (431, 50, 121, 121))

    pygame.draw.ellipse(okno, (255, 0, 0), (435, 60, 45, 45))
    pygame.draw.ellipse(okno, (255, 0, 0), (490, 60, 45, 45))
    pygame.draw.ellipse(okno, (255, 0, 0), (435, 115, 45, 45))
    pygame.draw.ellipse(okno, (255, 0, 0), (490, 115, 45, 45))

    pygame.draw.rect(okno, (255, 255, 255), (226, 1, 49, 36))
    pygame.draw.rect(okno, (255, 255, 255), (276, 1, 49, 36))  # 1
    pygame.draw.rect(okno, (255, 255, 255), (326, 1, 49, 36))
    pygame.draw.rect(okno, (255, 255, 255), (226, 38, 49, 36))
    pygame.draw.rect(okno, (255, 0, 0), (276, 38, 49, 36))  # 2
    pygame.draw.rect(okno, (255, 0, 0), (326, 38, 49, 36))
    pygame.draw.rect(okno, (255, 255, 255), (226, 75, 49, 36))
    pygame.draw.rect(okno, (255, 0, 0), (276, 75, 49, 36))  # 3
    pygame.draw.rect(okno, (255, 255, 255), (326, 75, 49, 36))
    pygame.draw.rect(okno, (255, 255, 255), (226, 112, 49, 36))
    pygame.draw.rect(okno, (255, 0, 0), (276, 112, 49, 36))  # 4
    pygame.draw.rect(okno, (255, 255, 255), (326, 112, 49, 36))
    pygame.draw.rect(okno, (255, 255, 255), (226, 149, 49, 36))
    pygame.draw.rect(okno, (255, 0, 0), (276, 149, 49, 36))  # 5
    pygame.draw.rect(okno, (255, 255, 255), (326, 149, 49, 36))
    pygame.draw.rect(okno, (255, 255, 255), (226, 186, 49, 37))
    pygame.draw.rect(okno, (255, 0, 0), (276, 186, 49, 37))  # 6
    pygame.draw.rect(okno, (255, 255, 255), (326, 186, 49, 37))

    pygame.draw.rect(okno, (0, 0, 0), (0, 225, 225, 150))

    pygame.draw.rect(okno, (255, 255, 255), (1, 225, 36, 49))  ##########
    pygame.draw.rect(okno, (0, 150, 0), (38, 225, 36, 49))
    pygame.draw.rect(okno, (255, 255, 255), (75, 225, 36, 49))
    pygame.draw.rect(okno, (255, 255, 255), (112, 225, 36, 49))  # lewa
    pygame.draw.rect(okno, (255, 255, 255), (149, 225, 37, 49))
    pygame.draw.rect(okno, (255, 255, 255), (187, 225, 37, 49))  ##########  1
    pygame.draw.rect(okno, (255, 255, 255), (376, 225, 37, 49))
    pygame.draw.rect(okno, (255, 255, 255), (414, 225, 37, 49))
    pygame.draw.rect(okno, (255, 255, 255), (452, 225, 36, 49))  # prawa
    pygame.draw.rect(okno, (255, 255, 255), (489, 225, 36, 49))
    pygame.draw.rect(okno, (255, 255, 255), (526, 225, 36, 49))
    pygame.draw.rect(okno, (255, 255, 255), (563, 225, 36, 49))  ##########

    pygame.draw.rect(okno, (255, 255, 255), (1, 275, 36, 49))  ##########
    pygame.draw.rect(okno, (0, 150, 0), (38, 275, 36, 49))
    pygame.draw.rect(okno, (0, 150, 0), (75, 275, 36, 49))
    pygame.draw.rect(okno, (0, 150, 0), (112, 275, 36, 49))  # lewa
    pygame.draw.rect(okno, (0, 150, 0), (149, 275, 37, 49))
    pygame.draw.rect(okno, (0, 150, 0), (187, 275, 37, 49))  ##########  2
    pygame.draw.rect(okno, (0, 0, 255), (376, 275, 37, 49))
    pygame.draw.rect(okno, (0, 0, 255), (414, 275, 37, 49))
    pygame.draw.rect(okno, (0, 0, 255), (452, 275, 36, 49))  # prawa
    pygame.draw.rect(okno, (0, 0, 255), (489, 275, 36, 49))
    pygame.draw.rect(okno, (0, 0, 255), (526, 275, 36, 49))
    pygame.draw.rect(okno, (255, 255, 255), (563, 275, 36, 49))  ##########

    pygame.draw.rect(okno, (255, 255, 255), (1, 325, 36, 49))  ##########
    pygame.draw.rect(okno, (255, 255, 255), (38, 325, 36, 49))
    pygame.draw.rect(okno, (255, 255, 255), (75, 325, 36, 49))
    pygame.draw.rect(okno, (255, 255, 255), (112, 325, 36, 49))  # lewa
    pygame.draw.rect(okno, (255, 255, 255), (149, 325, 37, 49))
    pygame.draw.rect(okno, (255, 255, 255), (187, 325, 37, 49))  ##########  3
    pygame.draw.rect(okno, (255, 255, 255), (376, 325, 37, 49))
    pygame.draw.rect(okno, (255, 255, 255), (414, 325, 37, 49))
    pygame.draw.rect(okno, (255, 255, 255), (452, 325, 36, 49))  # prawa
    pygame.draw.rect(okno, (255, 255, 255), (489, 325, 36, 49))
    pygame.draw.rect(okno, (0, 0, 255), (526, 325, 36, 49))
    pygame.draw.rect(okno, (255, 255, 255), (563, 325, 36, 49))  ##########

    pygame.draw.rect(okno, (0, 0, 0), (0, 373, 225, 224))
    pygame.draw.rect(okno, (120, 0, 255), (1, 374, 224, 223))
    pygame.draw.rect(okno, (0, 0, 0), (49, 425, 123, 123))
    pygame.draw.rect(okno, (255, 255, 255), (50, 426, 121, 121))

    pygame.draw.ellipse(okno, (120, 0, 255), (60, 433, 45, 45))
    pygame.draw.ellipse(okno, (120, 0, 255), (115, 433, 45, 45))
    pygame.draw.ellipse(okno, (120, 0, 255), (60, 483, 45, 45))
    pygame.draw.ellipse(okno, (120, 0, 255), (115, 483, 45, 45))

    pygame.draw.rect(okno, (0, 0, 0), (375, 373, 225, 224))
    pygame.draw.rect(okno, (0, 0, 255), (376, 374, 224, 223))
    pygame.draw.rect(okno, (0, 0, 0), (430, 431, 123, 123))
    pygame.draw.rect(okno, (255, 255, 255), (431, 431, 121, 121))

    pygame.draw.ellipse(okno, (0, 0, 255), (445, 440, 45, 45))
    pygame.draw.ellipse(okno, (0, 0, 255), (495, 440, 45, 45))
    pygame.draw.ellipse(okno, (0, 0, 255), (445, 495, 45, 45))
    pygame.draw.ellipse(okno, (0, 0, 255), (495, 495, 45, 45))

    pygame.draw.rect(okno, (255, 255, 255), (226, 375, 49, 37))
    pygame.draw.rect(okno, (120, 0, 255), (276, 375, 49, 37))  # 1
    pygame.draw.rect(okno, (255, 255, 255), (326, 375, 49, 37))
    pygame.draw.rect(okno, (255, 255, 255), (226, 413, 49, 37))
    pygame.draw.rect(okno, (120, 0, 255), (276, 413, 49, 37))  # 2
    pygame.draw.rect(okno, (255, 255, 255), (326, 413, 49, 37))
    pygame.draw.rect(okno, (255, 255, 255), (226, 451, 49, 36))
    pygame.draw.rect(okno, (120, 0, 255), (276, 451, 49, 36))  # 3
    pygame.draw.rect(okno, (255, 255, 255), (326, 451, 49, 36))
    pygame.draw.rect(okno, (255, 255, 255), (226, 488, 49, 36))
    pygame.draw.rect(okno, (120, 0, 255), (276, 488, 49, 36))  # 4
    pygame.draw.rect(okno, (255, 255, 255), (326, 488, 49, 36))
    pygame.draw.rect(okno, (120, 0, 255), (226, 525, 49, 36))
    pygame.draw.rect(okno, (120, 0, 255), (276, 525, 49, 36))  # 5
    pygame.draw.rect(okno, (255, 255, 255), (326, 525, 49, 36))
    pygame.draw.rect(okno, (255, 255, 255), (226, 562, 49, 36))
    pygame.draw.rect(okno, (255, 255, 255), (276, 562, 49, 36))  # 6
    pygame.draw.rect(okno, (255, 255, 255), (326, 562, 49, 36))



    # print("Plansza narysowana")

    for x in range(15 + 1):
        pygame.draw.line(okno, (89, 89, 89),(48*x, 0),(48*x,720), 5)
        pygame.draw.line(okno,  (89, 89, 89),(0, 48*x),(720,48*x), 5)




    return 1


def losowanie():
    oczka =random.randint(1, 6)
    print("Kostka: ", oczka)
    return oczka

def key_check():
    while True:
        event = pygame.event.wait()
        if (event.type == pygame.KEYDOWN and (event.key == pygame.K_ESCAPE or event.key == pygame.K_1 or event.key == pygame.K_2 or event.key == pygame.K_3 or event.key == pygame.K_4)) or event.type == pygame.QUIT:
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


event = pygame.event.clear()

counter = 0


board_draw()
for i in range(4):
    player_1.draw(i)
    player_2.draw(i)
    player_3.draw(i)
    player_4.draw(i)

pygame.display.update()
1

while True:


    #pętla gry nie urzywamy systemu tick i delta time bo klatka gry jest zamrażana
    counter += board_draw()



    print("Plansza nr. ", counter, " narysowana")


    oczka = player_1.losowanie()

    oczka = player_2.losowanie()

    oczka = player_3.losowanie()

    oczka = player_4.losowanie()

    #player_1.prostyRuch()

    player_1.losowyRuchTest(1,1,1)
    print(player_1.pozycja)













    for i in range(4):
        player_1.draw(i)
        player_2.draw(i)
        player_3.draw(i)
        player_4.draw(i)

    pygame.display.update()


    print(key_check())