#!/usr/bin/env python

class Jugador:
	#~ cartasJugador=[]
	
	def __init__(self, nombre="unNombre"):
		self.nombre = nombre
		self.miscartas=[]
		self.eliminado="no"
		self.total=0
		
	def __str__(self):
		r = self.nombre
		r += "XXXXXXTOTAL\t\t"
		r += str(self.total)
		r += "\t\tXXXXXXELIMINADO"
		r += self.eliminado
		return r
	
	def agregarCarta(self,carta):
		
		self.miscartas.append(carta)
		if (carta.valor > 9):
			self.total += 0.5
		else:
			self.total += carta.valor
		if self.total > 7.5:
			self.eliminado="si"
	
	def mostrarCartas(self):
		#~ que cartas tiene
		#~ r = ""
		for unacarta in self.miscartas:
			r = [unacarta.valor,unacarta.palo]
			#~ cartapalo = "("
			#~ cartapalo += str(unacarta.valor)
			#~ cartapalo += " "
			#~ cartapalo += unacarta.palo
			#~ cartapalo += ")"
			#~ r += cartapalo
		return r

	def ListaObjCartasUnJugador(self,jugador):
		r=[]
		for unacarta in self.miscartas:
			r.append(unacarta)
		return r
		
			

class Bankia(Jugador):
	#Si que podia ser un singleton
	nivel=0
	puntuacion_max_jug = 0
