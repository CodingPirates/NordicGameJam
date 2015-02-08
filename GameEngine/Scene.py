import Element
import player
import pygame
import Viewport

class Scene():
    def __init__(self):
        # empty list of elements
        playerImage = pygame.image.load('./Graphics/Player/player_standing.png')
        playerImage = playerImage.convert()
        thePlayer = player.Player(20, 60, playerImage.get_size(), playerImage, 11)
        self.elements = [thePlayer]
        self.viewport = Viewport.Viewport(thePlayer, self)

    def addElement(self, element):
        element.setScene(this)
        this.elements.add(element)

    def removeElement(self, element):
        elements.remove(element)

    def getSurface(self):
        return self.viewport.getSurface()

    def tick(self, deltaTime, keyEvent=False):
        # iterate over all elements and update their state
        for currentElement in self.elements:
            currentElement.tick(deltaTime)

    def control(self, event):
        # iterate over all elements and update their state
        for currentElement in self.elements:
            currentElement.tick(deltaTime, keyEvent)
