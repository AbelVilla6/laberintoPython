class Laberinto:
	def __init__(self):
		self.habitaciones = list()

	def agregarHabitacion(self, habitacion):
		self.habitaciones.append(habitacion)

	def obtenerHabitacion(self, posicion):
		return self.habitaciones[posicion-1]

