import pygame, sys, Element

class Player (Element.Element):

    def __init__(self, position, size, image, layer):

        # The player controls, no keyboard handling is done n this class all
        self.movementAcc = 0.02
        self.jumpHeight = 4.0
        self.movementSpeed = 0.0
        self.maxSpeed = 6.0
        self.control = 0
        self.friction = 7.0
        self.animMode = "none"
        self.animClock = 0.0

        self.animRightImages = [pygame.image.load ('Graphics/Player/anim/right_walk/player_right_walk01.png').convert()]
        self.animRightImages.append(pygame.image.load ('Graphics/Player/anim/right_walk/player_right_walk02.png').convert())
        self.animRightImages.append(pygame.image.load ('Graphics/Player/anim/right_walk/player_right_walk03.png').convert())
        
        self.animLeftImages = [pygame.image.load ('Graphics/Player/anim/left_walk/player_left_walk01.png').convert()]
        self.animLeftImages.append(pygame.image.load ('Graphics/Player/anim/left_walk/player_left_walk02.png').convert())
        self.animLeftImages.append(pygame.image.load ('Graphics/Player/anim/left_walk/player_left_walk03.png').convert())

        self.animBreakLeft = pygame.image.load ('Graphics/Player/player_break01_left.png').convert()
        self.animBreakRight = pygame.image.load ('Graphics/Player/player_break01_right.png').convert()
        #self.animStandingStill = pygame.ingame.load('Graphics/Player/player_standing.png').convert()

        super(Player, self).__init__(position, size, image, layer)

    def anim (self, deltaTime):
        if self.movementSpeed > 0:
            if self.control == -1:
                self.image = self.animBreakRight
                self.animMode = "none"
            else:
                self.animMode = "right"
        elif self.movementSpeed < 0:
            if self.control == 1:
                self.image = self.animBreakLeft
                self.animMode = "none"
            else:
                self.animMode = "left"
        else:
            self.animMode = "none"
            #self.image = self.animStandingStill
        
        self.animClock += self.movementSpeed*deltaTime/200.0
        self.animClock = self.animClock%3
        if self.animMode == "right":
            self.image = self.animRightImages[int(self.animClock)]
        elif self.animMode == "left":
            self.image = self.animLeftImages[int(self.animClock)]
            
            

    def updatePos(self, deltaTime):
        if self.movementSpeed < 0.1 and self.movementSpeed > -0.1:
            self.movementSpeed = 0

        self.movementSpeed += self.movementAcc * deltaTime * self.control

        if self.movementSpeed > self.maxSpeed:
            self.movementSpeed = 5
        elif self.movementSpeed < -self.maxSpeed:
            self.movementSpeed = -5
        
        print(self.movementSpeed)    
        self.setPosition((self.getPosition()[0]+self.movementSpeed, self.getPosition()[1]))

        self.movementSpeed = self.movementSpeed - self.movementSpeed / self.friction

    def checkKeys (self, keyEvent):

        if keyEvent.type == pygame.KEYDOWN:

            if (keyEvent.key == pygame.K_LEFT):
            	self.control = -1

            elif (keyEvent.key == pygame.K_RIGHT):
            	self.control = 1

        elif (keyEvent.type == pygame.KEYUP):
            if (keyEvent.key == pygame.K_LEFT or keyEvent.key == pygame.K_RIGHT):
                self.control = 0

        print("control changed: " + str(self.control))

    def tick(self, deltaTime, keyEvent=False):
        self.anim(deltaTime)
        self.updatePos(deltaTime)
        if keyEvent is not False:
            self.checkKeys (keyEvent)
