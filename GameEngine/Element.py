import pygame

# This class is used for creating screen elements
class Element(object):

	def __init__(self, position, size, image, layer):
		self.position = position
		self.size  = size
		self.image = image
		self.layer = layer

	def setScene(self, scene):
		self.scene = scene

	def setPosition(self, newPos):
		self.position = newPos

	# get get lower left pixel position
	def getPosition(self):
		return self.position

	# get box surrounding element (the size of element)
	def getRect(self):
		return pygame.Rect(self.image.get_rect(bottomleft=self.position))

	# get the current Image for this element
	def getSurface(self):
		return self.image

	# get depth in image
	#  0: Background
	#  1: Background elements
	# 10: Enemies
	# 11: Player
	# 12: Foreground elements
	def getLayer(self):
		return self.layer


	def setSurfaceAndBox(self, image, size):
		self.image = image
		self.size  = size

	# update all element data (delta time is in milliseconds)
	# keyEvent is only if key has been pressed
	def tick(self, deltaTime, keyEvent=False):
		return None
