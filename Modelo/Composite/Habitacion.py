from Composite.Contenedor import Contenedor

class Habitacion(Contenedor):
	def __init__(self):
		super(Habitacion,self).__init__()
		self.norte = None
		self.sur = None
		self.este = None
		self.oeste = None
	
	def __str__(self):
		return ("\n\nLA HABITACIÓN NÚMERO: " + str(self.num) +
            "\n Tiene en Norte: " + str(self.norte) +
            "\n Tiene en Sur: " + str(self.sur) +
            "\n Tiene en Este: " + str(self.este) +
            "\n Tiene en Oeste: " + str(self.oeste) +
            "\n " + super(Habitacion, self).printHijos())
	
	def entrar(self):
		print("Estás en la habitación" + str(self.num))
	
