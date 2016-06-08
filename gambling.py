import random


# Create a black box object that generates random numbers
rng = random.random()
print (rng)

dice_throw = random.randrange(1, 7) # Return an int, one of 1,2,3,4,5,6
print (dice_throw)

r_odd = random.randrange(1, 100, 2) # Random odd number
print (r_odd)

# Generate ints [0...51], representing a deck of cards
cards = list(range(52))
random.shuffle(cards)
print(cards)