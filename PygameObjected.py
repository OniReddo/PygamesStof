import random

import pygame.display
from pygame import *

pygame.init()


class Window:
    windowx = 1280
    windowy = 720
    window = pygame.display.set_mode((windowx, windowy))


class Methods:
    @staticmethod
    def quit():
        for Event in pygame.event.get():
            if Event.type == QUIT:
                pygame.quit()
                exit()


class Start:
    @staticmethod
    def start():
        Player.createplayer()
        Sword.create()

        Enemy.create()
        Enemy.create()
        Enemy.create()
        Enemy.create()
        Enemy.create()
        Enemy.create()
        Enemy.create()
        Enemy.create()

        Text.createtext(Input.playerinput, 50, 50)
        Text.createtext(' W  S  A  D', 50, 20)
        Text.createtext(Player.playerwheel[0].pos, 500, 20)
        Text.createtext(Player.playerwheel[0].spd, 500, 50)
        Text.createtext(Enemy.enemywheel[0].pos, 500, 70)
        Game.main()


class Game:
    clock = pygame.time.Clock()

    @staticmethod
    def main():
        while True:
            Game.clock.tick(60)
            Methods.quit()
            Collisions.sword()
            Input.player()
            Physics.playerphys()
            Enemy.chase()
            Render.render()


class EnemyOBJ:
    def __init__(self):
        print('criado')
        self.color = (255,0,0)
        self.pos = [random.randint(1,500), random.randint(1,500)]

    def draw(self):
        pygame.draw.rect(Window.window, self.color, (self.pos[0], self.pos[1], 10, 10))

class Enemy:
    enemycount = 0
    enemywheel = []

    @staticmethod
    def create():
        Enemy.enemywheel.append(Enemy.enemycount)
        Enemy.enemywheel[Enemy.enemycount] = EnemyOBJ()
        Enemy.enemycount += 1

    @staticmethod
    def chase():
        spd = 6
        for enemy in Enemy.enemywheel:
            disx = Player.playerwheel[0].pos[0] - enemy.pos[0]
            disy = Player.playerwheel[0].pos[1] - enemy.pos[1]

            print(enemy.pos)

            if abs(disx) <= spd:
                enemy.pos[0] = Player.playerwheel[0].pos[0]
                disx = Player.playerwheel[0].pos[0] - enemy.pos[0]

            if abs(disy) <= spd:
                enemy.pos[1] = Player.playerwheel[0].pos[1]
                disy = Player.playerwheel[0].pos[1] - enemy.pos[1]

            if disx != 0:
                enemy.pos[0] += spd * ( disx / abs( disx ))
            if disy != 0:
                enemy.pos[1] += spd * ( disy / abs(disy))



class Player:
    playercount = 0
    playerwheel = []

    @staticmethod
    def createplayer():
        Player.playerwheel.append(Player.playercount)
        Player.playerwheel[Player.playercount] = Player()
        Player.playercount += 1

    def __init__(self):
        self.pos = [200,200]
        self.spd = [0, 0]
        self.color = (0, 0, 0)

    def draw(self):
        pygame.draw.rect(Window.window, self.color, (self.pos[0], self.pos[1], 10, 10))


class Sword:
    swordcount = 0
    swordwheel = []

    @staticmethod
    def create():
        Sword.swordwheel.append(Sword.swordcount)
        Sword.swordwheel[Sword.swordcount] = Sword()
        Sword.swordcount += 1

    def __init__(self):
        self.color = (0,0,255)
        self.swordpos = Player.playerwheel[0].pos[0]

    def draw(self):
        pygame.draw.rect(Window.window, (0, 255, 255), (self.swordpos, Player.playerwheel[0].pos[1], 20, 10))

class Input:
    playerinput = [False, False, False, False]
    isflipped = False

    @staticmethod
    def player():
        # W
        if pygame.key.get_pressed()[K_w]:
            if not Input.playerinput[1]:
                Input.playerinput[0] = True
        else:
            Input.playerinput[0] = False
        # S
        if pygame.key.get_pressed()[K_s]:
            if not Input.playerinput[0]:
                Input.playerinput[1] = True
        else:
            Input.playerinput[1] = False
        # A
        if pygame.key.get_pressed()[K_a]:
            if not Input.playerinput[3]:
                Input.playerinput[2] = True
                Input.isflipped = True
        else:
            Input.playerinput[2] = False
        # D
        if pygame.key.get_pressed()[K_d]:
            if not Input.playerinput[2]:
                Input.playerinput[3] = True
                Input.isflipped = False
        else:
            Input.playerinput[3] = False
        if pygame.key.get_pressed()[K_SPACE]:
            for enemy in Enemy.enemywheel:
                enemy.pos = [random.randint(1,1280), random.randint(1,720)]


class Physics:
    plyrslowdownx = 0.5
    plyrslowdowny = 0.5

    plyrspdboostx = 2
    plyrspdboosty = 2

    @staticmethod
    def playerphys():
        # Placeholder
        # Y Speedbreaker limit
        if Player.playerwheel[0].spd[1] > 10:
            Player.playerwheel[0].spd[1] = 10
        elif Player.playerwheel[0].spd[1] < -10:
            Player.playerwheel[0].spd[1] = -10
        # X Speedbreaker limit
        if Player.playerwheel[0].spd[0] > 10:
            Player.playerwheel[0].spd[0] = 10
        elif Player.playerwheel[0].spd[0] < -10:
            Player.playerwheel[0].spd[0] = -10

        # Player input force
        if Input.playerinput[0]:
            Player.playerwheel[0].spd[1] -= Physics.plyrspdboosty
        if Input.playerinput[1]:
            Player.playerwheel[0].spd[1] += Physics.plyrspdboosty
        if Input.playerinput[2]:
            Player.playerwheel[0].spd[0] -= Physics.plyrspdboostx
        if Input.playerinput[3]:
            Player.playerwheel[0].spd[0] += Physics.plyrspdboostx

        # Add Friction
        # Y
        if Player.playerwheel[0].spd[1] > 0:
            Player.playerwheel[0].spd[1] -= Physics.plyrslowdowny
        elif Player.playerwheel[0].spd[1] < 0:
            Player.playerwheel[0].spd[1] += Physics.plyrslowdowny
        # X
        if Player.playerwheel[0].spd[0] > 0:
            Player.playerwheel[0].spd[0] -= Physics.plyrslowdownx
        elif Player.playerwheel[0].spd[0] < 0:
            Player.playerwheel[0].spd[0] += Physics.plyrslowdownx

        # Change playerpos after physics
        Player.playerwheel[0].pos[1] += Player.playerwheel[0].spd[1]
        Player.playerwheel[0].pos[0] += Player.playerwheel[0].spd[0]

        if Input.isflipped == False :
            Sword.swordwheel[0].swordpos = Player.playerwheel[0].pos[0] + 20
        if Input.isflipped:
            Sword.swordwheel[0].swordpos = Player.playerwheel[0].pos[0] - 30

class Collisions:
    @staticmethod
    def sword():
        for enemy in Enemy.enemywheel:
           pass




class Text:
    textfont = pygame.font.SysFont("monospace", 20)
    textcount = 0
    textwheel = []

    @staticmethod
    def createtext(text, posx, posy, house=None):
        Text.textwheel.append(Text.textcount)
        Text.textwheel[Text.textcount] = Text(text, posx, posy, house)
        Text.textcount += 1

    def __init__(self, text, posx, posy, house=None):
        self.path = text
        self.text = str(self.path)
        self.texposx = posx
        self.texposy = posy
        self.house = house
        self.surface = Text.textfont.render(self.text, True, (0, 0, 0))

    @staticmethod
    def txtupd():
        for textnum in Text.textwheel:
            textnum.text = str(textnum.path)
            textnum.surface = Text.textfont.render(textnum.text, True, (0, 0, 0))
            Window.window.blit(textnum.surface, (textnum.texposx, textnum.texposy))


class Render:
    @staticmethod
    def objects():
        for enemy in Enemy.enemywheel:
            enemy.draw()
        for sword in Sword.swordwheel:
            sword.draw()
        for player in Player.playerwheel:
            player.draw()


    @staticmethod
    def render():
        Window.window.fill((255, 255, 255))
        Player.playerwheel[0].draw()
        Render.objects()
        Text.txtupd()
        pygame.display.update()


if __name__ == '__main__':
    Start.start()
    # Ta funcionano omagod
