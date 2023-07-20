from random import shuffle


class Card:
    def __init__(self, role_tag):
        self.role_tag = role_tag


class Deck:
    def __init__(self, commander, cards):
        self.commander = commander
        self.cards = cards

        self.__size_check()

    def __size_check(self):
        assert len(self.cards) == 99

    def shuffle(self):
        shuffle(self.cards)

    def look_top(self, number):
        return self.cards[:number]

    def draw_top(self, number):
        draw, self.cards = self.cards[:number], self.cards[number:]
        return draw
