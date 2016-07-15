class Card:
	suits = ["Clubs", "Diamonds", "Hearts", "Spades"]
	ranks = ["narf", "Ace", "2", "3", "4", "5", "6", "7", 
			 "8", "9", "10", "Jack", "Queen", "King"]


	def __init__(self, suit=0, rank=0):
		self.suit = suit
		self.rank = rank


	def __str__(self):
		return (self.ranks[self.rank] + " of " + self.suits[self.suit])


	def cmp(self, other):
		# Check the suits.
		if self.suit > other.suit: return 1
		if self.suit < other.suit: return -1
		# Suits are the same, so check ranks.
		if self.rank > other.rank: return 1
		if self.rank < other.rank: return -1
		# Ranks are the same... it's a tie
		return 0


	def __eq__(self, other):
		return self.cmp(other) == 0

	def __le__(self, other):
		return self.cmp(other) <= 0

	def __ge__(self, other):
		return self.cmp(other) >= 0

	def __gt__(self, other):
		return self.cmp(other) > 0

	def __lt__(self, other):
		return self.cmp(other) < 0

	def __ne__(self, other):
		return self.cmp(other) != 0



class Deck:
	def __init__(self):
		self.cards = []
		for suit in range(4):
			for rank in range(1, 14):
				self.cards.append(Card(suit, rank))


	def print_deck(self):
		for card in self.cards:
			print(card)


	def __str__(self):
		s = ""
		for i in range(len(self.cards)):
			s = s + " "*i + str(self.cards[i]) + "\n"
		return s


	def shuffle(self):
		import random
		rng = random.Random()
		rng.shuffle(self.cards)
		'''
		num_cards = len(self.cards)
		for i in range(num_cards):
			j = rng.randrange(i, num_cards)
			(self.cards[i], self.cards[j]) = (self.cards[j], self.cards[i])
		'''


	def remove(self, card):
		if card in self.cards:
			self.cards.remove(card)
			return True
		else:
			return False


	def pop(self):
		return self.cards.pop()


	def is_empty(self):
		return self.cards == []


	def deal(self, hands, num_cards=999):
		num_hands = len(hands)
		for i in range(num_cards):
			if self.is_empty():
				break					# Break if out of cards
			card = self.pop()			# Take the top card
			hand = hands[i % num_hands]	# Whose turn is next?
			hand.add(card)				# Add the card to the hand



class Hand(Deck):
	def __init__(self, name=""):
		self.cards = []
		self.name = name


	def add(self, card):
		self.cards.append(card)


	def __str__(self):
		s = self.name + "\'s hand"
		if self.is_empty():
			s += " is empty.\n"
		else:
			s += " contains:\n"
		return s + Deck.__str__(self)



'''
card1 = Card(1,11)
# print(card1)
card2 = Card(1,3)
# print(card2.suits[1])
card3 = Card(1, 11)
print(card1 < card2)
print(card1 == card3)

red_deck = Deck()
blue_deck = Deck()
red_deck.shuffle()
print(red_deck)
'''
deck = Deck()
deck.shuffle()
hand = Hand("frank")
deck.deal([hand], 5)
print(hand)





