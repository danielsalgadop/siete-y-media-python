#!/usr/bin/env python
import carta
import jugador
import random
import os
unMazo = carta.Mazo()
#~ unMazo
unMazo.mezclar()
class Tablero:
	def __init__(self,num_jug=1):
		self.ListaJugadores = []
		for i in range(num_jug):
			
			n = random.random();
			self.ListaJugadores.append(jugador.Jugador("jagador"+str(n)))
		self.ListaJugadores.append(jugador.Jugador("bankia"))
			
	def __str__ (self,header="default_HEADER",footer="default_FOOTER"):
		os.system('clear')
		r = header+"\n"
		r += "="*10+"\n"
		for jugador in self.ListaJugadores:
			r += jugador.nombre+"\n"
			r += jugador.mostrarCartas()
			r += "\n"
		r += "="*10+"\n"
		r += footer+"\n"
		return r
		#~ 
	#~ def __call__ (self,header="DSD CALL HEADER",footer="DSD CALL FOOTER"):
		#~ return str(header,footer)
	def darCartaJugador(self,jugador):
		#~ print "dar carta a jugador"+jugador.nombre
		carta = unMazo.darCarta()
		jugador.agregarCarta(carta)
		
		
	def ListJugadores(self):
		return self.ListaJugadores

	def ResultsFinales(self):
		print "RESULTSSSSSSSSSSSSSSSSSSSS\n"
		for j in self.ListaJugadores:
			listaCartas = j.ListaObjCartasUnJugador(j)
			#~ print "para este jugador="+j.nombre+" tiene un total= "+str(j.total)+"\n"
			cartas = ""
			for unacarta in listaCartas:
				cartas += str(unacarta)
			print j.nombre
			print cartas
			print j.total
	def CalculosBankia(self):
		print "Calcular quien esta CROCRO mas cerca, para saber cuanto me tengo que acercar"
		print "BANK\n"*44
		for j in self.ListaJugadores:
			listaCartas = j.ListaObjCartasUnJugador(j)
			#~ print "para este jugador="+j.nombre+" tiene un total= "+str(j.total)+"\n"
			cartas = ""
			for unacarta in listaCartas:
				cartas += str(unacarta)
			print j.nombre
			print cartas
			print j.total

