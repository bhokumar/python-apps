from card import Card
from deck import Deck
import unittest

class CardTests(unittest.TestCase):
	def setUp(self):
		self.card = Card("Hearts", "A")

	def test_init(self):
		""" cards should have a suit and a value"""
		self.assertEqual(self.card.suite, "Hearts")
		self.assertEqual(self.card.value, "A")

	def test_repr(self):
		"""repr should return a string of the form 'VALUE of SUITE' """
		self.assertEqual(repr(self.card), 'A of Hearts')

class DeckTest(unittest.TestCase):
	"""docstring for DeckTest"""
	def __init__(self, arg):
		super(DeckTest, self).__init__()
		self.arg = arg
		