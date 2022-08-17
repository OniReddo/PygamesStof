
import pygame
import time


class Methods:
    @staticmethod
    def quit():
        for Event in pygame.event.get():
            if Event.type == pygame.QUIT:
                pygame.quit()
                exit()

    @staticmethod
    def find_add(find, stuff, add_to):
        for search in stuff:
            if search == find:
                add_to.append(search)


class Startup:
    def __init__(self):
        self.window = Render()
        self.time = Time()
        self.framerate = 165
        self.inputs = Input()
        self.camera = Camera(['w', 'a', 's', 'd'], self.inputs.keys)


class Game(Startup):
    def __init__(self):
        super().__init__()

        self.test()

    def test(self):
        while True:
            print(self.camera.pos)
            self.time.clock.tick(self.framerate)
            self.time.update()
            Methods.quit()
            self.inputs.update()
            self.camera.update(self.time.dt)
            self.window.win_update()


class Camera:
    def __init__(self, keys, holder):
        self.pos = [0, 0]
        self.keys = []
        self.holder = holder
        for key in keys:
            Methods.find_add(key, self.holder, self.keys)
        self.speed = []
        print(self.keys)

    def move(self, key, house, step, dt):
        if key:
            self.pos[house] += step * dt

    def update(self, dt):
        self.move(self.keys[0], 0, -100, dt)
        self.move(self.keys[1], 1, -100, dt)
        self.move(self.keys[2], 0, 100, dt)
        self.move(self.keys[3], 1, 100, dt)


class Key:
    def __str__(self):
        return self.key

    def __eq__(self, other):
        if self.key == str(other):
            return True

    def __bool__(self):
        if self.pressed:
            return True
        else:
            return False

    def __init__(self, key):

        print('created key :', key.upper())

        self.key = key
        self.ascii_key = ord(key)
        self.pressed = False


class Input:
    def __init__(self):
        self.keys = []

        self.create('w')
        self.create('a')
        self.create('s')
        self.create('d')

    def create(self, name):
        name = Key(str(name))
        self.keys.append(name)

    def update(self):
        for key in self.keys:
            if pygame.key.get_pressed()[key.ascii_key]:
                key.pressed = True
            else:
                key.pressed = False


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

