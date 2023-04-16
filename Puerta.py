class Puerta(ElementoMapa):
	def __init__(self):
		self.abierta = False
		self.lado1 = None
		self.lado2 = None

	def entrar(self):
		if self.abierta:
			print("Puedes pasar al otro lado") 
			return
		print("La puerta está cerrada")