import pygame

class Viewport:
    def __init__(self, player):
        self.player = player

    def getSurface(self):
        return pygame.Surface((100, 100))
