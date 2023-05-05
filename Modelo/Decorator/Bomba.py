from Decorator.Decorator import Decorator

class Bomba(Decorator):
	def __init__(self):
		super(Bomba,self).__init__()
	
	def entrar(self):
		print("He explotado. Te has comido una bomba")
		super(Bomba,self).entrar()

	def __str__(self):
		return "Soy bomba y estoy decorando -> " + str(self.componente)
	
	#Método para los test unitarios
	def esBomba(self):
		return True