from Decorator.Decorator import Decorator

class Espada(Decorator):
	def __init__(self):
		super(Espada,self).__init__()
		
	def entrar(self):
		print("Anda! Has encontrado una espada!")
		super(Espada,self).entrar()

	def __str__(self):
		return "Soy espada y estoy decorando -> " + str(self.componente)