from Composite.ElementoMapa import ElementoMapa
class Puerta(ElementoMapa):
	def __init__(self):
		self.abierta = True
		self.lado1 = None
		self.lado2 = None

	def cerrar(self):
		self.abierta = False
		 
	def entrar(self):
		if self.abierta:
			print("Puedes pasar al otro lado") 
			return
		print("La puerta está cerrada")

	def __str__(self):
		return "Una puerta"