from abc import ABC, abstractmethod
from Composite.ElementoMapa import ElementoMapa

class Hoja(ElementoMapa, ABC):
	def __init__(self):
		super(Hoja,self).__init__()
