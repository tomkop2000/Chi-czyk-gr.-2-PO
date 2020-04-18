import pygame, sys

from Gracz import User


class Game(object):

    def __init__(self):
        #config
        self.tps_max = 60
        self.resolution = (1280 , 720)

        #initialization
        pygame.init()
        self.screen = pygame.display.set_mode((self.resolution[0],self.resolution[1]))
        self.tps_clock = pygame.time.Clock()
        self.tps_delta = 0.0

        self.player_1 = User(self)
        self.player_2 = User(self)
        self.player_3 = User(self)
        self.player_4 = User(self)

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit(0)
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    sys.exit(0)

            #ticking
            self.tps_delta += self.tps_clock.tick()/1000.0
            while self.tps_delta > 1 / self.tps_max:
                self.tick()
                self.tps_delta -= 1 / self.tps_max

            #drawing
            self.screen.fill((0,0,0))
            self.draw()
            pygame.display.flip()



    def tick(self):
        self.player_1.tick()

        for x in range(4):
            pass


    def draw(self):

        for x in range(15+1):
            pygame.draw.line(self.screen,(255,255,255),((self.resolution[0]-self.resolution[1])/2,self.resolution[1]/15*(x)),((self.resolution[0]-self.resolution[1])/2+self.resolution[1],self.resolution[1]/15*(x)),5 )
            pygame.draw.line(self.screen, (255, 255, 255), ((self.resolution[0] - self.resolution[1]) / 2 + self.resolution[1]/15*(x),0), ( (self.resolution[0] - self.resolution[1]) / 2 + self.resolution[1]/15*(x),self.resolution[1]), 5)

        self.player_1.draw(1)
        self.player_2.draw(2)
        self.player_3.draw(3)
        self.player_4.draw(4)


if __name__ == "__main__":
    Game()