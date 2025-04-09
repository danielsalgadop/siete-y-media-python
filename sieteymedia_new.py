#!/usr/bin/env python

import mazo
import jugador
import os



class Partida:
    def __init__(self, names):
        self.mazo = mazo.Mazo()
        self.players = [];
        # generate players
        print("vamos a jugar al siete y media" + " num_players=[" + str(len(names)) + "]")
        # give 1 card to each player
        for name in names:
            self.players.append(jugador.Jugador(name, self.mazo.darCarta()))

        print(self)
        for player in self.players:
            if(self.user_input_to_boolean(input('Turno de ' + player.nombre + '¿quieres carta?'))):
                # pub_or_private = self.user_input_to_boolean(input('privada?'))
                player.addCard(self.mazo.darCarta())
            print(self)

    def __str__(self):
        ret_str = '';
        for player in self.players:
            ret_str += player.nombre + ' '
            for my_card in player.my_cards:
                ret_str += str(my_card)
            ret_str += '\n'
        return ret_str

    def user_input_to_boolean(self, wants_card):
        if (wants_card.lower() == 's'):
            return True
        return False


partida = Partida(['ana', 'mateo', 'edu', 'maria'])
