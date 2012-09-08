#!/usr/bin/env python
#~ import carta
#~ import jugador
import tablero
import pprint
pp = pprint.PrettyPrinter(indent=4)
#~ partida =["inicio","jugador","banca","results"]
class Partida:
	estado=["jugador","banca","results"]
	def __init__(self, fecha="unaFecha"):
		self.fecha = fecha
		self.num_jug="0"
		# opciones del usuario
		ObjTablero = tablero.Tablero(input('Numero de jugadores'))
		for jugador in  ObjTablero.ListJugadores():
			ObjTablero.darCartaJugador(jugador)
			print ObjTablero
			if jugador.nombre == "bankia":
				pass
			else:
				resp = raw_input("quieres otra carta   (s - si /n - no / p planto /q - quit)")
				# Dar cuantas cartas quiera sin pasarse de 7.5
				while resp == "s":
					ObjTablero.darCartaJugador(jugador)
					print ObjTablero
					if jugador.eliminado == "no":
						resp = raw_input("quieres otra carta")
					else:
						resp = "n"
		for xjugador in  ObjTablero.ListJugadores():
			if xjugador.nombre == "bankia":
				ObjTablero.CalculosBankia
		
				
				# Calcular las probabilidades
			#~ print UnTablero("footer")
		ObjTablero.ResultsFinales()

ObjPartida = Partida()
		
