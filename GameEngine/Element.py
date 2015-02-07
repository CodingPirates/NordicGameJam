# This class is used for creating screen elements
class Element:

	def __init__(self, xPos, yPos, size, image, layer):
		self.pos   = (x,y)
		self.size  = size
		self.image = image
		self.layer = layer

	# get get lower left pixel position
	def getPosition():
		return self.pos

	# get box surrounding element (the size of element)
	def getBoundingBox():
		return self.size

	# get the current Image for this element
	def getSurface():
		return self.image

	# get depth in image
	#  0: Background
	#  1: Background elements
	# 10: Enemies
	# 11: Player
	# 12: Foreground elements
	def getLayer():
		return self.layer

	def setPosition(Newpos):
		if (newPos[0] < 0 || newPos[0] > 1024):
			print "You gone fucked with the x postion"
			break
		elif(newPos[0] < 0 || newPos[0] > )
		else:
			pos[0] = newPos[0]
			pos[1] = newPos[1]

	def setSurfaceAndBox(image, size):
		self.image = image
		self.size  = size

	# update all element data (delta time is in milliseconds)
	# keyEvent is only if key has been pressed
	def tick(deltaTime, keyEvent=False):
