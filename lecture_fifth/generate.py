from random import choice, randint, shuffle

coin = choice(["heads" "tails"])
dnd_dice = randint(1, 10)
cards = ["jack", "queen", "king", "ace"]

shuffle(cards)
for card in cards:
    print(card)