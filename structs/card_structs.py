from random import shuffle


class Card:
    def __init__(self, role_tag, cmc=0, has_summoning_sickness=True):
        self.role_tag = role_tag
        self.cmc = cmc

        self.has_summoning_sickness = has_summoning_sickness

    def __str__(self):
        return f"{self.role_tag}"


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

    def put_cards_deck(self, cards, where):
        if where == "top":
            self.cards = cards + self.cards
        if where == "bottom":
            self.cards = self.cards + cards
        else:
            raise NotImplementedError
