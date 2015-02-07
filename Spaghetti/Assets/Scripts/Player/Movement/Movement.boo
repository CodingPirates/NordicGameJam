import UnityEngine

class Movement (MonoBehaviour):
	
	private moveHor as single
	
	public moveSpeed as single = 5.0f
	public jumpSpeed as single = 250.0f
	
	def Update ():
		
		if Input.GetAxis ("Horizontal"):
			
			moveHor = Input.GetAxis ("Horizontal")
			
			rigidbody2D.velocity.x = (moveHor * moveSpeed)