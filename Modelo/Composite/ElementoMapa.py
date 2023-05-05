from abc import ABC, abstractmethod

class ElementoMapa(ABC):
	def __init__(self):
		self.padreaMas = None

	@abstractmethod
	def entrar():
		pass

	def recorrer(self,bloque):
		bloque(self)

	#Métodos para los test unitarios
	def esElementoMapa(self):
		return True
	
	def esBaul(self):
		return False
	
	def esContenedor(self):
		return False	
	
	def esHabitacion(self):
		return False
	
	def esHoja(self):
		return False
	
	def esLaberinto(self):
		return False
	
	def esPared(self):
		return False
	
	def esPuerta(self):
		return False
	
	def esBomba(self):
		return False
	
	def esDecorator(self):
		return False
		
	def esEspada(self):
		return False	
	
	def esFuego(self):
		return False


		