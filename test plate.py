## V 0
#
# import pygame
# import time
#
#
# class Methods:
#    @staticmethod
#    def quit():
#        for Event in pygame.event.get():
#            if Event.type == pygame.QUIT:
#                pygame.quit()
#                exit()
#
#
# class Startup:
#    def __init__(self):
#        self.camera = Camera()
#        self.window = Render()
#        self.time = Time()
#        self.framerate = 165
#        self.inputs = Input()
#        self.objs = Obj_handler()
#        self.objs.add_obj(size=[25,25],
#                          pos=[-25,-25],
#                          color=(0, 0, 0),
#                          surface=self.window.window,
#                          cam=self.camera.pos)
#        self.objs.add_obj(size=[25,25],
#                          pos=[0,0],
#                          color=(0, 0, 0),
#                          surface=self.window.window,
#                          cam=self.camera.pos)
#        self.objs.add_obj(size=[25, 25],
#                          pos=[25, 25],
#                          color=(0, 0, 0),
#                          surface=self.window.window,
#                          cam=self.camera.pos)
#        self.objs.add_obj(size=[2000,150],
#                          pos=[-200,800],
#                          color=(0, 0, 0),
#                          surface=self.window.window,
#                          cam=self.camera.pos)
#        self.window.renders.append(self.objs.objs)
#
#
#
# class Game(Startup):
#    def __init__(self):
#        super().__init__()
#
#        self.test()
#
#    def test(self):
#        while True:
#            self.time.clock.tick(self.framerate)
#            Methods.quit()
#            self.time.update()
#            self.inputs.keys_update()
#            self.camera.check_inputs(self.inputs.keys[0], 1, -321, self.time.dt)
#            self.camera.check_inputs(self.inputs.keys[1], 0, -321, self.time.dt)
#            self.camera.check_inputs(self.inputs.keys[2], 1, 321, self.time.dt)
#            self.camera.check_inputs(self.inputs.keys[3], 0, 321, self.time.dt)
#            print(self.camera.pos)
#            self.window.win_update()
#
#
# class Camera:
#    def __init__(self):
#        self.pos = [0, 0]
#
#    def check_inputs(self, argument, house, step, dt):
#        if argument:
#            self.pos[house] += step*dt
#
#
# class Obj_handler:
#    def __init__(self):
#        self.objs = []
#        self.obj_count = 0
#
#    def add_obj(self, size, pos, color, surface, cam):
#        self.objs.append(Object(size, pos, color, surface, cam))
#        self.obj_count += 1
#
#
# class Object:
#    def __init__(self, size, pos, color, surface, cam):
#        self.size = size
#        self.cam = cam
#        self.pos = pos
#        self.color = color
#        self.surface = surface
#
#    def draw(self):
#        pygame.draw.rect(self.surface, self.color, ((self.pos[0]-self.cam[0],self.pos[1]-self.cam[1]), self.size))
#
#
# class Input:
#    def __init__(self):
#        self.keys_name = []
#        self.keys = []
#
#        self.addkey(pygame.K_w)
#        self.addkey(pygame.K_a)
#        self.addkey(pygame.K_s)
#        self.addkey(pygame.K_d)
#
#    def addkey(self, key):
#        self.keys_name.append(key)
#        self.keys.append(False)
#
#    def keys_update(self, count=0):
#
#        for key in self.keys_name:
#            if pygame.key.get_pressed()[key]:
#                self.keys[count] = True
#            else:
#                self.keys[count] = False
#            count += 1
#
#
# class Time:
#    def __init__(self):
#        self.clock = pygame.time.Clock()
#
#        self.starttime = time.time()
#        self.now = 0
#        self.dt = 0
#        self.prev_time = 0
#
#    def update(self):
#        self.now = time.time()
#        self.dt = self.now - self.prev_time
#        self.prev_time = self.now
#
#
# class Screen:
#    def __init__(self):
#        self.res = [1600, 900]
#        self.resx = self.res[0]
#        self.resy = self.res[1]
#        self.flags = None
#        self.window = pygame.display.set_mode((self.resx, self.resy))
#
#
# class Render(Screen):
#    def __init__(self):
#        super().__init__()
#
#        self.renders = []
#
#    def win_update(self):
#        self.window.fill((255, 255, 255))
#        for render in self.renders:
#            self.render_all(render)
#        pygame.display.update()
#
#    def render_all(self, argument):
#        for count in argument:
#            count.draw()
#
#
# if __name__ == '__main__':
#    game = Game()
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

            self.window.win_update()


class Camera:
    def __init__(self, keys):
        self.pos = [0, 0]
        self.keys = keys
        self.speed = []


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

        self.create('a')
        print(self.keys)

        function(argument1, self.keys.)

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

