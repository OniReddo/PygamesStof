import pygame


class Key:
    @property
    def __repr__(self):  # Print
        return self.key

    def __eq__(self, other):  # If key equals X
        if self.key == str(other):
            return True

    def __bool__(self):  # If key is pressed
        if self.pressed:
            return True
        else:
            return False

    def __init__(self, key):
        self.key = key
        self.ascii_key = ord(key)
        self.holding = False
        self.pressed = False

        print('created key :', key.upper())


class Keys:
    W = Key('w')
    A = Key('a')
    S = Key('s')
    D = Key('d')

    SPACE = Key(' ')

    keys = [W, A, S, D, SPACE]

    @classmethod
    def update(cls):
        for key in cls.keys:
            if pygame.key.get_pressed()[key.ascii_key]:
                key.pressed = True
            else:
                key.pressed = False


class Mouse:
    @classmethod
    def status(cls):
        return f'Mouse at: {cls.pos} | LMB, RMB: {cls.left_mb},{cls.right_mb}'

    pos = [0, 0]
    left_mb = False
    right_mb = False

    @classmethod
    def update(cls):
        cls.pos[0] = pygame.mouse.get_pos()[0]
        cls.pos[1] = pygame.mouse.get_pos()[1]

        if pygame.mouse.get_pressed()[0]:
            cls.left = True
        else:
            cls.left = False
        if pygame.mouse.get_pressed()[2]:
            cls.right = True
        else:
            cls.right = False



def update():
    Keys.update()
    Mouse.update()
