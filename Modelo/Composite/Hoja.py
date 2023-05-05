from abc import ABC, abstractmethod
from Composite.ElementoMapa import ElementoMapa

class Hoja(ElementoMapa, ABC):
	def __init__(self):
		super(Hoja,self).__init__()

	#Método para los test unitarios
	def esHoja(self):
		return True
