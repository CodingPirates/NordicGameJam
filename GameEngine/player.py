import pygame, sys, Element

class Player (Element):

	# The player controls, no keyboard handling is done n this class all
	movementSpeed = 2
	jumpHeight    = 4

	def anim (deltaTime):

		changeTimeTop = movementSpeed * 100

		changeTime += deltaTime

		animRightImages [0] = pygame.image.load ('/Graphics/Player/anim/right_walk/player_right_walk01.png')
		animRightImages [1] = pygame.image.load ('/Graphics/Player/anim/right_walk/player_right_walk02.png')
		animRightImages [2] = pygame.image.load ('/Graphics/Player/anim/right_walk/player_right_walk03.png')

		animLeftImages [0] = pygame.image.load ('/Graphics/Player/anim/left_walk/player_left_walk01.png')
		animLeftImages [1] = pygame.image.load ('/Graphics/Player/anim/left_walk/player_left_walk02.png')
		animLeftImages [2] = pygame.image.load ('/Graphics/Player/anim/left_walk/player_left_walk03.png')

		i ++

		if (changeTime >= changeTimeTop):

			if (movementSpeed < 0):

				screen.blit (animLeftImages [i], (x,y))

			elif (movementSpeed < 0):

				screen.blit (animRightImages [i], (x,y))


	def moveRight ():

	    pos = getPostion ()

	    pos[0] += movementSpeed

	    setPostion(pos)

	def moveLeft ():

	    pos = getPostion ()

	    pos[0] -= movementSpeed

	    setPostion ()