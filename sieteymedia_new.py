#!/usr/bin/env python

import mazo
import jugador
import os



class Partida:
    def __init__(self, names):
        self.mazo = mazo.Mazo()
        self.players = []
        # generate players
        print("vamos a jugar al siete y media" + " num_players=[" + str(len(names)) + "]")
        # give 1 card to each player
        for name in names:
            self.players.append(jugador.Jugador(name, self.mazo.darCarta()))
        self.turn = self.players[0]

        print(self)
        actual_player_index = 0
        while self.turn:
            print(self.turn)
            # exit(2)
            if self.user_input_to_boolean(input('Turno de ' + self.turn.nombre + '¿quieres carta?')):
                pub_or_private = self.user_input_to_boolean(input('privada?'))
                self.turn.addCard(self.mazo.darCarta(pub_or_private))
                if self.turn.eliminated:
                    self.turn.allCardsPublic()
                    actual_player_index = self.next_turn(actual_player_index)
            else:
                actual_player_index = self.next_turn(actual_player_index)
            print(self)
        print('Fin partida')
        print(self)

    def next_turn(self, actual_player_index):
        actual_player_index += 1
        if actual_player_index >= len(self.players):
            self.turn = False
        else:
            self.turn = self.players[actual_player_index]
        return actual_player_index

    def __str__(self):
        ret_str = '';
        for player in self.players:
            ret_str += player.nombre + ' '
            for my_card in player.my_cards:
                ret_str += str(my_card)
            if player.eliminated:
                ret_str += 'ELIMINATED'
            ret_str += '\n'
        return ret_str

    def user_input_to_boolean(self, wants_card):
        if (wants_card.lower() == 's'):
            return True
        return False


partida = Partida(['ana', 'mateo', 'edu', 'maria'])
