from Decorator.Decorator import Decorator

class Fuego(Decorator):
	def __init__(self):
		super(Fuego,self).__init__()
	
	def entrar(self):
		print("Te has quemado")
		super(Fuego,self).entrar()

	def __str__(self):
		return "Soy fuego y estoy decorando -> " + str(self.componente)
	
	#Método para los test unitarios
	def esFuego(self):
		return True
		