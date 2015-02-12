#!/usr/bin/env python
# Encoding: UTF-8
#
# Obvious til Coding Pirates

from __future__ import unicode_literals
import random
import math
import pygame
import Scene
import sys
import player
import Element
import time

class runGame:
    def __init__(self):
        # Screen size
        screen_width = 1024
        screen_height = 768

        # Screen size
        self.screen = pygame.display.set_mode([screen_width, screen_height])

        pygame.mixer.init()

        # Start pygame
        pygame.init()

        pygame.display.set_caption('Obvious!')

        self.scene = Scene.Scene()
        self.ended = False
        self.clock = pygame.time.Clock()

    def loadFromImage(self,filename):
        print("Loading level: " + filename)
        try:
            image = pygame.image.load(filename)
        except (pygame.error, message):
            print ("Cannot load image: " + filename)
            raise SystemExit(message)

        print("Dimension: " + str(image.get_size()))

        for y in range(0, image.get_height()):
            for x in range(0, image.get_width()):
                location = (x, y)
                color = image.get_at(location)

                if color == pygame.Color(255, 255, 255, 255):
                    continue

                # player
                elif color == pygame.Color(0, 255, 255, 255):
                    Elementimage = pygame.image.load ('Graphics/Player/player_standing.png').convert()
                    self.scene.addElement(player.Player(location, Elementimage.get_size(), Elementimage, 11))

                # block1_top
                elif color == pygame.Color(255, 240, 0, 255):
                    ElementImage = pygame.image.load ('Graphics/Blocks/block1/block1_mid_grass.png').convert()
                    self.scene.addElement(Element.Element(location, ElementImage.get_size(), ElementImage, 11))

                # block1_dirt
                elif color == pygame.Color(255, 0, 0, 255):
                    ElementImage = pygame.image.load ('Graphics/Blocks/block1/block1_dirt.png').convert()
                    self.scene.addElement(Element.Element(location, ElementImage.get_size(), ElementImage, 11))

                # block1_right
                elif color == pygame.Color(170, 240, 0, 255):
                    ElementImage = pygame.image.load ('Graphics/Blocks/block1/block1_right_grass.png').convert()
                    self.scene.addElement(Element.Element(location, ElementImage.get_size(), ElementImage, 11))

                # block1_right_side
                elif color == pygame.Color(221, 221, 221, 255):
                    ElementImage = pygame.image.load ('Graphics/Blocks/block1/block1_right_grass_side.png').convert()
                    self.scene.addElement(Element.Element(location, ElementImage.get_size(), ElementImage, 11))

                # block1_left
                elif color == pygame.Color(0, 0, 255, 255):
                    ElementImage = pygame.image.load ('Graphics/Blocks/block1/block1_left_grass.png').convert()
                    self.scene.addElement(Element.Element(location, ElementImage.get_size(), ElementImage, 11))

                # block1_left_side
                #elif color == pygame.Color(0, 255, 255, 255):
                #    ElementImage = pygame.image.load ('Graphics/Blocks/block1/block1_left_grass_side.png').convert()
                #    self.scene.addElement(Element.Element(location, ElementImage, ElementImage.get_size(), 11))

                # block2
                elif color == pygame.Color(0, 0, 0, 255):
                    ElementImage = pygame.image.load ('Graphics/Blocks/block2/block2.png').convert()
                    self.scene.addElement(Element.Element(location, ElementImage.get_size(), ElementImage, 11))

                else:
                    print ("WARNING: unknow blocktype on position " + str(location) + " color was: " + str(color))

    def start(self):

        self.loadFromImage("Levels/1.png")

        while not self.ended:
            # Run 30 fps
            self.clock.tick(30)
            deltaTime = self.clock.get_time()

            if pygame.event.peek():
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                       pygame.quit ()
                       sys.exit ()

                    self.scene.tick(deltaTime, event)
            else:
                # no events - just update elements
                self.scene.tick(deltaTime)

            # Render screen
            self.scene.render(deltaTime, self.screen)

            # Update double buffered screen
            pygame.display.flip()



game = runGame()
game.start()
