import Player

class KeyInput ():

	def checkKeys ():

		self.player = Player.Player ()

		for event in pygame.event.get():

	        if event.type == KEYDOWN:

	        	if event.type == QUIT:

	                    pygame.quit ()

	                    sys.exit ()

	            if (event.key == K_LEFT):

	            	player.control = -1

	            elif (event.key == K_RIGHT):

	            	player.control = 1

	            else

	            	player.control = 0