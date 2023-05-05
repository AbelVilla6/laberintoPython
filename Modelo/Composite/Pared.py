from Composite.ElementoMapa import ElementoMapa
class Pared(ElementoMapa):
	def entrar():
		print("Te has chocado con una pared")

	def __str__(self):
		return "Una pared"
	
	#Método para los test unitarios
	def esPared(self):
		return True
	
	