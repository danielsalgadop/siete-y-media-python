#!/usr/bin/env python

class Jugador:
    # ~ cartasJugador=[]

    def __init__(self, nombre, card):
        self.nombre = nombre
        self.my_cards = []
        self.total = 0
        self.addCard(card)
        self.eliminated = False

    def __str__(self):
        r = 'Name [' + self.nombre + ']'
        r += 'Value [' + str(self.total) + ']'
        r += 'Eliminated [' + str(self.eliminated) + ']'
        return r

    def addCard(self, carta):

        self.my_cards.append(carta)
        if (carta.valor > 9):
            self.total += 0.5
        else:
            self.total += carta.valor
        if self.total > 7.5:
            self.eliminated = True

    def mostrarCartas(self):
        # ~ que cartas tiene
        # ~ r = ""
        for unacarta in self.my_cards:
            r = [unacarta.valor, unacarta.palo]
        # ~ cartapalo = "("
        # ~ cartapalo += str(unacarta.valor)
        # ~ cartapalo += " "
        # ~ cartapalo += unacarta.palo
        # ~ cartapalo += ")"
        # ~ r += cartapalo
        return r

    def ListaObjCartasUnJugador(self, jugador):
        r = []
        for unacarta in self.my_cards:
            r.append(unacarta)
        return r


class Bankia(Jugador):
    # Si que podia ser un singleton
    nivel = 0
    puntuacion_max_jug = 0
