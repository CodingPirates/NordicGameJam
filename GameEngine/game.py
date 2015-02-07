#!/usr/bin/env python
# Encoding: UTF-8
#
# Obvious til Coding Pirates

from __future__ import unicode_literals
import random
import math
import pygame

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

pygame.mixer.init()

while not ended:
    # Tik ti gange i sekundet
    clock.tick(15)
    
    # Udfyld skærmen med hvid
    screen.fill([0,0,0])
    
    pygame.display.flip()
    
pygame.quit()
