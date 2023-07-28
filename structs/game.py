from collections import Counter

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

        self.deck.shuffle()
        self.__mulligan()

        while self.turn_count < self.turn_limit:
            self.run_turn()

    def __mulligan(self):
        mulligan_count = 0
        while mulligan_count < 8:
            hand = self.deck.look_top(number=7)

            result = self.strat.mulligan_strat(hand=hand, mull_counter=mulligan_count)
            if result:
                break

            self.deck.shuffle()
            mulligan_count += 1

        # record stats
        self.stats.mulligan_count.append(mulligan_count)
        self.stats.mulligan_results.append(result)

        # draw 7 cards
        self.hand = self.deck.draw_top(7)

        # mulligan extra cards away
        to_mulligan = []

        if result == "Fail" or mulligan_count > 1:
            self.hand, to_mulligan = self.strat.get_opening_hand(cards=self.hand, num_to_keep=min(8-mulligan_count, 7))

            # bottom unwanted cards
            self.deck.put_cards_deck(cards=to_mulligan, where="bottom")

        # TODO: maybe preprocess this before saving to stats?
        self.stats.mulligan_keeps_dumps.append((self.hand, to_mulligan))

    def __remove_summoning_sickness(self):
        for card in self.field:
            card.has_summoning_sickness = False

    def run_turn(self):
        # update vars
        self.turn_count += 1
        self.current_mana = self.max_mana
        self.__remove_summoning_sickness()

        # draw for turn
        self.hand = self.hand + self.deck.draw_top(number=1)

        # run strategy for this board state
        self.strat.run_turn_strat(game=self)

        # record statistics
        statistics = {"turn_count": self.turn_count,
                      "max_mana": self.max_mana,
                      "current_mana": self.current_mana,
                      "hand": Counter([str(i) for i in self.hand]),
                      "commander_already_played": len(self.command_zone) == 0,
                      }

        objectives = self.strat.check_objectives(game=self)
        for i, obj in enumerate(objectives):
            statistics[f"objective_{i}"] = obj

        self.stats.turn_logs.append(statistics)
