import numpy as np

class Game:
    def __init__(self, deck, strat, stats, turn_limit):
        self.deck = deck
        self.strat = strat
        self.stats = stats
        self.turn_limit = turn_limit

        self.turn_count = 0
        self.command_zone = []
        self.hand = []
        self.graveyard = []
        self.field = []

        self.max_mana = 0
        self.current_mana = 0

    def run(self):
        self.command_zone.append(self.deck.commander)
        self.deck.commander = []

        self.deck.shuffle()
        self.__mulligan()

        while self.turn_count < self.turn_limit:
            self.run_turn()

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
        to_mulligan = []
        if result != "Fail" and mulligan_count > 1:
            self.hand, to_mulligan = self.strat.get_opening_hand(cards=self.hand, num_to_keep=min(8-mulligan_count, 7))

            # bottom unwanted cards
            self.deck.put_cards_deck(cards=to_mulligan, where="bottom")

        # TODO: maybe preprocess this before saving to stats?
        self.stats.mulligan_keeps_dumps.append((self.hand, to_mulligan))

    def __update_card_zone(self, zone, deltas):
        for delta in deltas:
            if delta[1] == '+':
                zone.append(delta[0])
            elif delta[1] == '-':
                zone.remove(delta[0])

    def run_turn(self):
        # update vars
        self.turn_count += 1
        self.current_mana = self.max_mana

        # check strategy
        hand_deltas, field_deltas, grave_deltas,\
        command_zone_deltas, max_mana_deltas, self.current_mana = self.strat.run_turn_strat(hand=self.hand,
                                                                                            command_zone=self.command_zone,
                                                                                            max_mana=self.current_mana)

        # implement strategy
        self.__update_card_zone(zone=self.hand, deltas=hand_deltas)
        self.__update_card_zone(zone=self.field, deltas=field_deltas)
        self.__update_card_zone(zone=self.graveyard, deltas=grave_deltas)
        self.__update_card_zone(zone=self.command_zone, deltas=command_zone_deltas)

        for delta in max_mana_deltas:
            if delta[1] == '+':
                self.max_mana += delta[0]
            elif delta[1] == '-':
                self.max_mana -= delta[0]

        # record statistics
        self.stats.turn_logs.append({"turn_count": self.turn_count,
                                     "max_mana": self.max_mana,
                                     "current_mana": self.current_mana,
                                     "hand": self.hand,
                                     "commmand_zone": self.command_zone})
