import time
import random
import pygame.time
import pygame
import inputs as npt



class Time:
    clock = pygame.time.Clock()

    start_time = time.time()
    now = 0
    DT = 0
    prev_time = 0

    @classmethod
    def update(cls):
        cls.now = time.time()
        cls.DT = cls.now - cls.prev_time
        cls.prev_time = cls.now


class Methods:
    @staticmethod
    def quit():
        for Event in pygame.event.get():
            if Event.type == pygame.QUIT:
                pygame.quit()
                exit()


class Camera:
    pos = [0, 0]
    zoom = 0  # Possible ?


class Screen:
    resx = 1600
    resy = 900
    res = [resx, resy]
    flags = None
    Window = pygame.display.set_mode(res)

    @classmethod
    def update(cls, recs, circles, text):
        cls.Window.fill((255, 255, 255))

        for rec in recs:
            rec.draw()
        for ball in circles:
            ball.draw()
        for text in text:
            text.update()

        pygame.display.update()


class Rec:
    def __init__(self, pos, size, coloring):
        self.pos = pos
        self.size = size
        self.coloring = coloring

    def draw(self):
        pygame.draw.rect(Screen.Window, self.coloring, (self.pos, self.size))


class Circ:
    def __init__(self, pos, radius, coloring):
        self.pos = pos
        self.radius = radius
        self.coloring = coloring

    def draw(self):
        pygame.draw.circle(Screen.Window, self.coloring, self.pos, self.radius)


class Text:
    pygame.font.init()
    textfont = pygame.font.SysFont("monospace", 20)

    def __init__(self, text, pos, house=None, fade=False):
        self.path = text
        self.text = str(self.path)
        self.pos = pos
        self.house = house
        self.fade = fade
        self.color = [255, 255, 255]
        self.surface = Text.textfont.render(self.text, True, self.color)

    def update(self):
        if self.fade and ~self.color[0] > 50:
            self.color[0] -= Time.DT
            self.color[1] -= Time.DT
            self.color[2] -= Time.DT

        self.text = str(self.path)
        self.surface = Text.textfont.render(self.text, True, self.color)
        Screen.Window.blit(self.surface, (self.pos[0], self.pos[1]))


class Player:
    def __init__(self, obj, keys, speed=500):
        self.obj = obj
        self.keys = keys
        self.speed = speed

    def update(self):
        if self.keys[0] and self.obj.pos[1] > 50:
            self.obj.pos[1] -= self.speed * Time.DT
        if self.keys[1] and self.obj.pos[1] < 750:
            self.obj.pos[1] += self.speed * Time.DT


class Game_ball:
    def __init__(self, obj):
        self.colliding = [0]
        self.obj = obj
        self.cons_speed = 1200
        self.speed = [self.cons_speed, self.cons_speed]

    def update(self, players):
        if self.obj.pos[1] <= 60:
            self.obj.pos[1] += 1
            self.speed[1] = self.cons_speed
            self.colliding[0] += 1

        elif self.obj.pos[1] >= 890:
            self.obj.pos[1] -= 1
            self.speed[1] = -self.cons_speed
            self.colliding[0]  += 1

        elif self.obj.pos[0] >= 1095:
            self.obj.pos[1] -= 1
            self.speed[0] = -self.cons_speed
            self.colliding[0]  += 1

        elif self.obj.pos[0] <= 5:
            self.obj.pos[1] += 1
            self.speed[0] = self.cons_speed
            self.colliding[0] += 1  

        else:
            pass
            #self.colliding[0] += 1

        for player in players:
            player_rect = pygame.Rect((player.obj.pos[0], player.obj.pos[1]),
                                      (player.obj.size[0], player.obj.size[1]))
            ball_rect = pygame.Rect((self.obj.pos[0] - 5, self.obj.pos[1] - 5),
                                    (self.obj.radius * 2, self.obj.radius * 2))

            if player_rect.colliderect(ball_rect):
                self.speed[0] = -self.speed[0]

        self.obj.pos[0] += self.speed[0] * Time.DT
        self.obj.pos[1] += self.speed[1] * Time.DT


class Game:
    def __init__(self):
        self.score = [0,0]
        self.paused = [False]
        self.framerate = 10000

        self.recs = [Rec([75, 400], [25, 150], [0, 0, 0]), Rec([1000, 400], [25, 150], [0, 0, 0]),  # Player recs
                     Rec([0, 0], [1600, 50], [50, 50, 50]), Rec([1100, 50], [500, 850], [50, 50, 50]),  # Hud recs
                     Rec([0, 50], [20, 850], [225, 225, 225]), Rec([1080, 50], [20, 850], [225, 225, 225])]  # Goal recs

        self.circles = [Circ([550, 475], 10, [0, 0, 0])]  # Alll the players

        self.paused = [True]

        self.players = [Player(self.recs[0], [npt.Keys.W, npt.Keys.S], 700),
                        Player(self.recs[1], [npt.Keys.P, npt.Keys.L], 700)]

        self.balls = [Game_ball(self.circles[0])]

        self.text = [Text('P1 Commands : W S', [10, 15]), Text('P1 Commands : P L', [895, 15]),
                     Text('P1 Score:', [300, 15]), Text(self.score[0], [410, 15]),
                     Text('P2 Score:', [650, 15]), Text(self.score[1], [760, 15]),
                     Text('W :', [1110, 50]), Text(npt.Keys.W.pressed, [1140, 50]),
                     Text('S :', [1110, 70]), Text(npt.Keys.S.pressed, [1140, 70]),
                     Text('P :', [1110, 90]), Text(npt.Keys.P.pressed, [1140, 90]),
                     Text('L :', [1110, 110]), Text(npt.Keys.L.pressed, [1140, 110]),
                     Text('Player 1:', [1110, 130]), Text(self.recs[0].pos, [1220, 130]),
                     Text('Player 2:', [1110, 150]), Text(self.recs[1].pos, [1220, 150]),
                     Text('Ball colliding:', [1110, 170]), Text(self.balls[0].colliding[0], [1290, 170])
                     ]

        self.test_stage()

    def test_stage(self):
        while True:
            Time.clock.tick(self.framerate)
            Time.update()
            Methods.quit()
            npt.update()

            print(self.balls[0].colliding[0])
            self.update()
            Screen.update(self.recs, self.circles, self.text)

    def update(self):
        if Time.now - Time.start_time >= 1:
            self.paused[0] = False
        if not self.paused[0]:
            for player in self.players:
                player.update()
            for ball in self.balls:
                ball.update(self.players)
                # if npt.Keys.SPACE:
                #    self.paused = True
                #
                #    self.paused = False


if __name__ == '__main__':
    game = Game()

