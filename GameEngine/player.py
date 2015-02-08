import pygame, sys, Element

class Player (Element):

    # The player controls, no keyboard handling is done n this class all
    movementAcc = 2
    jumpHeight = 4
    movementSpeed = 0
    maxSpeed = 5
    control = 0
    animMode = "still"

    def anim (deltaTime):
        if movementSpeed > 0:
            if control == -1:
                anim = "rightStop"
            else
                anim = "right"
        elif movementSpeed < 0:
            if control == 1:
                anim = "leftStop"
            else
                anim = "left"
        
        animRightImages [0] = pygame.image.load ('/Graphics/Player/anim/right_walk/player_right_walk01.png')
        animRightImages [1] = pygame.image.load ('/Graphics/Player/anim/right_walk/player_right_walk02.png')
        animRightImages [2] = pygame.image.load ('/Graphics/Player/anim/right_walk/player_right_walk03.png')
        animRightImages [3] = pygame.image.load ('/Graphics/Player/player_break01_right')

        animLeftImages [0] = pygame.image.load ('/Graphics/Player/anim/left_walk/player_left_walk01.png')
        animLeftImages [1] = pygame.image.load ('/Graphics/Player/anim/left_walk/player_left_walk02.png')
        animLeftImages [2] = pygame.image.load ('/Graphics/Player/anim/left_walk/player_left_walk03.png')
        animLeftImages [3] = pygame.image.load ('/Graphics/Player/player_break01_left')

    def updatePos(deltaTime):
        if movementSpeed < 0.1 && movementSpeed > -0.1:
        movementSpeed = 0
        movementSpeed += movementAcc * deltaTime * control
        if movementSpeed > maxSpeed:
            movementSpeed = 5
        elif movementSpeed < -maxSpeed:
        movementSpeed = -5
        setPosition(getPostion()[0]+movementSpeed, getPostion()[1])

    def tick(deltaTime, keyEvent=False):
        self.anim(deltaTime)
        self.updatePos(deltaTime)