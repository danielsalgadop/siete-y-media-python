#!/usr/bin/env python
#~ import carta
#~ import jugador
# probando branches

#~ import tablero
import pprint
pp = pprint.PrettyPrinter(indent=4)

import carta
import jugador
import random
import os
#~ import sieteymedia
unMazo = carta.Mazo()
unMazo.mezclar()
tipoOutput = "t";  # t es terminal, h es html #TODO poner esto superglobal (por esta razon he quitado tablero.py y "arrejuntao" scripts
def meVes():
	print "viendo-t"
class Tablero:
	def __init__(self,num_jug=1):
		self.ListaJugadores = []
		for i in range(num_jug):
			
			n = random.random();
			self.ListaJugadores.append(jugador.Jugador("jagador"+str(n)))
		self.ListaJugadores.append(jugador.Jugador("bankia"))
			
	def __str__ (self,header="default_HEADER",footer="default_FOOTER"):
		r=""
		if(tipoOutput=="t"):
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
		bankia =""
		print "Calcular quien esta CROCRO mas cerca, para saber cuanto me tengo que acercar"
		#~ print "BANK\n"*44
		mas_cerca = 0;
		for j in self.ListaJugadores:
			print j
		for j in self.ListaJugadores:
			listaCartas = j.ListaObjCartasUnJugador(j)
			#~ print "para este jugador="+j.nombre+" tiene un total= "+str(j.total)+"\n"
			if j.nombre == "bankia":
				bankia = j
				print bankia
				print bankia.total
			else:
				if j.eliminado != "si":
					if j.total > mas_cerca:
						mas_cerca = j.total

			# para ganar tengo q mejorar mas_cerca
			if mas_cerca !=  0:  # si es cero, bankia no hace nada y gana
				#diff_con_jugador = bankia.total - mas_cerca
				print "el mas cerca es"
				print mas_cerca
				print "el mas cerca es"
			# Decidir si bankia tiene q jugar
			
			#~ for unacarta in listaCartas:
				#~ cartas += str(unacarta)


#~ partida =["inicio","jugador","banca","results"]
class Partida:
	estado=["jugador","banca","results"]
	nivel = 99
	def __init__(self, fecha="unaFecha"):
		self.fecha = fecha
		self.num_jug="0"
		# opciones del usuario
		ObjTablero = Tablero(input('Numero de jugadores'))
		mensaje_quieres_carta = "quieres otra carta   (s - si /n - no / p planto /q - quit)"
		for jugador in  ObjTablero.ListJugadores():
			ObjTablero.darCartaJugador(jugador)
			print ObjTablero
			if jugador.nombre == "bankia":
				pass
			else:
				resp = raw_input(mensaje_quieres_carta)
				# Dar cuantas cartas quiera sin pasarse de 7.5
				while resp == "s":
					ObjTablero.darCartaJugador(jugador)
					print ObjTablero
					if jugador.eliminado == "no":
						resp = raw_input(mensaje_quieres_carta)
					else:
						resp = "n"
		for xjugador in  ObjTablero.ListJugadores():
			if xjugador.nombre == "bankia":
				ObjTablero.CalculosBankia();
		
				
				# Calcular las probabilidades
			#~ print UnTablero("footer")
		ObjTablero.ResultsFinales()

ObjPartida = Partida()
		
