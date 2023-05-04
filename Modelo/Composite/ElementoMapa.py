from abc import ABC, abstractmethod

class ElementoMapa(ABC):
	def __init__(self):
		self.padreaMas = None

	@abstractmethod
	def entrar():
		pass

	def recorrer(self,bloque):
		bloque(self)
		