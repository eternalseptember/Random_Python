from cards import *

class OldMaidHand(Hand):
	def remove_matches(self):
		count = 0
		original_cards = self.cards[:]
		for card in original_cards:
			match = Card(3 - card.suit, card.rank)
			if match in self.cards:
				self.cards.remove(card)
				self.cards.remove(match)
				print("{0}\'s hand: {1} matches {2}".format(self.name, card, match))
				count += 1
		return count


class OldMaidGame(CardGame):
	def play(self, names):
		# Remove Queen of Clubs
		self.deck.remove(Card(0,12))

		# Make a hand for each player
		self.hands = []
		for name in names:
			self.hands.append(OldMaidHand(name))

		# Deal the cards
		self.deck.deal(self.hands)
		print("---------------- Cards have been dealt.")
		self.print_hands()

		# Remove initial matches
		matches = self.remove_all_matches()
		print("---------------- Matches discarded, play begins.")
		self.print_hands()

		# Play until all 50 cards are matched
		turn = 0
		num_hands = len(self.hands)
		while matches < 25:
			matches += self.play_one_turn(turn)
			turn = (turn + 1) % num_hands

		print("---------------- Game is Over.")
		self.print_hands()


	def print_hands(self):
		for hand in self.hands:
			print(hand)


	def remove_all_matches(self):
		count = 0
		for hand in self.hands:
			count += hand.remove_matches()
		return count


	def play_one_turn(self, i):
		if self.hands[i].is_empty():
			return 0
		neighbor = self.find_neighbor(i)
		picked_card = self.hands[neighbor].pop()
		self.hands[i].add(picked_card)
		print(self.hands[i].name, "picked", picked_card, "from", self.hands[neighbor].name)
		count = self.hands[i].remove_matches()
		self.hands[i].shuffle()
		return count


	def find_neighbor(self, i):
		num_hands = len(self.hands)
		for next in range(1, num_hands):
			neighbor = (i + next) % num_hands
			if not self.hands[neighbor].is_empty():
				return neighbor




'''
game = CardGame()
hand = OldMaidHand("Frank")
game.deck.deal([hand], 13)
print(hand)
hand.remove_matches()
print(hand)
'''

game = OldMaidGame()
game.play(["Allen", "Jeff", "Chris"])