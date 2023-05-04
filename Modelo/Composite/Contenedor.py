from abc import ABC, abstractmethod

class Contenedor(ElementoMapa, ABC):
	def __init__(self):
		super(Contenedor,self).__init__()
		self.num = None
		self.hijos = []

	def agregarHijo(self, hijo):
		self.hijos.append(hijo)
		#padreaMas = padre
		hijo.padreaMas = self
		
	def obtenerHijo(self, posicion):
		return self.hijos[posicion-1]
