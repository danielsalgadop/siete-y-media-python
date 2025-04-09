#!/usr/bin/env python
import carta

class Mazo:
	#~ def EligePalo():
	def __init__(self):
		self.cartas = []
		for palo in ['Bastos','Oros','Diamantes','Copas']:
			for valor in [1,2,3,4,5,6,7,10,11,12]:
				self.cartas.append(carta.Carta(palo, valor))
		self.mezclar()
			
	def mezclar(self):
		import random
		nCartas = len(self.cartas)
		for i in range(nCartas):
			j = random.randrange(i, nCartas)
			self.cartas[i], self.cartas[j] = self.cartas[j], self.cartas[i]

	def darCarta(self, is_private = True):
		card = self.cartas.pop()
		card.private = is_private
		return card