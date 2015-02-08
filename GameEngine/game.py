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
    # Screen size
    screen_width = 1024
    screen_height = 768

    # Size of block
    sizeOfBlock = 32

    # Screen size
    screen = pygame.display.set_mode([screen_width, screen_height])

    def __init__(self):
        # Start pygame
        pygame.init()

        pygame.display.set_caption('Obvious!')

        ended = False
        clock = pygame.time.Clock()

        scene = Scene()

        pygame.mixer.init()

        loadFromImage("Levels/1.png")

        while not ended:
            # Run 30
            clock.tick(30)

            # Clear screen
            screen.fill([0,0,0])
            screen.blit(pygame.image.load('back.png'), (0,0))

            screen.blit(pygame.image.load('mario.png'), (100,500))
            # Update double buffered screen
            pygame.display.flip()

        pygame.quit()


    def loadFromImage(filename):
        try:
            image = pygame.image.load(filename)
        except pygame.error, message:
            print "Cannot load image: ", filename
            raise SystemExit, message

            for y in range(1, image.get_height(), sizeOfBlock):
                for x in range(1, image.get_width(), sizeOfBlock):
                    color = image.get_at((x, y))
                    location = [x, y]

                    print str(color)
                    print str(location)

                    # block1_top
                    if color == pygame.Color(255, 240, 0, 0):

                    # block1_dirt
                    elif color == pygame.Color(255, 0, 0, 0):

                    # block1_right
                    elif color == pygame.Color(174, 140, 0, 0):

                    # block1_right_side
                    elif color == pygame.Color(211, 211, 211, 0):

                    # block1_left
                    elif color == pygame.Color(0, 0, 255, 0):

                    # block1_left_side
                    elif color == pygame.Color(0, 255, 255, 0):



#loadFromImage("/Users/dsdeniso/Documents/GitHub/discourse/public/images/emoji/apple/-1.png")

game = runGame()

game.start()
