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


okno = pygame.display.set_mode((800, 800))
pygame.display.set_caption('Chińczyk')

while True:
    pygame.draw.rect(okno, (0, 0, 0), (0, 0, 288, 288))
    pygame.draw.rect(okno, (0, 150, 0), (1, 1, 286, 286))
    pygame.draw.rect(okno, (0, 0, 0), (49, 49, 190, 190))
    pygame.draw.rect(okno, (255, 255, 255), (50, 50, 188, 188))

    pygame.draw.ellipse(okno, (0, 150, 0), (52, 52, 90, 90))
    pygame.draw.ellipse(okno, (0, 150, 0), (144, 52, 90, 90))
    pygame.draw.ellipse(okno, (0, 150, 0), (52, 144, 90, 90))
    pygame.draw.ellipse(okno, (0, 150, 0), (144, 144, 90, 90))

    pygame.draw.rect(okno, (0, 0, 0), (288, 0, 144, 144))

    pygame.draw.rect(okno, (0, 0, 0), (431, 0, 288, 288))
    pygame.draw.rect(okno, (255, 0, 0), (432, 1, 286, 286))
    pygame.draw.rect(okno, (0, 0, 0), (480, 49, 190, 190))
    pygame.draw.rect(okno, (255, 255, 255), (481, 50, 188, 188))

    pygame.draw.ellipse(okno, (255, 0, 0), (483, 52, 90, 90))
    pygame.draw.ellipse(okno, (255, 0, 0), (575, 52, 90, 90))
    pygame.draw.ellipse(okno, (255, 0, 0), (483, 144, 90, 90))
    pygame.draw.ellipse(okno, (255, 0, 0), (575, 144, 90, 90))

    pygame.draw.rect(okno, (255, 255, 255), (288, 1, 47, 47))
    pygame.draw.rect(okno, (255, 255, 255), (336, 1, 47, 47))  # 1
    pygame.draw.rect(okno, (255, 255, 255), (384, 1, 47, 47))
    pygame.draw.rect(okno, (255, 255, 255), (288, 49, 47, 47))
    pygame.draw.rect(okno, (255, 0, 0), (336, 49, 47, 47))  # 2
    pygame.draw.rect(okno, (255, 0, 0), (384, 49, 47, 47))
    pygame.draw.rect(okno, (255, 255, 255), (288, 97, 47, 47))
    pygame.draw.rect(okno, (255, 0, 0), (336, 97, 47, 47))  # 3
    pygame.draw.rect(okno, (255, 255, 255), (384, 97, 47, 47))
    pygame.draw.rect(okno, (255, 255, 255), (288, 145, 47, 47))
    pygame.draw.rect(okno, (255, 0, 0), (336, 145, 47, 47))  # 4
    pygame.draw.rect(okno, (255, 255, 255), (384, 145, 47, 47))
    pygame.draw.rect(okno, (255, 255, 255), (288, 193, 47, 47))
    pygame.draw.rect(okno, (255, 0, 0), (336, 193, 47, 47))  # 5
    pygame.draw.rect(okno, (255, 255, 255), (384, 193, 47, 47))
    pygame.draw.rect(okno, (255, 255, 255), (288, 241, 47, 47))
    pygame.draw.rect(okno, (255, 0, 0), (336, 241, 47, 47))  # 6
    pygame.draw.rect(okno, (255, 255, 255), (384, 241, 47, 47))

    pygame.draw.rect(okno, (0, 0, 0), (0, 288, 144, 144))

    pygame.draw.rect(okno, (255, 255, 255), (1, 288, 47, 47))  ##########
    pygame.draw.rect(okno, (0, 150, 0), (49, 288, 47, 47))
    pygame.draw.rect(okno, (255, 255, 255), (97, 288, 47, 47))
    pygame.draw.rect(okno, (255, 255, 255), (145, 288, 47, 47))  # lewa
    pygame.draw.rect(okno, (255, 255, 255), (193, 288, 47, 47))
    pygame.draw.rect(okno, (255, 255, 255), (241, 288, 47, 47))  ##########  1
    pygame.draw.rect(okno, (255, 255, 255), (431, 288, 47, 47))
    pygame.draw.rect(okno, (255, 255, 255), (479, 288, 47, 47))
    pygame.draw.rect(okno, (255, 255, 255), (527, 288, 47, 47))  # prawa
    pygame.draw.rect(okno, (255, 255, 255), (575, 288, 47, 47))
    pygame.draw.rect(okno, (255, 255, 255), (623, 288, 47, 47))
    pygame.draw.rect(okno, (255, 255, 255), (671, 288, 47, 47))  ##########

    pygame.draw.rect(okno, (255, 255, 255), (1, 336, 47, 47))  ##########
    pygame.draw.rect(okno, (0, 150, 0), (49, 336, 47, 47))
    pygame.draw.rect(okno, (0, 150, 0), (97, 336, 47, 47))
    pygame.draw.rect(okno, (0, 150, 0), (145, 336, 47, 47))  # lewa
    pygame.draw.rect(okno, (0, 150, 0), (193, 336, 47, 47))
    pygame.draw.rect(okno, (0, 150, 0), (241, 336, 47, 47))  ##########  2
    pygame.draw.rect(okno, (0, 0, 255), (431, 336, 47, 47))
    pygame.draw.rect(okno, (0, 0, 255), (479, 336, 47, 47))
    pygame.draw.rect(okno, (0, 0, 255), (527, 336, 47, 47))  # prawa
    pygame.draw.rect(okno, (0, 0, 255), (575, 336, 47, 47))
    pygame.draw.rect(okno, (0, 0, 255), (623, 336, 47, 47))
    pygame.draw.rect(okno, (255, 255, 255), (671, 336, 47, 47))  ##########

    pygame.draw.rect(okno, (255, 255, 255), (1, 384, 47, 47))  ##########
    pygame.draw.rect(okno, (255, 255, 255), (49, 384, 47, 47))
    pygame.draw.rect(okno, (255, 255, 255), (97, 384, 47, 47))
    pygame.draw.rect(okno, (255, 255, 255), (145, 384, 47, 47))  # lewa
    pygame.draw.rect(okno, (255, 255, 255), (193, 384, 47, 47))
    pygame.draw.rect(okno, (255, 255, 255), (241, 384, 47, 47))  ##########  3
    pygame.draw.rect(okno, (255, 255, 255), (431, 384, 47, 47))
    pygame.draw.rect(okno, (255, 255, 255), (479, 384, 47, 47))
    pygame.draw.rect(okno, (255, 255, 255), (527, 384, 47, 47))  # prawa
    pygame.draw.rect(okno, (255, 255, 255), (575, 384, 47, 47))
    pygame.draw.rect(okno, (0, 0, 255), (623, 384, 47, 49))
    pygame.draw.rect(okno, (255, 255, 255), (671, 384, 47, 47))  ##########

    pygame.draw.rect(okno, (0, 0, 0), (0, 431, 288, 288))
    pygame.draw.rect(okno, (255, 255, 0), (1, 432, 286, 286))
    pygame.draw.rect(okno, (0, 0, 0), (49, 480, 190, 190))
    pygame.draw.rect(okno, (255, 255, 255), (50, 481, 188, 188))

    pygame.draw.ellipse(okno, (255, 255, 0), (52, 483, 90, 90))
    pygame.draw.ellipse(okno, (255, 255, 0), (144, 483, 90, 90))
    pygame.draw.ellipse(okno, (255, 255, 0), (52, 575, 90, 90))
    pygame.draw.ellipse(okno, (255, 255, 0), (144, 575, 90, 90))

    pygame.draw.rect(okno, (0, 0, 0), (431, 431, 288, 288))
    pygame.draw.rect(okno, (0, 0, 255), (432, 432, 286, 286))
    pygame.draw.rect(okno, (0, 0, 0), (480, 480, 190, 190))
    pygame.draw.rect(okno, (255, 255, 255), (481, 481, 188, 188))

    pygame.draw.ellipse(okno, (0, 0, 255), (483, 483, 90, 90))
    pygame.draw.ellipse(okno, (0, 0, 255), (575, 483, 90, 90))
    pygame.draw.ellipse(okno, (0, 0, 255), (483, 575, 90, 90))
    pygame.draw.ellipse(okno, (0, 0, 255), (575, 575, 90, 90))

    pygame.draw.rect(okno, (255, 255, 255), (288, 431, 47, 47))
    pygame.draw.rect(okno, (255, 255, 0), (336, 431, 47, 47))  # 1
    pygame.draw.rect(okno, (255, 255, 255), (384, 431, 47, 47))
    pygame.draw.rect(okno, (255, 255, 255), (288, 479, 47, 47))
    pygame.draw.rect(okno, (255, 255, 0), (336, 479, 47, 47))  # 2
    pygame.draw.rect(okno, (255, 255, 255), (384, 479, 47, 47))
    pygame.draw.rect(okno, (255, 255, 255), (288, 527, 47, 47))
    pygame.draw.rect(okno, (255, 255, 0), (336, 527, 47, 47))  # 3
    pygame.draw.rect(okno, (255, 255, 255), (384, 527, 47, 47))
    pygame.draw.rect(okno, (255, 255, 255), (288, 575, 47, 47))
    pygame.draw.rect(okno, (255, 255, 0), (336, 575, 47, 47))  # 4
    pygame.draw.rect(okno, (255, 255, 255), (384, 575, 47, 47))
    pygame.draw.rect(okno, (255, 255, 0), (288, 623, 47, 47))
    pygame.draw.rect(okno, (255, 255, 0), (336, 623, 47, 47))  # 5
    pygame.draw.rect(okno, (255, 255, 255), (384, 623, 47, 47))
    pygame.draw.rect(okno, (255, 255, 255), (288, 671, 47, 47))
    pygame.draw.rect(okno, (255, 255, 255), (336, 671, 47, 47))  # 6
    pygame.draw.rect(okno, (255, 255, 255), (384, 671, 47, 47))

    pygame.draw.rect(okno, (0, 0, 0), (288, 288, 144, 144))

    pygame.draw.polygon(okno, (255, 255, 0),((287, 430),(429, 430),(358,358))) 
    pygame.draw.polygon(okno, (0, 150, 0),((289, 430),(289, 288),(358,358)))
    pygame.draw.polygon(okno, (255, 0, 0),((288, 289),(431, 289),(358,358)))
    pygame.draw.polygon(okno, (0, 0, 255),((430,288),(430, 430),(359,358)))
 
    pygame.draw.line(okno, (150, 0, 150), (389, 6), (424, 41), 2)
    pygame.draw.line(okno, (150, 0, 150), (389, 41), (424, 6), 2)
    pygame.draw.line(okno, (150, 0, 150), (293, 151), (327, 185), 2)
    pygame.draw.line(okno, (150, 0, 150), (293, 185), (327, 151), 2)
    pygame.draw.line(okno, (150, 0, 150), (197, 292), (235, 330), 2)
    pygame.draw.line(okno, (150, 0, 150), (197, 330), (235, 292), 2)
    pygame.draw.line(okno, (150, 0, 150), (437, 293), (472, 328), 2)
    pygame.draw.line(okno, (150, 0, 150), (437, 329), (472, 294), 2)
    pygame.draw.line(okno, (150, 0, 150), (151, 389), (186, 425), 2)
    pygame.draw.line(okno, (150, 0, 150), (152, 425), (186, 389), 2)
    pygame.draw.line(okno, (150, 0, 150), (580, 391), (616, 425), 2)
    pygame.draw.line(okno, (150, 0, 150), (580, 425), (616, 391), 2)
    pygame.draw.line(okno, (150, 0, 150), (389, 485), (424, 520), 2)
    pygame.draw.line(okno, (150, 0, 150), (389, 520), (424, 485), 2)
    pygame.draw.line(okno, (150, 0, 150), (390, 676), (424, 712), 2)
    pygame.draw.line(okno, (150, 0, 150), (390, 712), (424, 676), 2)
    pygame.draw.line(okno, (150, 0, 150), (293, 533), (329, 568), 2)
    pygame.draw.line(okno, (150, 0, 150), (293, 568), (329, 533), 2)

    pygame.draw.circle(okno, (250, 150, 100), (407, 168), 15, 2)
    pygame.draw.circle(okno, (250, 150, 100), (311, 264), 15, 2)
    pygame.draw.circle(okno, (250, 150, 100), (264, 311), 15, 2)
    pygame.draw.circle(okno, (250, 150, 100), (550, 311), 15, 2)
    pygame.draw.circle(okno, (250, 150, 100), (454, 407), 15, 2)
    pygame.draw.circle(okno, (250, 150, 100), (311, 502), 15, 2)
    pygame.draw.circle(okno, (250, 150, 100), (311, 694), 15, 2)

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
