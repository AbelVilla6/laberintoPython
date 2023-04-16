class Juego:
	def __init__(self):
		self.laberinto = None

	def crearPared(self):
		return Pared()

	def crearPuerta(self, hab1, hab2):
		puerta = Puerta()
		puerta.lado1 = hab1
		puerta.lado2 = hab2
		return puerta

	def crearHabitacion(self, num):
		habitacion = Habitacion()
		habitacion.num = num
		return habitacion

	def crearLaberinto(self):
		return Laberinto()

	def crearLaberinto2H(self)
		self.laberinto = self.crearLaberinto()
		hab1 = self.crearHabitacion(1)
		hab2 = self.crearHabitacion(2)
		puerta = self.crearPuerta(hab1,hab2)
		hab1.norte = self.crearPared()
		hab1.oeste = self.crearPared()
		hab1.este = self.crearPared()
		hab2.sur = self.crearPared()
		hab2.oeste = self.crearPared()
		hab2.este = self.crearPared()
		hab1.sur = puerta
		hab2.norte = puerta
		self.laberinto.agregarHabitacion(hab1)
    	self.laberinto.agregarHabitacion(hab2)

