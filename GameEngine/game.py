#!/usr/bin/env python
# Encoding: UTF-8
#
# Space Invaders til Coding Pirates

from __future__ import unicode_literals
import random
import math
import pygame

# Skærmstørrelse
screen_width = 900
screen_height = 600

# Start pygame
pygame.init()

# Skærmstørrelse
screen = pygame.display.set_mode(
    [screen_width, screen_height])

pygame.display.set_caption('Obvious!')

slut = False
clock = pygame.time.Clock()

pygame.mixer.init()

while not slut:
    # Tik ti gange i sekundet
    clock.tick(15)
    
    # Udfyld skærmen med hvid
    screen.fill([0,0,0])
    
    pygame.display.flip()
    
pygame.quit()
