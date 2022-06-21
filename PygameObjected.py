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
        # Some asset declaration right up before game starts
        Player.createplayer()
        Text.createtext(Input.playerinput, 50, 50)
        Text.createtext(' W  S  A  D', 50, 20)
        # Problem is here
        Text.createtext(Player.playerwheel[0].posx, 500, 20)
        Text.createtext(Player.playerwheel[0].posy, 500, 50)
        Game.main()
        # text = str(Player.playerwheel[0].pposx)
        # surface = Text.textfont.render(text,True,(0, 0, 0))
        # Window.window.blit(surface,(20,100))


class Game:
    clock = pygame.time.Clock()

    @staticmethod
    def main():
        while True:
            Game.clock.tick(60)
            Methods.quit()
            Input.player()
            Physics.playerphys()
            Render.render()


class Player:
    playercount = 0
    playerwheel = []

    @staticmethod
    def createplayer():
        Player.playerwheel.append(Player.playercount)
        Player.playerwheel[Player.playercount] = Player()
        Player.playercount += 1

    def __init__(self):
        self.posx = 200
        self.posy = 200
        self.spdx = 0
        self.spdy = 0
        self.color = (0, 0, 0)

    def draw(self):
        pygame.draw.rect(Window.window, self.color, (self.posx, self.posy, 10, 10))


class Input:
    playerinput = [False, False, False, False]

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
        else:
            Input.playerinput[2] = False
        # D
        if pygame.key.get_pressed()[K_d]:
            if not Input.playerinput[2]:
                Input.playerinput[3] = True
        else:
            Input.playerinput[3] = False


class Physics:
    @staticmethod
    def playerphys():


        if Player.playerwheel[0].spdx > 10:
            Player.playerwheel[0].spdx = 10
        elif if Player.playerwheel[0].spdx < -10:
            if Player.playerwheel[0].spdx = -10









class Text:
    textfont = pygame.font.SysFont("monospace", 20)
    textcount = 0
    textwheel = []

    @staticmethod
    def createtext(text, posx, posy):
        Text.textwheel.append(Text.textcount)
        Text.textwheel[Text.textcount] = Text(text, posx, posy)
        Text.textcount += 1

    def __init__(self, text, posx, posy):
        self.path = text
        self.text = str(text)
        self.texposx = posx
        self.texposy = posy
        self.surface = Text.textfont.render(self.text, True, (0, 0, 0))

    # Problem is also here
    @staticmethod
    def txtupd():
        for textnum in Text.textwheel:
            textnum.text = str(textnum.path)
            textnum.surface = Text.textfont.render(textnum.text, True, (0, 0, 0))
            Window.window.blit(textnum.surface, (textnum.texposx, textnum.texposy))


class Render:
    @staticmethod
    def render():
        Window.window.fill((255, 255, 255))
        Player.playerwheel[0].draw()
        Text.txtupd()

        text = str(Player.playerwheel[0].posx)
        surface = Text.textfont.render(text, True, (0, 0, 0))
        Window.window.blit(surface, (20, 100))

        pygame.display.update()


if __name__ == '__main__':
    Start.start()