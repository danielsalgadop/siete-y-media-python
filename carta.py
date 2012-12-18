#!/usr/bin/env python
import pprint
pp = pprint.PrettyPrinter(indent=4)


class Carta ():
	x=4
	def __init__(self, palo=0, valor=0):
		self.palo = palo
		self.valor = valor
	def __str__(self):
		#return("aqui hay que devolver self.palo y self.valor")
		return("("+str(self.valor)+" "+self.palo+") ")

class Mazo:
	#~ def EligePalo():
	def __init__(self):
		numeros = [1,2,3,4,5,6,7,10,11,12]
		palos = ['Bastos','Oros','Diamantes','Copas']
		self.cartas = [] 
		for palo in palos:
			for valor in numeros:
				self.cartas.append(Carta(palo, valor))
			
	#~ def muestraMazo(self):
	#~ def muestraMazo(self):
		#~ for carta in self.cartas:
			#~ print carta.valor," ",carta.palo

	def mezclar(self):
		import random
		nCartas = len(self.cartas)
		for i in range(nCartas):
			j = random.randrange(i, nCartas)
			self.cartas[i], self.cartas[j] = self.cartas[j], self.cartas[i]

	def darCarta(self):
		return self.cartas.pop()
