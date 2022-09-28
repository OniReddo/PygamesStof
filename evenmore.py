import time
import random
import pygame
import inputs as npt


class Time:
    start_time = time.time()
    now = 0
    DT = 0
    prev_time = 0

    @classmethod
    def update(cls):
        cls.now = time.time()
        cls.dt = cls.now - cls.prev_time
        cls.prev_time = cls.now


class Methods:
    @staticmethod
    def quit():
        for Event in pygame.event.get():
            if Event.type == pygame.QUIT:
                pygame.quit()
                exit()


class Screen:
    resx = 1600
    resy = 900
    res = [resx, resy]
    flags = None
    Window = pygame.display.set_mode(res)


class Camera:
    pos = [0, 0]
    zoom = 0  # Possible ?


class Game:
    def __init__(self):
        self.test_stage()

    def test_stage(self):
        while True:
            Methods.quit()
            Time.update()
            npt.update()


if __name__ == '__main__':
    game = Game()
