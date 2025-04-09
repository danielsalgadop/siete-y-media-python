from unittest import TestCase
import carta


class TestCarta(TestCase):
    def test_private_card(self):
        card = carta.Carta('Oros', 1, True)
        self.assertEqual(str(card), '| * |')

    def test_public_card(self):
        card = carta.Carta('Oros', 1, False)
        self.assertEqual(str(card), '| 1 Oros |')
