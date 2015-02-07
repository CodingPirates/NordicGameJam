class Scene:

    def __init__(self):
    	# empty list of elements
    	player = Player()
    	this.elements = [player]
    	this.viewport = this.Viewport(player)

	def addElement(element: Element):
		element.setScene(this)
		this.elements[] = element

	def removeElement(element):
		elements.remove(element)

	def getSurface():
		this.viewport.getSurface()

	def tick(deltaTime, keyEvent=False):
		# iterate over all elements and update their state
		for currentElement in this.elements:
			currentElement.tick(deltaTime)

	def control(event):
		# iterate over all elements and update their state
		for currentElement in this.elements:
			currentElement.tick(deltaTime, keyEvent)
