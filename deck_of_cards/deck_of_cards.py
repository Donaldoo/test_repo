#!/usr/bin/python3
import random

class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def showCard(self):
        print("{} {}".format(self.value, self.suit))

    def evaluate_points(self):
        if self.value == "J" or self.value == "Q" or self.value == "K":
            return 10
        elif self.value == "A":
            return 11
        else:
            return int(self.value)


class Deck:
    cardRank = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
    suits = ["\u2666", "\u2665", "\u2663", "\u2660"]

    def __init__(self):
        self.deck = []
        self.build()

    def build(self):
        for s in self.suits:
            for v in self.cardRank:
                self.deck.append(Card(s, v))

    def showDeck(self):
        for c in self.deck:
            c.showCard()

    def shuffle(self):
        random.shuffle(self.deck)

    def drawCard(self):
        return self.deck.pop()


class Player:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.hand = []

    def draw(self, deck):
        self.hand.append(deck.drawCard())
        return self

    def showHand(self):
        for card in self.hand:
            card.showCard()

    def evaluate_points(self):
        points = [c.evaluate_points() for c in self.hand]
        total = sum(points)
        print("{} points".format(total))
        return total



"""Tests"""
deck = Deck()
deck.shuffle()

p1 = Player("p1", 50)
p2 = Player("p2", 51)

for i in range(5):
    p1.draw(deck)
    p2.draw(deck)

print("Player 1:")
p1.showHand()
p1_points = p1.evaluate_points()

print("\nPlayer 2:")
p2.showHand()
p2_points = p2.evaluate_points()

if p1_points > p2_points:
    print("\nPlayer 1 wins")
elif p2_points > p1_points:
    print("\nPlayer 2 wins")
else:
    print("\nDraw")

