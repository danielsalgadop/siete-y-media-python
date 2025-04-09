#!/usr/bin/env python
import pprint

pp = pprint.PrettyPrinter(indent=4)


class Carta():
    def __init__(self, palo, valor, private=True):
        self.private = private
        self.palo = palo
        self.valor = valor

    def __str__(self):
        if self.private:
            return '|*' + str(self.valor) + ' ' + self.palo + '*|'
        #     return '| * |'
        return '| ' + str(self.valor) + ' ' + self.palo + ' |'
