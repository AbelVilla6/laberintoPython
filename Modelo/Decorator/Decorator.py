from Composite.Hoja import Hoja

class Decorator(Hoja):
	def __init__(self):
		super(Decorator,self).__init__()
		self.estado = None
		self.componente = None

	def decorar(self,elementoMapa):
		self.componente = elementoMapa
		
	def entrar(self):
		if self.componente is not None:
			self.componente.entrar()