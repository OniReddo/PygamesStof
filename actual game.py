
print('V1')

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