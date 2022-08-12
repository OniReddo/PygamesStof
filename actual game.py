# V 0

import pygame
import time


class Methods:
    @staticmethod
    def quit():
        for Event in pygame.event.get():
            if Event.type == pygame.QUIT:
                pygame.quit()
                exit()


class Startup:
    def __init__(self):
        self.window = Render()
        self.time = Time()
        self.framerate = 165
        self.inputs = Input()


class Game(Startup):
    def __init__(self):
        super().__init__()

        self.test()

    def test(self):
        while True:
            self.time.clock.tick(self.framerate)
            Methods.quit()
            self.inputs.keys_update()
            self.window.win_update()


class Input:
    def __init__(self):
        self.keys_name = []
        self.keys = []

        self.addkey(pygame.K_w)
        self.addkey(pygame.K_a)
        self.addkey(pygame.K_s)
        self.addkey(pygame.K_d)

    def addkey(self, key):
        self.keys_name.append(key)
        self.keys.append(False)

    def keys_update(self, count=0):

        for key in self.keys_name:
            if pygame.key.get_pressed()[key]:
                self.keys[count] = True
            else:
                self.keys[count] = False
            count += 1


class Time:
    def __init__(self):
        self.clock = pygame.time.Clock()

        self.starttime = time.time()
        self.now = 0
        self.dt = 0
        self.prev_time = 0

    def update(self):
        self.now = time.time()
        self.dt = self.now - self.prev_time
        self.prev_time = self.now


class Screen:
    def __init__(self):
        self.res = [1600, 900]
        self.resx = self.res[0]
        self.resy = self.res[1]
        self.flags = None
        self.window = pygame.display.set_mode((self.resx, self.resy))


class Render(Screen):
    def __init__(self):
        super().__init__()

    def win_update(self):
        self.window.fill((255, 255, 255))
        pygame.display.update()


if __name__ == '__main__':
    game = Game()
