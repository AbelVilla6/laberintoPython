from Modelo.Composite.Baúl import Baul
from Modelo.Composite.Habitacion import Habitacion
from Modelo.Composite.Laberinto import Laberinto
from Modelo.Composite.Pared import Pared
from Modelo.Composite.Puerta import Puerta
from Modelo.Decorator.Bomba import Bomba
from Modelo.Decorator.Espada import Espada
from Modelo.Decorator.Fuego import Fuego

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

	def crearPuertaCerrada(self, hab1, hab2):
		puerta = self.crearPuerta(hab1, hab2)
		puerta.cerrar()
		return puerta

	def crearPuertaBomba(self, hab1, hab2):
		puerta = self.crearPuerta(hab1, hab2)
		return self.crearBombaParaDecorar(puerta)

	def crearHabitacion(self, num):
		habitacion = Habitacion()
		habitacion.num = num
		habitacion.norte = self.crearPared()
		habitacion.sur = self.crearPared()
		habitacion.este = self.crearPared()
		habitacion.oeste = self.crearPared()
		return habitacion

	def crearLaberinto(self):
		return Laberinto()

	def crearFuego(self):
		return Fuego()

	def crearBomba(self):
		return Bomba()

	def crearEspada(self):
		return Espada()

	def crearBaul(self):
		return Baul()

	def crearLaberinto2H(self):
		self.laberinto = self.crearLaberinto()
		hab1 = self.crearHabitacion(1)
		hab2 = self.crearHabitacion(2)
		puerta = self.crearPuerta(hab1,hab2)
		hab1.sur = puerta
		hab2.norte = puerta
		self.laberinto.agregarHabitacion(hab1)
		self.laberinto.agregarHabitacion(hab2)

	def crearLaberintoEntrega2(self):
    	#Laberinto
		self.laberinto = self.crearLaberinto()

    	#Habitaciones
		hab1 = self.crearHabitacion(1)	
		hab2 = self.crearHabitacion(2)
		hab3 = self.crearHabitacion(3)
		hab4 = self.crearHabitacionEnLlamas(4)

		#Puertas
		puerta12 = self.crearPuerta(hab1,hab2)
		hab1.este = puerta12
		hab2.oeste = puerta12

		#!.componente ya que la hab4, en realidad es fuego decorando habitacion
		puerta24 = self.crearPuerta(hab2,hab4.componente)
		hab2.sur = puerta24
		hab4.componente.norte = puerta24

		puerta13 = self.crearPuertaCerrada(hab1,hab3)
		hab1.sur = puerta13
		hab3.norte = puerta13

		#!.componente ya que la hab4, en realidad es fuego decorando habitacion
		puerta34 = self.crearPuertaBomba(hab3,hab4.componente)
		hab3.este = puerta34
		hab4.componente.oeste = puerta34

		#Baules
		baul2 = self.crearBaul()
		baul3 = self.crearBaul()

		#Bomba
		bomba = self.crearBomba()

		#Espada
		espada = self.crearEspada()

		#Composite para agregar Baul a Habitación
		baul2.agregarHijo(bomba)
		baul3.agregarHijo(espada)
		hab2.agregarHijo(baul2)
		hab3.agregarHijo(baul3)

		#Agragar habitaciones al laberinto
		self.laberinto.agregarHabitacion(hab1)
		self.laberinto.agregarHabitacion(hab2)
		self.laberinto.agregarHabitacion(hab3)
		self.laberinto.agregarHabitacion(hab4)

	def crearHabitacionEnLlamas(self, num):
		hab = self.crearHabitacion(num)
		return self.crearFuegoParaDecorar(hab)

	def crearFuegoParaDecorar(self, componente):
		fuego = self.crearFuego()
		fuego.decorar(componente)
		return fuego 

	def crearBombaParaDecorar(self, componente):
		bomba = self.crearBomba()
		bomba.decorar(componente)
		return bomba 



    