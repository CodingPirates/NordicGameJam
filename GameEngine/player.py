import pygame, sys, Element

class Player (Element.Element):

    def __init__(self, xPos, yPos, size, image, layer):

        # The player controls, no keyboard handling is done n this class all
        self.movementAcc = 2
        self.jumpHeight = 4
        self.movementSpeed = 0
        self.maxSpeed = 5
        self.control = 0
        self.animMode = "still"

        self.animRightImages = [pygame.image.load ('Graphics/Player/anim/right_walk/player_right_walk01.png').convert()]
        self.animRightImages.append(pygame.image.load ('Graphics/Player/anim/right_walk/player_right_walk02.png').convert())
        self.animRightImages.append(pygame.image.load ('Graphics/Player/anim/right_walk/player_right_walk03.png').convert())
        self.animRightImages.append(pygame.image.load ('Graphics/Player/player_break01_right.png').convert())

        self.animLeftImages = [pygame.image.load ('Graphics/Player/anim/left_walk/player_left_walk01.png').convert()]
        self.animLeftImages.append(pygame.image.load ('Graphics/Player/anim/left_walk/player_left_walk02.png').convert())
        self.animLeftImages.append(pygame.image.load ('Graphics/Player/anim/left_walk/player_left_walk03.png').convert())
        self.animLeftImages.append(pygame.image.load ('Graphics/Player/player_break01_left.png').convert())

        super(Player, self).__init__(xPos, yPos, size, image, layer)

    def anim (self, deltaTime):
        if self.movementSpeed > 0:
            if self.control == -1:
                self.anim = "rightStop"
            else:
                self.anim = "right"
        elif self.movementSpeed < 0:
            if self.control == 1:
                self.anim = "leftStop"
            else:
                self.anim = "left"
        
    def updatePos(self, deltaTime):
        if self.movementSpeed < 0.1 and self.movementSpeed > -0.1:
            self.movementSpeed = 0
            self.movementSpeed += self.movementAcc * deltaTime * self.control
        if self.movementSpeed > self.maxSpeed:
            self.vmovementSpeed = 5
        elif self.movementSpeed < -self.maxSpeed:
            self.movementSpeed = -5
            setPosition(getPostion()[0]+self.movementSpeed, getPostion()[1])

    def tick(self, deltaTime, keyEvent=False):
        self.anim(deltaTime)
        self.updatePos(deltaTime)
