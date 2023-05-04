from Contenedor import Contenedor

class Habitacion(Contenedor):
	def __init__(self):
		super(Habitacion,self).__init__()
		self.norte = None
		self.sur = None
		self.este = None
		self.oeste = None

	def entrar(self)
		print("Estás en la habitación" + self.num)
	
