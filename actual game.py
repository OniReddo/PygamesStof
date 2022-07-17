# ('V1')

import random
import pygame
import time


class Methods:
    @staticmethod
    def quit():
        for Event in pygame.event.get():
            if Event.type == pygame.QUIT:
                pygame.quit()
                exit()


class Window:
    def __init__(self):
        self.resx = 1280
        self.resy = 720
        self.flags = pygame.SCALED
        self.window = pygame.display.set_mode((self.resx, self.resy))

    def update(self):
        self.window.fill((255, 255, 255))

        pygame.display.update()


class OBJ:
    def __init__(self, pos, size, color, window):
        self.pos = pos
        self.size = size
        self.color = color
        self.window = window

    def draw(self):
        pygame.draw.rect(self.window,
                         self.color,
                         (
                             self.pos[0],
                             self.pos[1],
                             self.size[0],
                             self.size[1]
                         )
                         )


class OBJ_Handler:
    def __init__(self):
        self.playercount = 0
        self.playerwheel = []

    def add_player(self, pos, size, color, window):
        self.playerwheel.append(OBJ(pos, size, color, window))
        self.playercount += 1


class Game:
    def __init__(self):
        self.clock = pygame.time.Clock()
        self.win = Window()
        self.time = Time()

        self.mainloop()

    def mainloop(self):
        while True:
            self.clock.tick(165)
            Methods.quit()
            self.time.update()
            self.win.update()


class Time:
    def __init__(self):
        self.now = 0
        self.dt = 0
        self.prev_time = 0

    def update(self):
        self.now = time.time()
        self.dt = self.now - self.prev_time
        self.prev_time = self.now


if __name__ == '__main__':
    game = Game()
