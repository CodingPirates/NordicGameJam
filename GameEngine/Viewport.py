import pygame
import player

class Viewport:
    def __init__(self, scene):
        self.player = None
        self.scene = scene
        self.position = (0, 0)

    def findPlayer(self):
        # locate player element on scene
        for curElement in self.scene.getElements():
            if(isinstance(curElement, player.Player)):
                self.player=curElement
                break

        if(self.player is None):
            raise Exception("No player element found on scene")

    def render(self, deltaTime, display):
        # make sure we know the player
        if(self.player is None):
            self.findPlayer()

        viewportSize = display.get_size()

        # set position to center on player
        self.position = self.player.getPosition()
        self.position = (self.position[0] - viewportSize[0] / 2, self.position[1] - viewportSize[1] / 2)

        # stay inside scene
        if(self.position[0] < 0):
            self.position = (0, self.position[1])
        elif(self.position[0] + viewportSize[0] > self.scene.getSize()[0]):
            self.position = (self.scene.getSize()[0] - viewportSize[0], self.position[1])
        if(self.position[1] < 0):
            self.position = (self.position[0], 0)
        elif(self.position[1] + viewportSize[1] > self.scene.getSize()[1]):
            self.position = (self.position[0], self.scene.getSize()[1] - viewportSize[1])

        # iterate all elements and draw them on the screen
        for element in self.scene.getElements():
            display.blit(element.getSurface(), element.getRect())
