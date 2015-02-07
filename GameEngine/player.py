import pygame, sys

# The player controls, no keyboard handling is done n this class all
movementSpeed = 2
jumpHeight    = 4

def moveRight():
    pos = getPostion()
    pos[0] += movementSpeed
    setPostion(pos)

def moveLeft():
    pos = getPostion()
    pos[0] -= movementSpeed
    setPostion()




#def jump():
