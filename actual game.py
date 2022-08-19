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
        self.framerate = 165
        self.window = Render()
        self.time = Time()
        self.inputs = Input()
        self.camera = Camera(self.inputs)
        self.handler = OBJ_Handler(self.window.window)


class Game(Startup):
    def __init__(self):
        super().__init__()

        self.test()

    def test(self):
        # Assets
        self.handler.add_rec([0, 0, 0], [int(self.window.resx / 2), int(self.window.resy / 2)], [10, 10])

        self.handler.add_line([50, 50, 50], [0, 0], [1600, 0], 30)
        self.handler.add_line([50, 50, 50], [0, 900], [1600, 900], 30)
        self.handler.add_line([50, 50, 50], [0, -14], [0, 915], 30)
        self.handler.add_line([50, 50, 50], [1600, -14], [1600, 915], 30)

        player = Player(self.handler.rect[0], self.inputs, ['w', 'a', 's', 'd'])

        while True:
            # System
            self.time.clock.tick(self.framerate)
            self.time.update()
            Methods.quit()
            # Stuff
            self.inputs.update()
            self.camera.update(self.time.dt, player.obj, self.window.res)
            player.update(self.time.dt, self.inputs.mouse, self.camera, self.time, self.handler)

            # System
            self.window.win_update(self.handler.objs, self.camera.pos)


class OBJ_Handler:
    def __init__(self, screen=None):
        self.screen = screen
        self.rect = []
        self.line = []
        self.objs = [self.rect, self.line]

    def add_rec(self, color, pos, size):
        self.rect.append(Rect(self.screen, color, pos, size))

    def add_line(self, color, spos, epos, width=5, fade=False):
        self.line.append(Line(self.screen, self.line, color, spos, epos, width, fade))


class Player:
    def __init__(self, obj, holder, keys):
        self.obj = obj
        self.keys = []
        self.control = True

        self.tp = [True, 1]

        for key in keys:
            holder.add_key(key, self.keys)

    def move(self, key, house, step, dt):
        if key:
            self.obj.t_pos[house] += int(step * dt)

    def teleport(self, mouse, cam, timer, handler):

        handler.add_line([0, 0, 0], [self.obj.t_pos[0], self.obj.t_pos[1]],
                         [mouse.pos[0]+cam.pos[0], mouse.pos[1]+cam.pos[1]], 5, True)

        self.tp[0] = False
        self.tp[1] = timer.now
        self.obj.t_pos[0] = mouse.pos[0] + cam.pos[0]
        self.obj.t_pos[1] = mouse.pos[1] + cam.pos[1]

    def update(self, dt, mouse, cam, timer, handler):
        if self.control:
            self.move(self.keys[0], 1, -500, dt)
            self.move(self.keys[1], 0, -500, dt)
            self.move(self.keys[2], 1, 500, dt)
            self.move(self.keys[3], 0, 500, dt)

            if mouse.right and self.tp[0]:
                self.teleport(mouse, cam, timer, handler)
            if not self.tp[0]:
                if timer.now - self.tp[1] >= 1:
                    self.tp[0] = True


class Rect:
    def __init__(self, screen, color, pos, size):
        self.screen = screen
        self.color = color
        self.pos = [0, 0]
        self.t_pos = pos
        self.size = size

    def draw(self, cam):

        self.pos[0] = self.t_pos[0] - cam[0]
        self.pos[1] = self.t_pos[1] - cam[1]

        pygame.draw.rect(self.screen, self.color, (self.pos, self.size))


class Line:
    def __init__(self, screen, origin, color, spos, epos, width=5, fade=False):
        self.origin = origin
        self.screen = screen
        self.color = color
        self.t_spos = spos
        self.t_epos = epos
        self.spos = [0, 0]
        self.epos = [0, 0]
        self.width = width
        self.fade = fade

    def draw(self, cam):

        if self.color[0] >= 250:
            del self.origin[4]

        self.spos[0] = self.t_spos[0] - cam[0]
        self.spos[1] = self.t_spos[1] - cam[1]

        self.epos[0] = self.t_epos[0] - cam[0]
        self.epos[1] = self.t_epos[1] - cam[1]

        if self.fade:
            self.color[0] += 5
            self.color[1] += 5
            self.color[2] += 5

        pygame.draw.line(self.screen, self.color, self.spos, self.epos, self.width)


class Camera:
    def __init__(self, holder):
        self.pos = [0, 0]
        self.keys = []
        self.control = True

        for key in ['w', 'a', 's', 'd', ' ']:
            holder.add_key(key, self.keys)

        self.speed = []

    def move(self, key, house, step, dt):
        if key:
            self.pos[house] += step * dt

    def update(self, dt, track=None, res=None):
        # Track
        if track is not None and self.keys[4]:
            self.pos[0] = track.t_pos[0] - int(res[0] / 2)
            self.pos[1] = track.t_pos[1] - int(res[1] / 2)

        print('\n p t_pos', track.t_pos)
        print('p pos', track.pos)
        print('c pos', self.pos)


class Input:
    def __init__(self):
        self.keys = []

        self.create('w')
        self.create('a')
        self.create('s')
        self.create('d')
        self.create(' ')

        self.mouse = Mouse()

    def add_key(self, find, add_to):
        for search in self.keys:
            if search == find:
                add_to.append(search)

    def create(self, name):
        name = Key(str(name))
        self.keys.append(name)

    def update(self):
        # kboar
        for key in self.keys:
            if pygame.key.get_pressed()[key.ascii_key]:
                key.pressed = True
            else:
                key.pressed = False
        # mosue
        self.mouse.pos[0] = pygame.mouse.get_pos()[0]
        self.mouse.pos[1] = pygame.mouse.get_pos()[1]

        if pygame.mouse.get_pressed()[0]:
            self.mouse.left = True
        else:
            self.mouse.left = False

        if pygame.mouse.get_pressed()[2]:
            self.mouse.right = True
        else:
            self.mouse.right = False


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
    def __str__(self):
        return f'{self.pos}, {self.left},{self.right}'

    def __init__(self):
        self.pos = [0, 0]
        self.left = False
        self.right = False


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

    def win_update(self, content, cam):
        self.window.fill((255, 255, 255))
        self.render_list(content, cam)
        pygame.display.update()

    @staticmethod
    def render_list(content, cam):
        # try:
        if len(content) > 0:
            for holder in content:
                for obj in holder:
                    obj.draw(cam)
    # except:
    #    print('bruh')


if __name__ == '__main__':
    game = Game()
