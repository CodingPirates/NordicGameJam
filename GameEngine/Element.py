class Element:
	# get get lower left pixel position
	def getPosition():
	
	# get box surrounding element (the size of element)
	def getBoundingBox():

	# get the current Image for this element
	def getSurface():

	# get depth in image
	#  0: Background
	#  1: Background elements
	# 10: Enemies
	# 11: Player
	# 12: Foreground elements 
	def getLayer():

	# update all element data (delta time is in milliseconds)
	# keyEvent is only if key has been pressed
	def tick(deltaTime, keyEvent=False):


