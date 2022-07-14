import pygame
from pygame import QUIT


class Start:
    @staticmethod
    def start():
        Handler.create_obj(70, 70)
        Handler.create_obj(100, 100)

        Main.mainloop()


class Events:
    @staticmethod
    def quit():
        for Event in pygame.event.get():
            if Event.type == QUIT:
                pygame.quit()
                exit()


class Window:
    windowx = 1280
    windowy = 720
    window = pygame.display.set_mode((windowx, windowy))


class Render:

    @staticmethod
    def obj():
        for obj in Handler.objwheel:
            obj.draw()

    @staticmethod
    def render():
        Window.window.fill((255, 255, 255))
        Render.obj()
        pygame.display.update()


class Main:
    clock = pygame.time.Clock()

    @staticmethod
    def mainloop():
        while True:
            # Main start
            Main.clock.tick(60)
            Events.quit()
            # Stuff
            Collision.collisions()
            # Final
            Render.render()

class Collision:
    @staticmethod
    def sword_enemy():
        for obj in Handler.objwheel:
            self_rect = pygame.Rect((obj.pos[0], obj.pos[1]),(10,10))
            other_rect = pygame.Rect((obj.pos[0], obj.pos[1]+100),(10,10))
            if self_rect.colliderect(other_rect):
                print('a')

    @staticmethod
    def collisions():
        Collision.sword_enemy()
class Obj:
    def __init__(self, posx, posy):
        print(f'obj number  : {Handler.objcount + 1}')
        self.color = (151, 151, 151)
        self.pos = [posx, posy]

    def draw(self):
        pygame.draw.rect(Window.window, self.color, (self.pos[0], self.pos[1], 20, 20))


class Handler:
    objcount = 0
    objwheel = []

    @staticmethod
    def create_obj(posx, posy):
        Handler.objwheel.append(Handler.objcount)
        Handler.objwheel[Handler.objcount] = Obj(posx, posy)
        Handler.objcount += 1


if __name__ == '__main__':
    Start.start()
