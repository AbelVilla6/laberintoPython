from Contenedor import Contenedor

class Baul(Contenedor):
	def __init__(self):
		super(Baul,self).__init__()

	def entrar(self):
		print("Dentro del baúl")
		super(Baul,self).entrar()