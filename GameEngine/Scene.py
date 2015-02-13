import Element
import player
import pygame
import Viewport

class Scene():
    def __init__(self):
        # empty list of elements
        self.elements = []
        self.viewport = Viewport.Viewport(self)

    def addElement(self, element):
        element.setScene(self)
        self.elements.append(element)

        def layerSort(element):
            return element.getLayer()

        # keep elements sorted in layer order
        self.elements.sort(key=layerSort)

        print("added element at " + str(element.getPosition()))

    def removeElement(self, element):
        elements.remove(element)

    def getElements(self):
        return self.elements

    def getSize(self):
        return (2048, 768)

    def render(self, deltaTime, display):
        return self.viewport.render(deltaTime, display)

    def tick(self, deltaTime, keyEvent=False):
        # iterate over all elements and update their state
        for currentElement in self.elements:
            currentElement.tick(deltaTime, keyEvent)

