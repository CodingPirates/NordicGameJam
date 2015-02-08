#!/usr/bin/env python
# Encoding: UTF-8
#
# Obvious til Coding Pirates

from __future__ import unicode_literals
import random
import math
import pygame
import Scene

# Screen size
screen_width = 900
screen_height = 600

# Start pygame
pygame.init()

# Screen size
screen = pygame.display.set_mode(
    [screen_width, screen_height])

pygame.display.set_caption('Obvious!')

ended = False
clock = pygame.time.Clock()

scene = Scene.Scene()

pygame.mixer.init()

while not ended:
    # Run 30 fps
    clock.tick(30)
    deltaTime = clock.get_time()

    if pygame.event.peek():
        for event in pygame.event.get():
            scene.tick(deltaTime, event)
    else:
        # no events - just update elements
        scene.tick(deltaTime)

    # Clear screen
    screen.blit(scene.getSurface(), (0,0))

    # Update double buffered screen
    pygame.display.flip()

pygame.quit()
