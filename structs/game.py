import numpy as np

class Game:
    def __init__(self, deck, strat, stats):
        self.deck = deck
        self.strat = strat
        self.stats = stats

        self.turn_count = 0
        self.hand = []
        self.graveyard = []

    def run(self):
        self.deck.shuffle()
        self.__mulligan()

    def __mulligan(self):
        mulligan_count = 0
        while mulligan_count < 8:
            hand = self.deck.look_top(number=7)

            result = self.strat.mulligan_strat(hand=hand, mull_counter=mulligan_count)
            if result == "Success":
                break
            elif result == "Fail":
                mulligan_count = np.nan
                break

            self.deck.shuffle()
            mulligan_count += 1

        # record stats
        self.stats.mulligan_count.append(mulligan_count)

        # draw 7 cards
        self.hand = self.deck.draw_top(7)

        # mulligan extra cards away
        if result != "Fail" and mulligan_count > 1:
            self.hand, to_mulligan = self.strat.get_opening_hand(cards=self.hand, num_to_keep=min(8-mulligan_count, 7))

            # bottom unwanted cards
            self.deck.put_cards_deck(cards=to_mulligan, where="bottom")
