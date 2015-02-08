#!/usr/bin/env python
# Encoding: UTF-8
#
# Obvious til Coding Pirates

from __future__ import unicode_literals
import random
import math
import pygame
import Scene

class runGame:
    def __init__(self):
        # Screen size
        screen_width = 1024
        screen_height = 768

        # Size of block
        sizeOfBlock = 32

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
        try:
            image = pygame.image.load(filename)
        except pygame.error, message:
            print "Cannot load image: ", filename
            raise SystemExit, message

            for y in range(1, image.get_height(), sizeOfBlock):
                for x in range(1, image.get_width(), sizeOfBlock):
                    color = image.get_at((x, y))
                    location = [x, y]

                    # block1_top
                    if color == pygame.Color(255, 240, 0, 0):
                        dummy = False

                    # block1_dirt
                    elif color == pygame.Color(255, 0, 0, 0):
                        dummy = False

                    # block1_right
                    elif color == pygame.Color(174, 140, 0, 0):
                        dummy = False

                    # block1_right_side
                    elif color == pygame.Color(211, 211, 211, 0):
                        dummy = False

                    # block1_left
                    elif color == pygame.Color(0, 0, 255, 0):
                        dummy = False

                    # block1_left_side
                    elif color == pygame.Color(0, 255, 255, 0):
                        dummy = False

                    # block2
                    elif color == pygame.Color(0, 0, 0, 0):
                        dummy = False

    def start(self):

        self.loadFromImage("Levels/1.png")

        while not self.ended:
            # Run 30 fps
            self.clock.tick(30)
            deltaTime = self.clock.get_time()

            if pygame.event.peek():
                for event in pygame.event.get():
                    self.scene.tick(deltaTime, event)
            else:
                # no events - just update elements
                self.scene.tick(deltaTime)

            # Clear screen
            self.screen.blit(self.scene.getSurface(), (0,0))

            # Update double buffered screen
            pygame.display.flip()



game = runGame()

game.start()
