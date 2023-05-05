from abc import ABC, abstractmethod
from Composite.ElementoMapa import ElementoMapa

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

	def printHijos(self):
		hijos_descripcion = ', '.join([str(hijo) for hijo in self.hijos])
		return "Tiene los hijos: [" + hijos_descripcion + "]"
		#return "Tiene los hijos: " + self.hijos

	def recorrer(self,bloque):
		super(Contenedor,self).recorrer(bloque)
		for each in self.hijos:
			each.recorrer(bloque)
		
	#Método para los test unitarios
	def esContenderor(self):
		return True