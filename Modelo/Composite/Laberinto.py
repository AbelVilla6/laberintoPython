from Composite.Contenedor import Contenedor
class Laberinto(Contenedor):
	def __init__(self):
		super(Laberinto,self).__init__()
		

	def __str__(self):
		return "\nBIENVENIDO AL LABERINTO NÚMERO: " + str(self.num) 
	
	def entrar(self):
		print ("Estas jugnado en el laberinto")



