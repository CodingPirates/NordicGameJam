import pygame, sys, Element

class Player (Element.Element):

	# The player controls, no keyboard handling is done n this class all
	movementAcc = 2
	jumpHeight = 4
	movementSpeed = 0
	maxSpeed = 5
	control = 0

	def anim (deltaTime):

		animRightImages [0] = pygame.image.load ('/Graphics/Player/anim/right_walk/player_right_walk01.png')
		animRightImages [1] = pygame.image.load ('/Graphics/Player/anim/right_walk/player_right_walk02.png')
		animRightImages [2] = pygame.image.load ('/Graphics/Player/anim/right_walk/player_right_walk03.png')

		animLeftImages [0] = pygame.image.load ('/Graphics/Player/anim/left_walk/player_left_walk01.png')
		animLeftImages [1] = pygame.image.load ('/Graphics/Player/anim/left_walk/player_left_walk02.png')
		animLeftImages [2] = pygame.image.load ('/Graphics/Player/anim/left_walk/player_left_walk03.png')
		
	def updatePos(deltaTime):
		movementSpeed += movementAcc * deltaTime * control
		if movementSpeed > maxSpeed:
			movementSpeed = 5
		elif movementSpeed < -maxSpeed:
		    movementSpeed = -5
		setPosition(getPostion()[0]+movementSpeed, getPostion()[1])

	def tick(self, deltaTime, keyEvent=False):
		self.anim(deltaTime)
		self.updatePos(deltaTime)
