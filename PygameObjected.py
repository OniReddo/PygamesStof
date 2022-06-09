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
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()


class Start:
    @staticmethod
    def start():
        # Stuff declaration right before game startup
        global player1, text1
        player1 = Player()
        Text.createtext(Input.playerinput, 50, 50)
        Text.createtext(' W  S  A  D', 50, 20)
        Game.main()


class Game:
    clock = pygame.time.Clock()

    @staticmethod
    def main():
        while True:
            Game.clock.tick(60)
            Methods.quit()
            Input.player()
            Render.render()


class Player:
    def __init__(self):
        self.posx = 200
        self.posy = 200
        self.color = (0, 0, 0)

    def draw(self):
        pygame.draw.rect(Window.window, self.color, (self.posx, self.posy, 10, 10))


class Input:
    playerinput = [0, 0, 0, 0]

    @staticmethod
    def player():
        # Up
        if pygame.key.get_pressed()[K_w]:
            Input.playerinput[0] = 1
        else:
            Input.playerinput[0] = 0
        # Down
        if pygame.key.get_pressed()[K_s]:
            Input.playerinput[1] = 1
        else:
            Input.playerinput[1] = 0
        # Left
        if pygame.key.get_pressed()[K_a]:
            Input.playerinput[2] = 1
        else:
            Input.playerinput[2] = 0
        # Right
        if pygame.key.get_pressed()[K_d]:
            Input.playerinput[3] = 1
        else:
            Input.playerinput[3] = 0


class Physics:
    @staticmethod
    def playerphys():
        pass


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
        self.posx = posx
        self.posy = posy
        self.surface = Text.textfont.render(self.text, 1, (0, 0, 0))

    @staticmethod
    def txtupd():
        for text in Text.textwheel:
            text.text = str(text.path)
            text.surface = Text.textfont.render(text.text, 1, (0, 0, 0))
            Window.window.blit(text.surface, (text.posx, text.posy))


class Render:
    @staticmethod
    def render():
        Window.window.fill((255, 255, 255))
        player1.draw()
        Text.txtupd()
        #       textfont = pygame.font.SysFont("monospace",20)
        #       text = str(Input.playerinput)
        #       Texttr = textfont.render(text,1,(0,0,0))
        #       Window.window.blit(Texttr,(50,50))

        pygame.display.update()


Start.start()
