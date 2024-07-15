from mtg_optimizer.structs.game import Game

from collections import Counter


class StrategyZur:

    def __init__(self):
        self.opening_targets = [
            ("land", 3),
            ("ramp", 1),
            ("counter", 99),
            ("protection", 99),
            ("draw", 99),
            ("ability_doubler", 99),
            ("removal", 99),
            ("drannith magistrate", 99),
            ("tutorable_enchantment", 99),
        ]

    def get_opening_hand(self, cards, num_to_keep):
        # TODO: dar um refactor nisto, tá outra vez esparguete por causa do código fora do loop
        to_keep = []
        for type_tuple in self.opening_targets:
            kept = 0
            for card in cards:
                if kept < type_tuple[1] and card.role_tag == type_tuple[0]:
                    to_keep.append(card)
                    kept += 1
                    if len(to_keep) == num_to_keep:
                        to_put_back = [c for c in cards if c not in to_keep]
                        return to_keep, to_put_back

        # this means we couldn't complete a hand
        to_put_back = [c for c in cards if c not in to_keep]
        delta = num_to_keep - len(to_keep)
        to_keep = to_keep + to_put_back[:delta]
        to_put_back = [c for c in cards if c not in to_keep]
        return to_keep, to_put_back

    def mulligan_strat(self, hand, mull_counter):
        stats = self.__get_tag_stats(hand)

        if mull_counter < 5:
            if stats["land"] >= 3 and stats["ramp"] >= 1:
                return "Success"
            else:
                return None
        else:
            return "Fail"

    def run_turn_strat(self, game: Game):

        # 1-play land
        for c in list(game.hand):
            if c.role_tag == "land":
                game.hand.remove(c)
                game.field.append(c)
                game.max_mana += 1
                game.current_mana += 1
                break

        # 2-check for commander play
        if game.command_zone and game.command_zone[0].cmc <= game.current_mana:
            game.current_mana -= game.command_zone[0].cmc
            game.field.append(game.command_zone[0])
            game.command_zone.remove(game.command_zone[0])

        # 3-play ramp
        for c in list(game.hand):
            if c.role_tag == "ramp" and c.cmc <= game.current_mana:
                game.current_mana -= c.cmc
                game.hand.remove(c)
                game.field.append(c)
                game.max_mana += 1

    def __get_tag_stats(self, hand):
        tags = []
        for card in hand:
            tags.append(card.role_tag)

        return Counter(tags)

    def check_objectives(self, game: Game):
        objectives = [False, False]
        for c in game.field:
            if c.role_tag == "commander" and c.has_summoning_sickness == False:
                objectives[0] = True

                for h_c in game.hand:
                    if h_c.role_tag == "counter" and h_c.cmc <= game.current_mana:
                        objectives[1] = True

                for f_c in game.field:
                    if f_c.role_tag == "protection":
                        objectives[1] = True

        return objectives

class StrategyWinota:

    def __init__(self):
        self.opening_targets = [
            ("land", 3),
            ("ramp", 1),
            ("counter", 99),
            ("protection", 99),
            ("draw", 99),
            ("ability_doubler", 99),
            ("removal", 99),
            ("drannith magistrate", 99),
            ("tutorable_enchantment", 99),
        ]

    def get_opening_hand(self, cards, num_to_keep):
        # TODO: dar um refactor nisto, tá outra vez esparguete por causa do código fora do loop
        to_keep = []
        for type_tuple in self.opening_targets:
            kept = 0
            for card in cards:
                if kept < type_tuple[1] and card.role_tag == type_tuple[0]:
                    to_keep.append(card)
                    kept += 1
                    if len(to_keep) == num_to_keep:
                        to_put_back = [c for c in cards if c not in to_keep]
                        return to_keep, to_put_back

        # this means we couldn't complete a hand
        to_put_back = [c for c in cards if c not in to_keep]
        delta = num_to_keep - len(to_keep)
        to_keep = to_keep + to_put_back[:delta]
        to_put_back = [c for c in cards if c not in to_keep]
        return to_keep, to_put_back

    def mulligan_strat(self, hand, mull_counter):
        stats = self.__get_tag_stats(hand)

        if mull_counter < 5:
            if stats["land"] >= 3 and stats["ramp"] >= 1:
                return "Success"
            else:
                return None
        else:
            return "Fail"

    def run_turn_strat(self, game: Game):

        # 1-play land
        for c in list(game.hand):
            if c.role_tag == "land":
                game.hand.remove(c)
                game.field.append(c)
                game.max_mana += 1
                game.current_mana += 1
                break

        # 2-check for commander play
        if game.command_zone and game.command_zone[0].cmc <= game.current_mana:
            game.current_mana -= game.command_zone[0].cmc
            game.field.append(game.command_zone[0])
            game.command_zone.remove(game.command_zone[0])

        # 3-play ramp
        for c in list(game.hand):
            if c.role_tag == "ramp" and c.cmc <= game.current_mana:
                game.current_mana -= c.cmc
                game.hand.remove(c)
                game.field.append(c)
                game.max_mana += 1

    def __get_tag_stats(self, hand):
        tags = []
        for card in hand:
            tags.append(card.role_tag)

        return Counter(tags)

    def check_objectives(self, game: Game):
        objectives = [False, False]
        for c in game.field:
            if c.role_tag == "commander" and c.has_summoning_sickness == False:
                objectives[0] = True

                for h_c in game.hand:
                    if h_c.role_tag == "counter" and h_c.cmc <= game.current_mana:
                        objectives[1] = True

                for f_c in game.field:
                    if f_c.role_tag == "protection":
                        objectives[1] = True

        return objectives