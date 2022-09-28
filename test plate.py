

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
        self.time = Time()
        self.framerate = 165
        self.inputs = Input()
        self.camera = Camera(['w', 'a', 's', 'd'], self.inputs.keys)
        self.window = Render(self.camera.pos)
        self.handler = OBJ_Handler(self.window.window)



class Game(Startup):
    def __init__(self):
        super().__init__()

        self.scenario_1()

    def scenario_1(self):
        self.handler.add_obj([0, 0], [10, 10], [50, 50, 50])
        self.handler.add_obj([-100, 800], [1800, 100], [0, 0, 0])
        player = Player(self.handler.objs[0], ['w', 'a', 's', 'd'], self.inputs.keys, self.inputs.mouse, self.handler)

        while True:
            self.time.clock.tick(self.framerate)
            self.time.update()
            Methods.quit()
            # stuff
            self.inputs.update()
            self.camera.update(self.time.dt)
            player.update(self.time.dt)
            # stuff
            self.window.win_update(self.handler.objs, self.handler)


class Player:
    def __init__(self, obj, keys, k_holder, mouse, handler):
        self.object = obj
        self.keys = []
        self.key_holder = k_holder
        self.mouse = mouse

        for key in keys:
            Methods.find_add(key, self.key_holder, self.keys)
        print('player keys : ', self.keys)

        self.tps = []
        self.handler = handler

    def move(self, key, house, step, dt):
        if key:
            self.object.pos[house] += step * dt

    def teleport(self):
        if self.mouse.state[0]:

            self.handler.add_line(self.object.pos,self.mouse.pos,[0,0,0])

            self.object.pos[0] = self.mouse.pos[0]
            self.object.pos[1] = self.mouse.pos[1]

    def update(self, dt):
        self.teleport()
        self.move(self.keys[0], 1, -500, dt)
        self.move(self.keys[1], 0, -500, dt)
        self.move(self.keys[2], 1, 500, dt)
        self.move(self.keys[3], 0, 500, dt)


class OBJ_Handler:
    def __init__(self, screen):
        self.objs = []
        self.count = -1
        self.screen = screen

    def add_obj(self, truepos, size, color):
        self.count += 1
        self.objs.append(OBJ(truepos, size, self.screen, color))

    def add_line(self,  pos1, pos2, color):

        self.count += 1

        self.objs.append(Line(self.screen, pos1, pos2, color, self.count))


class Line:
    def __eq__(self, other):
        if other == 'line':
            return True
        else:
            return False

    def __init__(self, screen, s_pos, e_pos, color, count):
        self.screen = screen
        self.startpos = [s_pos[0], s_pos[1]]
        self.endpos = [e_pos[0], e_pos[1]]
        self.color = color
        self.count = count
        print(self.color)

    def draw(self):

        if self.color[0] < 255:
            self.color[0] += 5
            self.color[1] += 5
            self.color[2] += 5

        pygame.draw.line(self.screen, self.color, self.startpos, self.endpos, 5)


class OBJ:
    def __init__(self, truepos, size, screen, color):
        self.truepos = truepos
        self.pos = truepos
        self.size = size
        self.screen = screen
        self.color = color

    def draw(self, cam_posx, cam_posy):
        pygame.draw.rect(self.screen, self.color, ((self.pos[0] - cam_posx, self.pos[1] - cam_posy), self.size))


class Camera:
    def __init__(self, keys, holder):
        self.pos = [0, 0]
        self.keys = []
        self.holder = holder
        for key in keys:
            Methods.find_add(key, self.holder, self.keys)
        self.speed = []
        self.can_move = False

    def move(self, key, house, step, dt):
        if key:
            self.pos[house] += step * dt

    def update(self, dt):
        if self.can_move:
            self.move(self.keys[0], 1, -500, dt)
            self.move(self.keys[1], 0, -500, dt)
            self.move(self.keys[2], 1, 500, dt)
            self.move(self.keys[3], 0, 500, dt)


class Key:
    def __repr__(self):
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


class Mouse:
    def __init__(self):
        self.state = [False, False]
        self.left = self.state[0]
        self.right = self.state[1]
        self.pos = [0, 0]
        self.get = pygame.mouse


class Input:
    def __init__(self):
        self.keys = []
        self.mouse = Mouse()

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

        self.mouse.pos[0] = self.mouse.get.get_pos()[0]
        self.mouse.pos[1] = self.mouse.get.get_pos()[1]

        if self.mouse.get.get_pressed()[0]:
            self.mouse.state[0] = True
        else:
            self.mouse.state[0] = False

        if self.mouse.get.get_pressed()[2]:
            self.mouse.state[1] = True
        else:
            self.mouse.state[1] = False


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
    def __init__(self, cam):
        super().__init__()
        self.cam = cam

    def win_update(self, objects, handler):
        self.window.fill((255, 255, 255))
        self.render_all(objects, handler)
        pygame.display.update()

    def render_all(self, objects, handler):
        for obj in objects:
            if obj != 'line':
                obj.draw(self.cam[0], self.cam[1])
            else:
                obj.draw()

                if obj.color[0] == 255:
                    del handler.objs[obj.count]
                    handler.count -= 1


if __name__ == '__main__':
    game = Game()

