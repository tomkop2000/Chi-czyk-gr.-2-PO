# coding=utf-8
import pygame
import pygame.locals

pygame.init()  # funkcja ładująca moduły pyGame'a odpowiedzialne m.in. za dźwięk czy grafikę


class Board(object):
    """
    Plansza do gry. Odpowiada za rysowanie okna gry.
    """

    def __init__(width, height):
        """
        Konstruktor planszy do gry. Przygotowuje okienko gry.
        """


okno = pygame.display.set_mode((1000, 1000))
pygame.display.set_caption('Chińczyk')

while True:
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

    pygame.display.update()


    class ChinczykGame(object):  # łączy wszystkie elementy w całośc
        def __init__(self, width, height):
            pygame.init()
            self.board = Board(width, height)
            # zegar którego użyjemy do kontrolowania szybkości rysowania
            # kolejnych klatek gry
            self.fps_clock = pygame.time.Clock()


    def run(self):
        """
        Główna pętla programu
        """
        while not self.handle_events():
            # działaj w pętli do momentu otrzymania sygnału do wyjścia
            self.board.draw()
            self.fps_clock.tick(30)


    def handle_events(self):
        """
        Obsługa zdarzeń systemowych, tutaj zinterpretujemy np. ruchy myszką
        :return True jeżeli pygame przekazał zdarzenie wyjścia z gry
        """
        for event in pygame.event.get():
            if event.type == pygame.locals.QUIT:
                pygame.quit()
                return True

# Ta część powinna być zawsze na końcu modułu (ten plik jest modułem)
# chcemy uruchomić naszą grę dopiero po tym jak wszystkie klasy zostaną zadeklarowane
if __name__ == "__main__":
    game = ChinczykGame(800, 400)
    game.run()
board = Board(800, 400)
board.draw()